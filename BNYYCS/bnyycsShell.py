
# -*- coding: UTF-8 -*-

import time;
import math;
import threading;
import subprocess;
import traceback;
import socket;

from . import bnyycsUser as User;
from . import bnyycsRes as Res;

from .bnyycsLog import logger;
from .bnyycsRes import splitres;
from .bnyycsCtrl import *;

__all__ = [
    "splitcmd",
    "Shell_BNYYCS",
    "Shell_Refuse",
    "Shell_Echo",
    "Shell_Interactor",
    "Shell_Caster"
];

# splitcmd(cmd:update) : (cmd, args)
# 用于拆分一个update的cmd，为cmd和args；
def splitcmd(cmd):
    if type(cmd) == bytes:
        _cmds = cmd.split();
        assert type(_cmds[0]) == bytes;
        return _cmds[0], _cmds[1:];
    elif type(cmd) in (list, tuple):
        return cmd[0], cmd[1:];
    return;





# Shell_BNYYCS(conn, [name], [maxidle])
# 单个用户的标准BNYYCS型shell控制线程，使用User类的update进行交互，
# 接受用户操作后将User类的page和line返回，User类不能主动更新；
#   conn        : socket                                // 该用户的socket连接；
#   name        : str                                   // 该用户的线程名称；
#   maxidle     : float                                 // 该用户的最大空闲，超时下线；
#   maxhistory  : int                                   // 该用户的最大历史深度；
#   maxparams   : int                                   // 该用户的最大参数规模；
#   maxvalue    : int                                   // 该用户的最大单个参数规模；
#   resloader   : class(ResLoader)                      // 用于控制资源加载的类；
#   inputqueue  : class(InputQueue)                     // 用于控制输入处理的类，功能较完备，不建议修改；
#   usercontrol : class(User)                           // 用于用户控制界面的类，可通过定制实现其他控制功能逻辑；
#   frontpage   : res                                   // 首页的资源标识符res；
#   shellparams : dict                                  // Shell提供的初始参数列表；

class Shell_BNYYCS(threading.Thread):

    def __init__(
        self,
        conn,
        name        = '',
        maxidle     = 900,
        maxhistory  = 8,
        maxparams   = 64,
        maxvalue    = 256,
        resloader   = Res.ResLoader_BNYYCS,
        inputqueue  = TelnetInputQueue,
        usercontrol = User.User_BNYYCS,
        frontpage   = 'res::front',
        shellparams = {},
    ) -> None:
        super().__init__();
        self.conn = conn;
        self.name = name if name else hex(id(self));
        self.maxidle = maxidle;
        self.maxhistory = maxhistory;
        self.maxparams = maxparams;
        self.maxvalue = maxvalue;
        self.rl = resloader();
        self.iq = inputqueue();
        self.params = shellparams;
        self.user = usercontrol(params = self.params);
        self.res = self.rl.getres(res = frontpage, params = self.params);
        self.history = [self.res.res];
        self.timestamp = time.time();
        self._flagstop = False;
        return;
    
    def stop(self) -> None:
        self._flagstop = True;
        return;
    


    # 网站顶级指令集合

    # 退出网站
    def cmdquit(self, *args):
        self.stop();
        return;

    # 访问历史记录的上一条资源
    def cmdback(self, *args):
        if len(self.history) > 1:
            self.res = self.rl.getres(self.history[-2]);
            self.history = self.history[:-1];
            self.user.cmds = self.res.cmds;
        return;
    
    # 访问当前资源逻辑上的下一条资源
    def cmdnext(self, *args):
        _res = self.rl.nextres(self.res.res);
        self.res = self.rl.getres(res = _res, params = self.params);
        self.history.append(self.res.res);
        if len(self.history) > self.maxhistory:
            self.history = self.history[1:];
        return;

    # 访问承载帮助信息的资源
    def cmdhelp(self, *args):
        _respath = b'help';
        for arg in args:
            if type(arg) == bytes:
                _respath += b'/' + arg;
        _res = b'res:' + _respath + b':help';
        self.res = self.rl.getres(res = _res, params = self.params);
        self.history.append(self.res.res);
        if len(self.history) > self.maxhistory:
            self.history = self.history[1:];
        return;
    
    # 访问一条res指向的资源
    def cmdvisit(self, *args):
        if len(args) >= 1 and type(args[0]) == bytes:
            _s = splitres(args[0]);
            if len(_s) >= 3 and _s[0] == b'res':
                _res = args[0];
                self.res = self.rl.getres(res = _res, params = self.params);
                self.history.append(self.res.res);
            elif len(_s) >= 2:
                _res = b'res:' + args[0];
                self.res = self.rl.getres(res = _res, params = self.params);
                self.history.append(self.res.res);
        if len(self.history) > self.maxhistory:
            self.history = self.history[1:];
        return;
    
    # 未设计功能
    def cmdget(self, *args):
        return;
    
    # 设置Shell的params
    def cmdset(self, *args):
        try:
            for _i in range(math.floor(len(args) / 2)):
                if args[_i] in self.params or len(self.params) < self.maxparams:
                    self.params[args[_i]] = args[_i + 1] if len(args[_i + 1]) <= self.maxvalue else None;
        except Exception as err:
            logger.error(err);
            logger.error('User [%s] set failed.' % self.name);
            logger.debug(traceback.format_exc());
        return;
    
    # 未设计功能
    def cmdput(self, *args):
        return;



    def cmd(self, command):
        _cmd, _args = splitcmd(command);
        if _cmd == b'quit':
            self.stop(*_args);
        elif _cmd == b'back':
            self.cmdback(*_args);
        elif _cmd == b'next':
            self.cmdnext(*_args);
        elif _cmd == b'help':
            self.cmdhelp(*_args);
        elif _cmd == b'visit':
            self.cmdvisit(*_args);
        elif _cmd == b'get':
            self.cmdget(*_args);
        elif _cmd == b'set':
            self.cmdset(*_args);
        elif _cmd == b'put':
            self.cmdput(*_args);
        else:
            try:
                self.res.run(command, self.params);
            except Exception as err:
                logger.error(err);
                logger.error('User [%s] res run failed.' % self.name);
                logger.debug(traceback.format_exc());
            self.user.cmds = self.res.cmds;
        return;

    def updateres(self, inps):
        try:
            update = self.res.update(inps = inps, params = self.params);
        except Exception as err:
            logger.error(err);
            logger.error('User [%s] res update failed.' % self.name);
            logger.debug(traceback.format_exc());
        if update:
            logger.info('User [%s] res updated "%s"' % (self.name, update));
            self.cmd(update);
        self.user.cmds = self.res.cmds;
        return;
    
    def updateuser(self, inps):
        self.user.cmds = self.res.cmds;
        try:
            update = self.user.update(inps = inps, params = self.params);
        except Exception as err:
            logger.error(err);
            logger.error('User [%s] update failed.' % self.name);
            logger.debug(traceback.format_exc());
        if update:
            self.timestamp = time.time();
            logger.info('User [%s] updated "%s"' % (self.name, update));
            self.cmd(update);
        return;
    
    def draw(self):
        _draw = (
            CHR_CLR +
            CHR_CSI_CUP + self.res.draw(tab = self.user.tab, params = self.params) + CHR_T_RST +
            CHRf_CSI_CUP(21, 1) + self.user.draw(res = self.res.res, params = self.params) + CHR_T_RST +
            CHRf_CSI_CUP(24, 80)
        );
        self.conn.send(_draw);
        return;
    
    def run(self) -> None:
        logger.info('User [%s] running...' % self.name);
        try:
            self.draw();
            recv = CHR_NUL;
            self.conn.send(
                TELf_WILL(TEL_OP_ECHO) +
                TELf_DONT(TEL_OP_ECHO) +
                TELf_WILL(TEL_OP_SPRGA) +
                TELf_DO(TEL_OP_NAWS) +
                TELf_DONT(TEL_OP_LNMOD)
            );
            while time.time() - self.timestamp <= self.maxidle and recv != b'' and not self._flagstop:
                try:
                    recv = self.conn.recv(4096);
                except BlockingIOError or TimeoutError:
                    recv = None;
                if recv:
                    self.iq.push(recv);
                    for chr in self.iq.pops():
                        #logger.debug('In : <%s>' % chr);
                        if chr[:1] == TEL_IAC and len(chr) == 1:
                            pass;
                        if chr[:1] == TEL_IAC and len(chr) >= 2 and chr[:2] != TEL_CMD_xFF:
                            # 由于目前请求都是由服务器发出的，这里我们放弃考虑客户端的请求情况
                            # 这可以避免对请求情况记录的复杂实现，若不进行复杂实现则可能触发回复的风暴
                            pass;
                        elif chr[:1] == TEL_IAC and len(chr) >= 2 and chr[:2] == TEL_CMD_xFF:
                            # 对于此处是否应该对两者进行同步更新是需要继续讨论的；
                            self.updateuser([TEL_xFF]);
                            self.updateres([TEL_xFF]);
                        else:
                            # 对于此处是否应该对两者进行同步更新是需要继续讨论的；
                            self.updateuser([chr]);
                            self.updateres([chr]);
                    self.draw();
            self.conn.shutdown(socket.SHUT_RDWR);
            time.sleep(2);
        except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError) as err:
            self.conn.close();
            logger.info('User [%s] connection aborted.' % self.name);
        except Exception as err:
            self.conn.close();
            logger.error(err);
            logger.critical('User [%s] shell failed.' % self.name);
            logger.debug(traceback.format_exc());
        logger.info('User [%s] ended.' % self.name);
        return;





# Shell_Refuse(conn, [name], [reason])
# 单个用户的标准Refuse型shell控制线程，向用户展示被拒绝访问的信息；
#                                                       // 该Shell应当是短暂快速轻量的处理信息，并且应当可被视作不具有时间上的开销的；
#   conn        : socket                                // 该用户的socket连接；
#   name        : str                                   // 该用户的线程名称；
#   reason      : str                                   // 该用户的拒绝理由；

class Shell_Refuse(threading.Thread):

    @property
    def _page(self):
        _reason = self.reason.encode(CHRSET_EXT);
        _reason = (_reason if len(_reason) <= 72 else _reason[:69] + b'...') if _reason else b'NO REASON PRESENTED';
        _lspace = b'%*s' % (math.ceil((72 - len(_reason)) / 2), b'');
        _rspace = b'%*s' % (math.floor((72 - len(_reason)) / 2), b'');
        return b''.join([
        CHR_CLR,
        b'#==============================================================================#' + CHR_CRLF,
        b'| CONNECTION INFORMATION                                                       |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'| The atempt to visit this site is refused,                                    |' + CHR_CRLF,
        b'| The reason to the rufusing is:                                               |' + CHR_CRLF,
        b'|   '                   + _lspace + _reason + _rspace +                   b'   |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'|                                                SUPPORTED BY PROTOTYPE BNYYCS |' + CHR_CRLF,
        b'#==============================================================================#' + CHR_CRLF,
        CHRf_CSI_CUP(8, 3)
        ]);
    
    def __init__(self, conn, name = '', reason = '') -> None:
        super().__init__();
        self.conn = conn;
        self.name = name if name else hex(id(self));
        self.reason = reason;
        return;
    
    def stop(self) -> None:
        return;
    
    def run(self) -> None:
        logger.info('User [%s] refusing...' % self.name);
        try:
            self.conn.send(self._page);
        except Exception as err:
            logger.error(err);
            logger.error('User [%s] refusing error.' % self.name);
            logger.debug(traceback.format_exc());
        self.conn.close();
        return;



# Shell_Echo(conn, [name], [timeout])
# 单个用户的Echo型shell控制线程，
# 将用户输入投射至返回；
#   conn        : socket                                // 该用户的socket连接；
#   name        : str                                   // 该用户的线程名称；
#   prt         : bool                                  // 该用户的键入是否记录log；
#   timeout     : float                                 // 该用户的最长保持时间；

class Shell_Echo(threading.Thread):

    def __init__(self, conn, name = '', prt = False, timeout = 300) -> None:
        super().__init__();
        self.conn = conn;
        self.name = name if name else hex(id(self));
        self.prt = prt;
        self.timeout = timeout;
        self.timestart = time.time();
        self._flagstop = False;
        return;

    def stop(self) -> None:
        self._flagstop = True;
    
    def run(self) -> None:
        logger.info('User [%s] running...' % self.name);
        try:
            r = CHR_NUL;
            while (self.timeout < 0 or time.time() - self.timestart <= self.timeout) and r != b'' and not self._flagstop:
                try:
                    r = self.conn.recv(4096);
                except BlockingIOError or TimeoutError:
                    r = None;
                if r:
                    self.conn.send(r);
                    if self.prt:
                        logger.info('User [%s] input <%s>, ansi : <%s>, utf-8 : <%s>' % (self.name, str(r), r.decode('ansi'), r.decode('utf-8')));
            self.conn.shutdown(socket.SHUT_RDWR);
            time.sleep(2);
        except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError) as err:
            self.conn.close();
            logger.info('User [%s] connection aborted.' % self.name);
        except Exception as err:
            self.conn.close();
            logger.error(err);
            logger.critical('User [%s] shell failed.');
            logger.debug(traceback.format_exc());
        logger.info('User [%s] ended.' % self.name);
        return;



# Shell_Interactor(conn, [name], [shell], [timeout])
# 单个用户的Interactor型shell控制线程，使用外置的shell的进程，
# 将用户输入投射至shell进程的标准输入，将shell进程的标准输出投射至返回，实时主动更新；
#   conn        : socket                                // 该用户的socket连接；
#   name        : str                                   // 该用户的线程名称；
#   shell       : str                                   // 该用户的shell程序；
#   timeout     : float                                 // 该用户的最长保持时间；

########################################################
# 功能有问题不能用，先不修了                             #
########################################################

class Shell_Interactor(threading.Thread):

    def __init__(self, conn, name = '', shell = '', timeout = 300) -> None:
        super().__init__();
        self.conn = conn;
        self.name = name if name else hex(id(self));
        self.shell = shell;
        self.timeout = timeout;
        self.timestart = time.time();
        self.proc = None;
        self.pipein = None;
        self.pipeout = None;
        self._subinput = None;
        self._flagstop = False;
        return;

    def stop(self) -> None:
        self._flagstop = True;
    
    def run(self) -> None:

        class subinput(threading.Thread):
            def run(subinput):
                try:
                    r = CHR_NUL;
                    while (self.timeout < 0 or time.time() - self.timestart <= self.timeout) and self.proc.poll() == None and r != b'' and not self._flagstop:
                        try:
                            r = self.conn.recv(4096);
                        except BlockingIOError or TimeoutError:
                            r = None;
                        if r:
                            self.pipein.write(r);
                    self.stop();
                except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError) as err:
                    self.stop();
                    self.conn.close();
                    self.pipein.close();
                    self.pipeout.close();
                    self.proc.kill();
                    logger.info('User subinput [%s] connection aborted.' % self.name);
                except Exception as err:
                    self.stop();
                    self.conn.close();
                    self.pipein.close();
                    self.pipeout.close();
                    self.proc.kill();
                    logger.error(err);
                    logger.critical('User subinput [%s] shell failed.');
                    logger.debug(traceback.format_exc());
                return;

        logger.info('User [%s] running...' % self.name);
        try:
            self.proc = subprocess.Popen(
                self.shell,
                stdin = subprocess.PIPE,
                stdout = subprocess.PIPE,
                stderr = subprocess.DEVNULL,
                shell=True
            );
            self.pipein = self.proc.stdin;
            self.pipeout = self.proc.stdout;
        except Exception as err:
            self.conn.close();
            self.proc = None;
            self.pipein = None;
            self.pipeout = None;
            logger.error(err);
            logger.critical('User [%s] shell failed starting.');
            logger.debug(traceback.format_exc());
            return;
        try:
            self._subinput = subinput(name = self.name + '_subinput');
            self._subinput.start();
            s = CHR_NUL;
            while (self.timeout < 0 or time.time() - self.timestart <= self.timeout) and self.proc.poll() == None and s != b'' and not self._flagstop:
                s = self.pipeout.read(1);
                self.conn.send(s);
            self.stop();
            self.conn.shutdown(socket.SHUT_RDWR);
            self.pipein.close();
            self.pipeout.close();
            self.proc.kill();
            self._subinput.join(timeout = 2);
            time.sleep(2);
        except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError) as err:
            self.stop();
            self.conn.close();
            self.pipein.close();
            self.pipeout.close();
            self.proc.kill();
            logger.info('User [%s] connection aborted.' % self.name);
        except TimeoutError as err:
            self.stop();
            self.conn.close();
            self.pipein.close();
            self.pipeout.close();
            self.proc.kill();
            logger.info('User [%s] shell quit timeout.' % self.name);
            logger.debug(traceback.format_exc());
        except Exception as err:
            self.stop();
            self.conn.close();
            self.pipein.close();
            self.pipeout.close();
            self.proc.kill();
            logger.error(err);
            logger.critical('User [%s] shell failed.');
            logger.debug(traceback.format_exc());
        logger.info('User [%s] ended.' % self.name);
        return;



# Shell_Caster(conn, [name], [shell], [timeout])
# 单个用户的Caster型shell控制线程，使用外置的shell的进程，
# 将shell进程的标准输出投射至返回，实时主动更新；
#   conn        : socket                                // 该用户的socket连接；
#   name        : str                                   // 该用户的线程名称；
#   shell       : str                                   // 该用户的shell程序；
#   timeout     : float                                 // 该用户的最长保持时间；

class Shell_Caster(threading.Thread):

    def __init__(self, conn, name = '', shell = '', timeout = 300) -> None:
        super().__init__();
        self.conn = conn;
        self.name = name if name else hex(id(self));
        self.shell = shell;
        self.timeout = timeout;
        self.timestart = time.time();
        self.proc = None;
        self.pipe = None;
        self._flagstop = False;
        return;

    def stop(self) -> None:
        self._flagstop = True;
    
    def run(self) -> None:
        logger.info('User [%s] running...' % self.name);
        try:
            self.proc = subprocess.Popen(
                self.shell,
                stdin = subprocess.DEVNULL,
                stdout = subprocess.PIPE,
                stderr = subprocess.DEVNULL,
                shell=True
            );
            self.pipe = self.proc.stdout;
        except Exception as err:
            self.conn.close();
            self.proc = None;
            self.pipe = None;
            logger.error(err);
            logger.critical('User [%s] shell failed starting.');
            logger.debug(traceback.format_exc());
            return;
        try:
            s = CHR_NUL;
            while (self.timeout < 0 or time.time() - self.timestart <= self.timeout) and self.proc.poll() == None and s != b'' and not self._flagstop:
                s = self.pipe.read(1);
                self.conn.send(s);
            self.conn.shutdown(socket.SHUT_RDWR);
            self.pipe.close();
            self.proc.kill();
            time.sleep(2);
        except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError) as err:
            self.conn.close();
            self.pipe.close();
            self.proc.kill();
            logger.info('User [%s] connection aborted.' % self.name);
        except Exception as err:
            self.conn.close();
            self.pipe.close();
            self.proc.kill();
            logger.error(err);
            logger.critical('User [%s] shell failed.');
            logger.debug(traceback.format_exc());
        logger.info('User [%s] ended.' % self.name);
        return;
