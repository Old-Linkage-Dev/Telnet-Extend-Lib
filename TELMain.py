
# -*- coding: UTF-8 -*-

# 该库的主要接口类；
# 应当实现一个高层的，可以快速部署使用的类；

import socket;
import traceback;
import threading;

from . import TELShell;

from ..OLDLog import logger;
from ..OLDLog import loggergetter;

__all__ = [
    "TEL"
];



# TEL([host], [port], [backlog], [poolsize], [block], [logger], [loggergetter], [shellclass], **kargs)
# 描述该telnet网站的类，对该类的一个实例是一个telnet网站；
#   host        : str                               // 网站地址；
#   port        : int                               // 网站端口，默认为telnet的23端口；
#   backlog     : int                               // 网站接入缓冲区的大小；
#   poolsize    : int                               // 网站同时接入的最大连接数，
#                                                   // poolsize应当明显大于backlog，不然你让人家等了最后进来吃拒绝页吗；
#   block       : bool                              // 网站连接是否为阻塞性，低负载下建议为True，
#                                                   // 非阻塞下会明显增大轮询开销，
#                                                   // 修改此属性会明显改变系统行为；
#   logger      : logger                            // 网站的日志实例；
#   loggergetter: function                          // 网站用户的日志实例
#   shellclass  : class                             // 网站的Shell类型；
#   **kargs     : **kargs                           // 其他参数，传递至各个Shell类；

# .open()       : iter + context                    // 开启网站服务，返回一个迭代器表示每轮update，
#                                                   // 可以通过with的上下文形式访问；
# .close()      : none                              // 关闭网站服务；
# .update()     : update                            // 单次update的调用，概念上返回本次update的信息，
#                                                   // 未实现；

class TEL:

    def __init__(
        self,
        host = socket.gethostname(),
        port = 23,
        backlog = 16,
        poolsize = 16,
        block = True,
        logger = logger,
        loggergetter = loggergetter,
        shellclass = TELShell.Shell,
        **kwargs
    ) -> None:
        self.host = host;
        self.port = port;
        self.backlog = backlog;
        self.poolsize = poolsize;
        self.block = block;
        self.logger = logger;
        self.loggergetter = loggergetter;

        self.shellclass = shellclass;
        self.kwargs = kwargs;

        self.server = None;
        self.thread = None;
        self.pool = [];
        return;
    
    def open(self):

        class context:

            def __enter__(context):
                return context;
            
            def __exit__(context, type, value, trace):
                self.close();
                return;
            
            def __iter__(context):
                while True:
                    yield self.update();
        
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        self.server.setblocking(self.block);
        self.server.bind((self.host, self.port));
        self.server.listen(self.backlog);
        return context();
    
    def close(self):
        for address, connection, shell in self.pool:
            if shell.is_alive():
                shell.stop();
        for address, connection, shell in self.pool:
            try:
                if shell.is_alive():
                    shell.join(timeout = 5);
            except:
                continue;
        for address, connection, shell in self.pool:
            try:
                if not connection._closed:
                    connection.shutdown(socket.SHUT_RDWR);
            except:
                continue;
        for address, connection, shell in self.pool:
            try:
                if not connection._closed:
                    connection.close();
            except:
                continue;
        self.server.close();
    
    def release(self):
        pool = [];
        for address, connection, shell in self.pool:
            if shell.is_alive():
                pool.append((address, connection, shell));
            else:
                self.logger.info('Removed user [%s] @%s:%d.' % (shell.name, *address));
        self.pool = pool;

    def update(self):
        try:
            connection, address = self.server.accept();
            self.release();
            if len(self.pool) < self.poolsize:
                if self.loggergetter == None:
                    logger = self.logger;
                else:
                    logger = self.loggergetter(name = ("User@%s:%s" % address));
                shell = self.shellclass(conn = connection, logger = logger, **self.kwargs);
                user = (address, connection, shell);
                self.pool.append(user);
                shell.start();
                self.logger.info('New user [%s] @%s:%d.' % (shell.name, *address));
            else:
                connection.close();
                self.logger.info('New connection refused @%s:%d.' % address);
        except (BlockingIOError, TimeoutError):
            pass;

    def threadrun(self, name = 'TEL'):
        
        def run():
            try:
                with self.open() as updates:
                    for update in updates:
                        if update:
                            logger.debug(update);
            except Exception as err:
                self.logger.critical('Threaded Main Loop run into an exception.');
                self.logger.info(err);
                self.logger.debug(traceback.format_exc());
        
        self.thread = threading.Thread(target = run, name = name);
        self.thread.start();
