
# -*- coding: UTF-8 -*-

# 实现单个用户访问的Shell的类；

# 模块内应当实现一个或多个实现对用户访问的整体管理的类，处理前端进入的操作流，
# 调用后端页面信息和资源加载功能响应用户操作，返回用于绘制的字符串流；
# 实现内容如，配置连接，实例化前后级，指示前级协商，根据前级协商内容响应用户的操作，
# 根据用户操作记录、控制用户访问的Res、焦点信息，将用户操作转发于Res，
# 根据更新，调用Res的绘制，缓存未更新的绘制内容，将绘制流通过前端发送；
# 又如，通过前端接口，根据特定的用户Telnet连接的属性，使用命令模式接受用户访问，
# 接受用户访问请求，返回元素信息，由用户自行绘制；

import time;
import threading;
import subprocess;
import traceback;
import socket;

from typing import *;

from .. import CLI;

from . import TELFront;

from ..OLDLog import logger;
from .CONSTS import *;

__all__ = [
    "Shell",
    "EchoShell",
    "CasterShell"
];



# Shell(conn, [logger], [name], [maxidle], [...])
# 单个用户的标准TEL型shell控制线程，实例化Res类作为交互对象；
#   conn        : socket                                // 该用户的socket连接；
#   logger      : logger                                // 该用户的日志实例；
#   name        : str                                   // 该用户的线程名称；
#   maxidle     : float                                 // 该用户的最大空闲，超时下线；
#   maxhistory  : int                                   // 该用户的最大历史深度；
#   telfront    : class(Front)                          // 用于控制输入处理的类；
#   resload     : class(ResLoad)                        // 用于控制资源加载的类；
#   frontpage   : res                                   // 首页的资源标识符res；

class Shell(threading.Thread):

    def __init__(
        self,
        conn,
        logger      = logger,
        name        = '',
        maxidle     = 900,
        maxhistory  = 8,
        telfront    = TELFront.Front,
        tfparam     = {
            'code'      : 'ascii',
            'autoecho'  : False,
            'autoga'    : False,
        },
        resload     = CLI.ResLoad,
        rlparam     = {},
        frontpage   = 'res::front',
    ) -> None:
        super().__init__();
        self.conn = conn;
        self.logger = logger;
        self.name = name if name else hex(id(self));
        self.maxidle = maxidle;
        self.maxhistory = maxhistory;
        self.tf = telfront(conn = conn, logger = logger, **tfparam);
        self.rl = resload(**rlparam);
        self.res = self.rl.getres(res = frontpage);
        self.history = [frontpage];
        self.timestamp = time.time();
        self._flagstop = False;
        return;
    
    def stop(self) -> None:
        self._flagstop = True;
        return;
    
    def draw(self) -> str:
        return '';

    def run(self) -> None:
        self.logger.info('User [%s] running...' % self.name);
        try:
            self.tf.optionquery(
                options = {
                    self.tf.OP_ECHO     : self.tf.WILL | self.tf.DONT,
                    self.tf.OP_SPRGA    : self.tf.WILL | self.tf.DO,
                    self.tf.OP_NAWS     : self.tf.DO,
                    self.tf.OP_LNMOD    : self.tf.DONT,
                },
                force = True
            );
            recv = bCHR_NUL;
            while time.time() - self.timestamp <= self.maxidle and recv != bCHR_NONE and not self._flagstop:
                try:
                    recv = self.conn.recv(4096);
                except (BlockingIOError, TimeoutError):
                    recv = None;
                if recv:
                    self.tf.recvpush(recv);
                    for input in self.tf.recvpops():
                        pass;
                try:
                    send = self.draw();
                except Exception as err:
                    send = None;
                    self.logger.error('User [%s] draw failed.' % self.name);
                    self.logger.error(err);
                    self.logger.debug(traceback.format_exc());
                if send:
                    self.tf.send(send);
            self.conn.shutdown(socket.SHUT_RDWR);
            time.sleep(2);
        except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError) as err:
            self.conn.close();
            self.logger.info('User [%s] connection aborted.' % self.name);
        except Exception as err:
            self.conn.close();
            self.logger.critical('User [%s] shell failed.' % self.name);
            self.logger.error(err);
            self.logger.debug(traceback.format_exc());
        self.logger.info('User [%s] ended.' % self.name);
        return;



# EchoShell(conn, [logger], [name], [timeout])
# 单个用户的Echo型shell控制线程，
# 将用户输入投射至返回；
#   conn        : socket                                // 该用户的socket连接；
#   logger      : logger                                // 该用户的日志实例；
#   name        : str                                   // 该用户的线程名称；
#   prt         : bool                                  // 该用户的键入是否记录log；
#   timeout     : float                                 // 该用户的最长保持时间；

class EchoShell(threading.Thread):

    def __init__(self, conn, logger = logger, name = '', prt = False, timeout = 300) -> None:
        super().__init__();
        self.conn = conn;
        self.logger = logger;
        self.name = name if name else hex(id(self));
        self.prt = prt;
        self.timeout = timeout;
        self.timestart = time.time();
        self._flagstop = False;
        return;

    def stop(self) -> None:
        self._flagstop = True;
    
    def run(self) -> None:
        self.logger.info('User [%s] running...' % self.name);
        try:
            r = bCHR_NUL;
            while (self.timeout < 0 or time.time() - self.timestart <= self.timeout) and r != b'' and not self._flagstop:
                try:
                    r = self.conn.recv(4096);
                except (BlockingIOError, TimeoutError):
                    r = None;
                if r:
                    self.conn.send(r);
                    if self.prt:
                        self.logger.info('User [%s] input <%s>, utf-8 : <%s>' % (self.name, str(r), r.decode('utf-8')));
            self.conn.shutdown(socket.SHUT_RDWR);
            time.sleep(2);
        except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError) as err:
            self.conn.close();
            self.logger.info('User [%s] connection aborted.' % self.name);
        except Exception as err:
            self.conn.close();
            self.logger.critical('User [%s] shell failed.');
            self.logger.error(err);
            self.logger.debug(traceback.format_exc());
        self.logger.info('User [%s] ended.' % self.name);
        return;



# CasterShell(conn, [logger], [name], [shell], [timeout])
# 单个用户的Caster型shell控制线程，使用外置的shell的进程，
# 将shell进程的标准输出投射至返回，实时主动更新；
#   conn        : socket                                // 该用户的socket连接；
#   logger      : logger                                // 该用户的日志实例；
#   name        : str                                   // 该用户的线程名称；
#   shell       : str                                   // 该用户的shell程序；
#   timeout     : float                                 // 该用户的最长保持时间；

class CasterShell(threading.Thread):

    def __init__(self, conn, logger = logger, name = '', shell = '', timeout = 300) -> None:
        super().__init__();
        self.conn = conn;
        self.logger = logger;
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
        self.logger.info('User [%s] running...' % self.name);
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
            self.logger.critical('User [%s] shell failed starting.');
            self.logger.error(err);
            self.logger.debug(traceback.format_exc());
            return;
        try:
            s = bCHR_NUL;
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
            self.logger.info('User [%s] connection aborted.' % self.name);
        except Exception as err:
            self.conn.close();
            self.pipe.close();
            self.proc.kill();
            self.logger.critical('User [%s] shell failed.');
            self.logger.error(err);
            self.logger.debug(traceback.format_exc());
        self.logger.info('User [%s] ended.' % self.name);
        return;
