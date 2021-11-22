
# -*- coding: UTF-8 -*-

# 实现协议前端的类；

# 模块内应当有一个或多个实现协议前端的类，通过对网络输入的数据流的处理，实现优化的可用的输出数据流，并提供状态的接口；
# 实现内容如，一个用于前端接口的类，实现Telnet的信令协商，处理信令协商和反馈，在流中屏蔽底层协议内容，
# 通过Telnet协商状态提供需要的状态接口，对输入流进行拆分使其成为更易于处理的流，交由后级调用，
# 接收后级处理完成的信息，根据Telnet协商状态将传回信息编码传回；
# 可尝试实现对用户字符集的自适应处理，；

from ..OLDLog import logger;
from .CONSTS import *;

__all__ = [
    "Front"
];



class Front:

    WILL        = 0x0001;
    WONT        = 0x0002;
    DO          = 0x0004;
    DONT        = 0x0008;
    WQUERYING   = 0x0010;
    DQUERYING   = 0x0040;

    OP_ECHO     = TEL_OP_ECHO;
    OP_SPRGA    = TEL_OP_SPRGA;
    OP_NAWS     = TEL_OP_NAWS;
    OP_TTYP     = TEL_OP_TTYP;
    OP_LNMOD    = TEL_OP_LNMOD;

    SUPPORTED   = {OP_ECHO, OP_SPRGA, OP_NAWS, OP_TTYP};

    TYPE = 'TEL FRONT';

    def __init__(self, conn, logger = logger, code = 'ascii', autoecho = False, autoga = False) -> None:
        self.code = code;
        self.conn = conn;
        self.logger = logger;
        self.status = {};
        self._recvbuff = b'';
        self._recvqueue = [];
        self._opst_echo_autoecho = autoecho;
        self._opst_sprga_autoga = autoga;
        self._opst_ttyp_terminaltype = 'UNKNOWN';
        self._opst_naws_windowsize = None;
        return;
    
    @property
    def _opst_echo_willecho(self):
        if TEL_OP_ECHO in self.status and self.status[TEL_OP_ECHO] & self.WILL:
            return True;
        else:
            return False;
    
    @property
    def _opst_echo_doecho(self):
        if TEL_OP_ECHO in self.status and self.status[TEL_OP_ECHO] & self.DO:
            return True;
        else:
            return False;
    
    @property
    def _opst_sprga_willsprga(self):
        if TEL_OP_SPRGA in self.status and self.status[TEL_OP_SPRGA] & self.WILL:
            return True;
        else:
            return False;

    @property
    def _opst_sprga_dosprga(self):
        if TEL_OP_SPRGA in self.status and self.status[TEL_OP_SPRGA] & self.DO:
            return True;
        else:
            return False;

    def _deal(self, s:bytes) -> tuple:
        if len(s) == 0:
            return b'', b'';
        elif s[:1] == TEL_IAC:
            if len(s) == 1:
                return b'', s;
            elif len(s) >= 2 and s[:2] != TEL_CMD_SB and s[:2] not in TELS_OPFORE:
                return s[:2], s[2:];
            elif len(s) == 2 and (s[:2] == TEL_CMD_SB or s[:2] in TELS_OPFORE):
                return b'', s;
            elif len(s) >= 3 and s[:2] in TELS_OPFORE:
                return s[:3], s[3:];
            elif len(s) >= 5 and s[:2] == TEL_CMD_SB:
                _l = TELS_SUBOPLEN[s[:3]] if (s[:3] in TELS_SUBOPLEN) else -1;
                if _l != -1 and len(s) < _l:
                    return b'', s;
                elif _l != -1 and len(s) >= _l and s[_l - 2 : _l] != TEL_CMD_SE:
                    return b'', s;
                elif _l != -1 and len(s) >= _l and s[_l - 2 : _l] == TEL_CMD_SE:
                    return s[:_l], s[_l:];
                elif _l == -1:
                    _i = 3;
                    while _i + 2 <= len(s) and s[_i : _i + 2] != TEL_CMD_SE:
                        _i += 1;
                    if _i + 2 <= len(s):
                        return s[:_i+2], s[_i+2:];
                    else:
                        return b'', s;
        elif s[:1] == bCHR_ESC:
            if len(s) == 1:
                return b'', s;
            elif len(s) > 1 and s[1:2] not in bCHRS_ESC_END:
                return s[:1], s[1:];
            elif len(s) > 1 and s[1:2] in bCHRS_ESC_END and s[:2] != bCHR_CSI_START:
                return s[:2], s[2:];
            elif len(s) > 1 and s[1:2] in bCHRS_ESC_END and s[:2] == bCHR_CSI_START:
                _i = 2;
                while _i + 1 <= len(s) and s[_i:_i+1] not in bCHRS_CSI_END:
                    _i += 1;
                if _i + 1 <= len(s):
                    return s[:_i+1], s[_i+1:];
                else:
                    return b'', s;
        elif s[:1] in bCHRS_RETURN:
            if len(s) == 1:
                return b'', s;
            elif len(s) > 1 and s[:2] == bCHR_CRLF:
                return s[:2], s[2:];
            elif len(s) > 1 and s[:2] == bCHR_CRNUL:
                return s[:2], s[2:];
            elif len(s) > 1 and s[:2] != bCHR_CRLF and s[:2] != bCHR_CRNUL:
                return s[:1], s[1:];
        else:
            _i = 1;
            while _i+1 <= len(s) and s[_i:_i+1] not in (TEL_IAC, bCHR_ESC, *bCHRS_RETURN):
                _i += 1;
            return s[:_i], s[_i:];
        return;

    def _option(self, s:bytes) -> bytes:
        if len(s) >= 3:
            if s[:2] == TEL_CMD_WILL:
                if s[2:3] in self.status and (self.status[s[2:3]] & self.DQUERYING):
                    self.status[s[2:3]] |= self.DO;
                    self.status[s[2:3]] &= ~ self.DONT;
                    self.status[s[2:3]] &= ~ self.DQUERYING;
                elif s[2:3] in self.SUPPORTED:
                    self.status[s[2:3]] |= self.DO;
                    self.status[s[2:3]] &= ~ self.DONT;
                    self.status[s[2:3]] &= ~ self.DQUERYING;
                    return TEL_CMD_DO + s[2:3];
                else:
                    self.status[s[2:3]] &= ~ self.DO;
                    self.status[s[2:3]] |= self.DONT;
                    self.status[s[2:3]] &= ~ self.DQUERYING;
                    return TEL_CMD_DONT + s[2:3];
            elif s[:2] == TEL_CMD_WONT:
                if s[2:3] in self.status and (self.status[s[2:3]] & self.DQUERYING):
                    self.status[s[2:3]] &= ~ self.DO;
                    self.status[s[2:3]] |= self.DONT;
                    self.status[s[2:3]] &= ~ self.DQUERYING;
                else:
                    self.status[s[2:3]] &= ~ self.DO;
                    self.status[s[2:3]] |= self.DONT;
                    self.status[s[2:3]] &= ~ self.DQUERYING;
                    return TEL_CMD_DONT + s[2:3];
            elif s[:2] == TEL_CMD_DO:
                if s[2:3] in self.status and (self.status[s[2:3]] & self.WQUERYING):
                    self.status[s[2:3]] |= self.WILL;
                    self.status[s[2:3]] &= ~ self.WONT;
                    self.status[s[2:3]] &= ~ self.WQUERYING;
                elif s[2:3] in self.SUPPORTED:
                    self.status[s[2:3]] |= self.WILL;
                    self.status[s[2:3]] &= ~ self.WONT;
                    self.status[s[2:3]] &= ~ self.WQUERYING;
                    return TEL_CMD_WILL + s[2:3];
                else:
                    self.status[s[2:3]] &= ~ self.WILL;
                    self.status[s[2:3]] |= self.WONT;
                    self.status[s[2:3]] &= ~ self.WQUERYING;
                    return TEL_CMD_WONT + s[2:3];
            elif s[:2] == TEL_CMD_DONT:
                if s[2:3] in self.status and (self.status[s[2:3]] & self.WQUERYING):
                    self.status[s[2:3]] &= ~ self.WILL;
                    self.status[s[2:3]] |= self.WONT;
                    self.status[s[2:3]] &= ~ self.WQUERYING;
                else:
                    self.status[s[2:3]] &= ~ self.WILL;
                    self.status[s[2:3]] |= self.WONT;
                    self.status[s[2:3]] &= ~ self.WQUERYING;
                    return TEL_CMD_WONT + s[2:3];
        return b'';
    
    def _sbttype(self, s:bytes) -> bytes:
        if len(s) >= 5:
            if s == TELf_SB(TEL_OP_TTYP, TEL_OP_TTYP_SEND):
                return TELf_SB(TEL_OP_TTYP, TEL_OP_TTYP_IS, self.TYPE);
            elif s[:4] == TEL_CMD_SB + TEL_OP_TTYP + TEL_OP_TTYP_IS and s[-2:] == TEL_CMD_SE:
                self._opst_ttyp_terminaltype = s[4:-2].decode(self.code, 'ignore');
        return b'';

    def _sbnaws(self, s:bytes) -> bytes:
        if len(s) == 9:
            w1, w0, h1, h0 = s[3], s[4], s[5], s[6];
            w = w1 * 256 + w0;
            h = h1 * 256 + h0;
            self._opst_naws_windowsize = (w, h);
        return b'';

    @property
    def autoecho(self) -> bool:
        return self._opst_echo_autoecho;
    
    @autoecho.setter
    def autoecho(self, val:bool) -> None:
        self._opst_echo_autoecho = val;

    @property
    def autoga(self) -> bool:
        return self._opst_sprga_autoga;
    
    @autoga.setter
    def autoga(self, val:bool) -> None:
        self._opst_sprga_autoga = val;

    @property
    def windowsize(self) -> tuple:
        return self._opst_naws_windowsize;
    
    @property
    def terminaltype(self) -> str:
        return self._opst_ttyp_terminaltype;

    @property
    def querying(self) -> bool:
        _q = False;
        for key in self.status:
            _q = _q or (self.status[key] & self.WQUERYING) or (self.status[key] & self.DQUERYING);
        return _q;

    def optionquery(self, options:dict, force:bool = False) -> None:
        _s = b'';
        for key in options:
            if (
                (key in self.SUPPORTED) and
                (options[key] & self.WILL) and
                not (key in self.status and self.status[key] & self.WILL) and
                not (key in self.status and self.status[key] & self.WQUERYING)
            ):
                _s += TEL_CMD_WILL + key;
                self.status[key] = (self.status[key] | self.WQUERYING) if (key in self.status) else self.WQUERYING;
            elif (options[key] & self.WILL) and force:
                _s += TEL_CMD_WILL + key;
                self.status[key] = (self.status[key] | self.WQUERYING) if (key in self.status) else self.WQUERYING;
            elif (options[key] & self.WONT) and force:
                _s += TEL_CMD_WONT + key;
                self.status[key] = (self.status[key] | self.WQUERYING) if (key in self.status) else self.WQUERYING;
            if (
                (key in self.SUPPORTED) and
                (options[key] & self.DO) and
                not (key in self.status and self.status[key] & self.DO) and
                not (key in self.status and self.status[key] & self.DQUERYING)
            ):
                _s += TEL_CMD_DO + key;
                self.status[key] = (self.status[key] | self.DQUERYING) if (key in self.status) else self.DQUERYING;
            elif (options[key] & self.DO) and force:
                _s += TEL_CMD_DO + key;
                self.status[key] = (self.status[key] | self.DQUERYING) if (key in self.status) else self.DQUERYING;
            elif (options[key] & self.DONT) and force:
                _s += TEL_CMD_DONT + key;
                self.status[key] = (self.status[key] | self.DQUERYING) if (key in self.status) else self.DQUERYING;
            if key == TEL_OP_TTYP and options[key] & self.DO:
                _s += TEL_CMD_SB + TEL_OP_TTYP + TEL_OP_TTYP_SEND + TEL_CMD_SE;
        self.conn.send(_s);
        return;
    
    def recvpush(self, r:bytes) -> None:
        self._recvbuff += r;
        _rs = [];
        _r = bCHR_NUL;
        while _r:
            _r, self._recvbuff = self._deal(self._recvbuff);
            _rs.append(_r);
        _s = b'';
        if not self._opst_sprga_dosprga and self._opst_sprga_autoga:
            _s += TEL_CMD_GA;
        for _i in range(len(_rs)):
            _r = _rs[_i];
            if _r[:2] in TELS_OPFORE:
                _s += self._option(_r);
            elif _r[:3] == TEL_CMD_SB + TEL_OP_TTYP:
                _s += self._sbttype(_r);
            elif _r[:3] == TEL_CMD_SB + TEL_OP_NAWS:
                _s += self._sbnaws(_r);
            elif _r[:1] == TEL_IAC:
                pass;
            elif _i == len(_rs) - 1 and self._recvbuff == b'':
                try:
                    _rd = _r.decode(self.code);
                except UnicodeDecodeError as err:
                    _rd = _r.decode(self.code);
                    self._recvbuff = self._r;
                self._recvqueue.append(_rd);
                if self._opst_echo_willecho and self._opst_echo_autoecho:
                    _s += _rd.encode(self.code);
            else:
                _rd = _r.decode(self.code, 'ignore');
                self._recvqueue.append(_rd);
                if self._opst_echo_willecho and self._opst_echo_autoecho:
                    _s += _rd.encode(self.code);
        if _s:
            self.conn.send(_s);
        return;
    
    def recvpop(self) -> str:
        if not self._recvqueue:
            _pop = self._recvqueue[0];
            self._recvqueue = self._recvqueue[1:];
            return _pop;
        else:
            return None;
    
    def recvpops(self) -> str:
        while self._recvqueue:
            _pop = self._recvqueue[0];
            self._recvqueue = self._recvqueue[1:];
            yield _pop;
        return;
    
    def send(self, s:str) -> None:
        _s = s.encode(self.code, 'ignore');
        self.conn.send(_s);
        return;
