
import time;

import socket;
from . import bnyycsUser as User;
from . import bnyycsRes as Res;

from .bnyycsLog import logger;



# BNYYCS([host], [port], [backlog], [maxidle])      // 描述该telnet网站的类，对该类的一个实例是一个telnet网站；
#   host        : str                               // 网站地址；
#   port        : int                               // 网站端口，默认为telnet的23端口；
#   backlog     : int                               // 同时接入的最大连接数；
#   maxidle     : float                             // 单个用户的最大空闲，超时下线；

# .open()       : iter + context                    // 开启网站服务，返回一个迭代器表示每轮update，可以通过with的上下文形式访问；
# .close()      : none                              // 关闭网站服务；
# .update()     : update                            // 单次update的调用，概念上返回本次update的信息，未实现；

class BNYYCS:

    def __init__(self, host = socket.gethostname(), port = 23, backlog = 16, maxidle = 300) -> None:
        self.host = host;
        self.port = port;
        self.backlog = backlog;
        self.maxidle = maxidle;

        self.server = None;
        self.pool = [];
        return;
    
    def open(self):

        class context:

            def __enter__(context):
                logger.debug('__enter__');
                return context;
            
            def __exit__(context, type, value, trace):
                self.close();
                logger.debug('__exit__');
                return;
            
            def __iter__(context):
                while True:
                    yield self.update();


        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        self.server.setblocking(False);
        self.server.bind((self.host, self.port));
        self.server.listen(self.backlog);
        return context();
    
    def close(self):
        for t, address, connection, user in self.pool:
            connection.shutdown(socket.SHUT_RDWR);
        self.server.close();
    
    def update(self):
        try:
            connection, address = self.server.accept();
            connection.setblocking(False);
            user = User.User();
            t = time.time();
            conn = (t, address, connection, user);
            self.pool.append(conn);
        except BlockingIOError:
            pass;
        
        pool = [];
        for t, address, connection, user in self.pool:
            try:
                recv = connection.recv(4096);
            except BlockingIOError:
                recv = None;
            if recv and user.update(recv):
                try:
                    connection.send(user.page);
                    connection.send(user.line);
                    t = time.time();
                    conn = (t, address, connection, user);
                    pool.append(conn);
                except:
                    connection.close();
            elif time.time() - t <= self.maxidle:
                conn = (t, address, connection, user);
                pool.append(conn);
            else:
                connection.shutdown(socket.SHUT_RDWR);
        self.pool = pool;
        
        
        
