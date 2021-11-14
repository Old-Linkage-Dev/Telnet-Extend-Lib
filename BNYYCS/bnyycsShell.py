
# -*- coding: UTF-8 -*-

import time;
import threading;
import subprocess;
import traceback;
import socket;

from . import bnyycsUser as User;
from . import bnyycsRes as Res;

from .bnyycsLog import logger;



# Shell_BNYYCS(conn, [name], [maxidle])             // 单个用户的标准BNYYCS型shell控制线程，使用User类的update进行交互，接受用户操作后将User类的page和line返回，User类不能主动更新；
#   conn        : socket                            // 该用户的socket连接；
#   name        : str                               // 该用户的线程名称；
#   maxidle     : float                             // 该用户的最大空闲，超时下线；

class Shell_BNYYCE(threading.Thread):

    def __init__(self, conn, name = '', maxidle = 900) -> None:
        super().__init__();
        self.conn = conn;
        self.name = name if name else hex(id(self));
        self.maxidle = maxidle;
        self.user = User.User();
        self.timestamp = time.time();
        self._stop = False;
        return;
    
    def stop(self) -> None:
        self._stop = True;
    
    def run(self) -> None:
        logger.info('User [%s] running...' % self.name);
        try:
            while time.time() - self.timestamp <= self.maxidle and not self._stop:
                try:
                    recv = self.conn.recv();
                except BlockingIOError or TimeoutError:
                    recv = None;
                update = self.user.update(recv) if recv else None;
                self.conn.send(self.user.page);
                self.conn.send(self.user.line);
                if update:
                    self.timestamp = time.time();
                    logger.info('User [%s] updated "%s"' % (self.name, update));
                if update == 'quit':
                    break;
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
            logger.critical('User [%s] shell failed.' % self.name);
        return;



# Shell_Caster(conn, [name], [shell])               // 单个用户的Caster型shell控制线程，使用外置的shell的进程，将shell进程的标准输出投射至返回，实时主动更新；
#   conn        : socket                            // 该用户的socket连接；
#   name        : str                               // 该用户的线程名称；
#   shell       : str                               // 该用户的shell程序；
#   timeout     : float                             // 该用户的最长保持时间；

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
        self._stop = False;
        return;

    def stop(self) -> None:
        self._stop = True;
    
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
            s = b'\x00';
            while (self.timeout < 0 or time.time() - self.timestart <= self.timeout) and self.proc.poll() == None and s != b'' and not self._stop:
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
