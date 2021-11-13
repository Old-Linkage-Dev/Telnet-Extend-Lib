
# -*- coding: UTF-8 -*-

import socket;

from . import bnyycsShell as Shell;
from . import bnyycsUser as User;
from . import bnyycsRes as Res;

from .bnyycsLog import logger;



# BNYYCS([host], [port], [backlog], **kargs)        // 描述该telnet网站的类，对该类的一个实例是一个telnet网站；
#   host        : str                               // 网站地址；
#   port        : int                               // 网站端口，默认为telnet的23端口；
#   backlog     : int                               // 网站同时接入的最大连接数；
#   block       : bool                              // 网站是否阻塞性等待连接；
#   **kargs     : **kargs                           // 其他参数，传递至各个Shell类；

# .open()       : iter + context                    // 开启网站服务，返回一个迭代器表示每轮update，可以通过with的上下文形式访问；
# .close()      : none                              // 关闭网站服务；
# .update()     : update                            // 单次update的调用，概念上返回本次update的信息，未实现；

class BNYYCS:

    def __init__(self, host = socket.gethostname(), port = 23, backlog = 16, block = True, shellclass = Shell.Shell_BNYYCE, **kwargs) -> None:
        self.host = host;
        self.port = port;
        self.backlog = backlog;
        self.block = block;
        self.shellclass = shellclass;
        self.kwargs = kwargs;

        self.server = None;
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
    
    def update(self):
        try:
            if len(self.pool) < self.backlog:
                connection, address = self.server.accept();
                shell = self.shellclass(conn = connection, **self.kwargs);
                user = (address, connection, shell);
                self.pool.append(user);
                logger.info('New user [%s] @%s:%d.' % (shell.name, *address));
            else:
                connection, address = self.server.accept();
                self.server.close();
                logger.info('New connection refused @%s:%d.' % address);
        except BlockingIOError:
            pass;
        
        pool = [];
        for address, connection, shell in self.pool:
            if shell.is_alive():
                pool.append(address, connection, shell);
            else:
                logger.info('Removed user [%s] @%s:%d.' % (shell.name, *address));
        self.pool = pool;
