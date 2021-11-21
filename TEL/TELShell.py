
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

from .TELLog import logger;
from .CONSTS import *;

__all__ = [
    "TELShell",
    "Shell_Refuse",
    "Shell_Echo",
    "Shell_Interactor",
    "Shell_Caster"
];

# TELShell(conn, [logger], [name], [maxidle], [...])
# 单个用户的标准TEL型shell控制线程，实例化Res类作为交互对象；
#   conn        : socket                                // 该用户的socket连接；
#   logger      : logger                                // 该用户的日志实例；
#   name        : str                                   // 该用户的线程名称；
#   maxidle     : float                                 // 该用户的最大空闲，超时下线；
#   maxhistory  : int                                   // 该用户的最大历史深度；
#   telfront    : class(Front)                          // 用于控制输入处理的类；
#   resload     : class(ResLoad)                        // 用于控制资源加载的类；
#   frontpage   : res                                   // 首页的资源标识符res；

class Shell_BNYYCS(threading.Thread):

    def __init__(
        self,
        conn,
        logger      = logger,
        name        = '',
        maxidle     = 900,
        maxhistory  = 8,
        telfront    = None,
        resload     = None,
        frontpage   = 'res::front',
    ) -> None:
        super().__init__();
        self.conn = conn;
        self.logger = logger;
        self.name = name if name else hex(id(self));
        self.maxidle = maxidle;
        self.maxhistory = maxhistory;
        self.resload = resload();
        self.front = telfront();
        self.res = self.resload.getres(res = frontpage, **self.params);
        self.history = [self.res.res];
        self.timestamp = time.time();
        self._flagstop = False;
        return;
    
    def stop(self) -> None:
        self._flagstop = True;
        return;
    
    def run(self) -> None:
        self.logger.info('User [%s] running...' % self.name);
        try:
            # TO DO HERE
            # ......
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
