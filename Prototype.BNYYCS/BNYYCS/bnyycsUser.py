
# -*- coding: UTF-8 -*-

from . import bnyycsRes as Res;

from .bnyycsLog import logger;
from .bnyycsCtrl import *;

__all__ = [
    "User",
    "User_BNYYCS",
    "User_BNYYCS_Light"
];



# User(**params)
# 用户控制的基类，不在本类实现用户控制的具体形式，只定义公共接口；
# params是Shell当前的环境参数；
# .tab          : int                                   // 该用户的焦点tab顺序，只读；
# .cmds         : [bytes]                               // 该用户的待选指令，可写，由Shell传入，
#                                                       // 为字符串类型的数组，每个元素为一条指令；
# .draw(res, **params)                                  // 该用户的一次绘制，res为绘制时的统一资源标识符，
#               : bytes                                 // 一个标准的user的draw应当返回一个可以实现画面绘制的bytes序列，
#                                                       // 绘制的控制序列应当遵循常用的，如VT100的控制协议，和80x24的尺寸，
#                                                       // 一个res应当只绘制屏幕下部80x4的区域，并余下(80,24)字符不绘制，
#                                                       // 限制范围因为Shell中可能会调用Res在上方80x20绘制画面，
#                                                       // 保留字符是为了避免绘制(80,24)字符后可能的换行导致内容推出屏幕，
#                                                       // 绘制的过程应当使用相对坐标，绘制前光标置于(1,21)，即下80x4区域的第一个字符位；
# .update(inps:[bytes], **params)                       // 向资源发送一次接受，params是Shell当前的环境参数，
#               : bytes                                 // 返回update表示交由Shell执行一条指令；
class User:

    def __init__(self, **params) -> None:
        self._tab = -1;
        self._cmd = '';
        self._cmds = [];
        self._params = params;
        return;
    
    @property
    def tab(self):
        return self._tab;
    
    @tab.setter
    def tab(self, val):
        assert val == -1;
        self._tab = -1;
        return;

    @property
    def cmds(self):
        return self._cmds;
    
    @cmds.setter
    def cmds(self, value):
        assert type(value) == list;
        for elm in value:
            assert type(elm) == bytes;
        self._cmds = value;
        return;

    def draw(self, res, **params):
        self._params.update(params);
        return b'';

    def update(self, inps = [], **params):
        self._params.update(params);
        for inp in inps:
            ...;
            # do sth to inps;
        return None;



# User_BNYYCS(**params)
# 用户控制的BNYYCS类，实现一个具有基本交互功能的类，params是Shell当前的环境参数；
# .tab          : int                                   // 该用户的焦点tab顺序，只读，
#                                                       // 与cmds列表对应，指定-1表示无焦点；
# .cmds         : [bytes]                               // 该用户的待选指令，可写，由Shell传入，
#                                                       // 为字符串类型的数组，每个元素为一条指令，
#                                                       // 在用户使用↑↓键时根据当前tab顺序辅助输入对应cmds，
#                                                       // 在用户使用Tab键时根据当前已输入指令执行辅助输入补全，或cmds下一，或不操作；
# .draw(res, **params)                                  // 该用户的一次绘制，res为绘制时的统一资源标识符，params是Shell当前的环境参数，
#               : bytes                                 // 在画面下方提供一个单行输入位置；
# .update(inps:[bytes], **params)                       // 向资源发送一次接受，params是Shell当前的环境参数，
#               : bytes                                 // 返回update表示交由Shell执行一条指令；
class User_BNYYCS(User):

    def __init__(self, **params) -> None:
        self._tab = -1;
        self._cmds = [];
        self._cmd = b'';
        self._params = params;
        return;
    
    def draw(self, res, **params):
        self._params.update(params);
        _scmd = self._cmd.split(maxsplit = 1);
        _cmd = (_scmd[0] + b' ') if len(_scmd) >= 1 else b'';
        _para = (_scmd[1] if len(_cmd) <= 76 else _scmd[1][76 - len(_scmd[0]) - 5] + b'...') if len(_scmd) >= 2 else b'';
        _rspace = b'%*s' % ((76 - len(_cmd + _para)), b'');
        _ret = (
            CHR_T_FC_YELLO + b' >> ' +
            CHR_T_FC_RED + _cmd +
            CHR_T_FC_BLUE + _para + _rspace +
            CHR_T_RST
        );
        return _ret
    
    def cmdmatch(self, cmd):
        if cmd == b'':
            return self._tab;
        else:
            for _match in range(len(self.cmds)):
                if cmd == self.cmds[_match][:len(cmd)]:
                    return _match;
            return -1;

    def dotab(self):
        _match = self.cmdmatch(self._cmd);
        if _match == -1:
            pass;
        elif _match != -1 and _match != self._tab:
            self._tab = _match;
        elif _match != -1 and _match == self._tab and self.cmds[_match] != self._cmd:
            if self._tab >= 0 and self._tab < len(self.cmds):
                self._cmd = self.cmds[self._tab];
        elif _match != -1 and _match == self._tab and self.cmds[_match] == self._cmd:
            self._tab = (self._tab + 2) % (len(self.cmds) + 1) - 1;
            if self._tab >= 0 and self._tab < len(self.cmds):
                self._cmd = self.cmds[self._tab];
        else:
            self._cmd = self.cmds[_match];
        return;
    
    def doup(self):
        self._tab = (self._tab) % (len(self.cmds) + 1) - 1;
        if self._tab >= 0 and self._tab < len(self.cmds):
            self._cmd = self.cmds[self._tab];
        return;
    
    def dodown(self):
        self._tab = (self._tab + 2) % (len(self.cmds) + 1) - 1;
        if self._tab >= 0 and self._tab < len(self.cmds):
            self._cmd = self.cmds[self._tab];
        return;
    
    def doright(self):
        self._cmd = b'next';
        return;
    
    def doleft(self):
        self._cmd = b'back';
        return;
    
    def dohome(self):
        self._tab = 0;
        if self._tab >= 0 and self._tab < len(self.cmds):
            self._cmd = self.cmds[self._tab];
        return;
    
    def doend(self):
        self._tab = len(self.cmds) - 1;
        if self._tab >= 0 and self._tab < len(self.cmds):
            self._cmd = self.cmds[self._tab];
        return;

    def doesc(self):
        self._tab = -1;
        return;
    
    def dodel(self):
        self._cmd = self._cmd[:-1];
        return;
    
    def dotype(self, chr):
        self._cmd = self._cmd + chr;
        return;

    def update(self, inps = [], **params):
        self._params.update(params);
        for inp in inps:
            if inp == CHR_KEY_TAB:
                self.dotab();
            elif inp == CHR_KEY_UP:
                self.doup();
            elif inp == CHR_KEY_DOWN:
                self.dodown();
            elif inp == CHR_KEY_RIGHT:
                self.doright();
            elif inp == CHR_KEY_LEFT:
                self.doleft();
            elif inp == CHR_KEY_BS or inp == CHR_KEY_DEL:
                self.dodel();
            elif inp == CHR_KEY_HOME:
                self.dohome();
            elif inp == CHR_KEY_END:
                self.doend();
            elif inp == CHR_KEY_ESC:
                self.doesc();
            elif inp in CHRS_PRINT + CHRS_EXT:
                self.dotype(inp);
            elif inp in CHRS_RETURN:
                _ret = self._cmd;
                self._cmd = b'';
                return _ret;
        return None;



# User_BNYYCS_Light(**params)
# 用户控制的BNYYCS_Light类，实现一个具有基本交互功能的类，只有对用户上下键切换焦点逻辑的响应
# params是Shell当前的环境参数；
# .tab          : int                                   // 该用户的焦点tab顺序，只读，
#                                                       // 与cmds列表对应，指定-1表示无焦点；
# .cmds         : [bytes]                               // 该用户的待选指令，可写，由Shell传入，
#                                                       // 为字符串类型的数组，每个元素为一条指令，
#                                                       // 在用户使用↑↓键时根据当前tab顺序辅助输入对应cmds，
#                                                       // 在用户使用Tab键时根据当前已输入指令执行辅助输入补全，或cmds下一，或不操作；
# .draw(res, **params)                                  // 该用户的一次绘制，res为绘制时的统一资源标识符，params是Shell当前的环境参数，
#               : bytes                                 // 在画面下方提供一个单行输入位置；
# .update(inps:[bytes], **params)                       // 向资源发送一次接受，params是Shell当前的环境参数，
#               : bytes                                 // 返回update表示交由Shell执行一条指令；
class User_BNYYCS_Light(User):

    def __init__(self, **params) -> None:
        self._tab = -1;
        self._cmds = [];
        return;
    
    def draw(self, res, **params):
        return b'';
    
    def doup(self):
        self._tab = (self._tab) % (len(self.cmds) + 1) - 1;
        return;
    
    def dodown(self):
        self._tab = (self._tab + 2) % (len(self.cmds) + 1) - 1;
        return;
    
    def doesc(self):
        self._tab = -1;
        return;
    
    def update(self, inps = [], **params):
        for inp in inps:
            if inp == CHR_KEY_UP:
                self.doup();
            elif inp == CHR_KEY_DOWN:
                self.dodown();
            elif inp == CHR_KEY_ESC:
                self.doesc();
            elif inp in CHRS_RETURN:
                if self._tab >= 0 and self._tab < len(self._cmds):
                    return self._cmds[self._tab];
                else:
                    self._tab = -1;
        return None;