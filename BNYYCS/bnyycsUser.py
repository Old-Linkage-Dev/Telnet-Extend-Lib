
# -*- coding: UTF-8 -*-

from .bnyycsLog import logger;

#CHAR_TYPE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-=~!@#$%^&*()_+[]{}<>,.;:\|/?`";
#CHAR_CMD = "\r\n\t\b\x7F\x03\x1B\x1B[A\x1B[B\x1B[D\x1B[C";

class User:

    def __init__(self) -> None:
        self.url = "";
        self.tab = 0;
        self.cmd = "";
        return;
    
    @property
    def page(self):
        return b"\f\033[0;34mHello World\033[0m\r\n";
    
    @property
    def line(self):
        return b"\033[0;33m >> \033[0;34m%s\033[0m" % bytes(self.cmd, "utf8");
    
    def update(self, inp):
        return True;
