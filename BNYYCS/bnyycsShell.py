
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
from .bnyyceCtrl import *;

__all__ = [
    "Shell_BNYYCE",
    "Shell_Refuse",
    "Shell_Echo",
    "Shell_Interactor",
    "Shell_Caster"
];



# Shell_BNYYCS(conn, [name], [maxidle])
# 单个用户的标准BNYYCS型shell控制线程，使用User类的update进行交互，
# 接受用户操作后将User类的page和line返回，User类不能主动更新；
#   conn        : socket                                // 该用户的socket连接；
#   name        : str                                   // 该用户的线程名称；
#   maxidle     : float                                 // 该用户的最大空闲，超时下线；

class Shell_BNYYCE(threading.Thread):

    def __init__(self, conn, name = '', maxidle = 900) -> None:
        super().__init__();
        self.conn = conn;
        self.name = name if name else hex(id(self));
        self.maxidle = maxidle;
        self.user = User.User();
        self.res = Res.Res_RefusePage();
        self.kwargs = {};
        self.timestamp = time.time();
        self._flagstop = False;
        return;
    
    def stop(self) -> None:
        self._flagstop = True;
    
    def cmd(self, command):
        if command == 'quit':
            self.stop();
        elif command:
            self.res.run(command, **self.kwargs);

    def updateres(self, recv):
        update = self.res.update(recv, **self.kwargs);
        if update:
            logger.info('User [%s] res updated "%s"' % (self.name, update));
            self.cmd(update);
    
    def updateuser(self, recv):
        update = self.user.update(recv, **self.kwargs);
        if update:
            self.timestamp = time.time();
            logger.info('User [%s] updated "%s"' % (self.name, update));
            self.cmd(update);
    
    def run(self) -> None:
        logger.info('User [%s] running...' % self.name);
        try:
            self.conn.send(self.res.draw(self.user.tab));
            self.conn.send(self.user.draw());
            recv = CHR_NUL;
            while time.time() - self.timestamp <= self.maxidle and recv != b'' and not self._flagstop:
                try:
                    recv = self.conn.recv(4096);
                except BlockingIOError or TimeoutError:
                    recv = None;
                if recv:
                    self.updateuser(recv);
                    self.updateres(recv);
                    self.conn.send(self.res.draw(self.user.tab));
                    self.conn.send(self.user.draw(self.res.res, **self.kwargs));
            self.conn.shutdown(socket.SHUT_RDWR);
            time.sleep(2);
        except BrokenPipeError or ConnectionAbortedError or ConnectionResetError as err:
            self.conn.close();
            logger.info('User [%s] connection aborted.' % self.name);
        except Exception as err:
            self.conn.close();
            logger.error(err);
            logger.critical('User [%s] shell failed.' % self.name);
            logger.debug(traceback.format_exc());
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
        _reason = self.reason if len(self.reason) <= 72 else self.reason[:69] + '...' if self.reason else b'NO REASON PRESENTED';
        _lspace = b'%*s' % (math.ceil((72 - len(bytes(_reason, 'ascii'))) / 2), b'');
        _rspace = b'%*s' % (math.floor((72 - len(bytes(_reason, 'ascii'))) / 2), b'');
        _midwords = bytes(_reason, 'ascii');
        return b''.join([
        CHR_CLR,
        b'#==============================================================================#' + CHR_CRLF,
        b'| CONNECTION INFORMATION                                                       |' + CHR_CRLF,
        b'|                                                                              |' + CHR_CRLF,
        b'| The atempt to visit this site is refused,                                    |' + CHR_CRLF,
        b'| The reason to the rufusing is:                                               |' + CHR_CRLF,
        b'|   '                  + _lspace + _midwords + _rspace +                  b'   |' + CHR_CRLF,
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
        except BrokenPipeError or ConnectionAbortedError or ConnectionResetError as err:
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
                except BrokenPipeError or ConnectionAbortedError or ConnectionResetError as err:
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
        except BrokenPipeError or ConnectionAbortedError or ConnectionResetError as err:
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
        except BrokenPipeError or ConnectionAbortedError or ConnectionResetError as err:
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
