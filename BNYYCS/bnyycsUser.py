
# -*- coding: UTF-8 -*-

from . import bnyycsRes as Res;

from .bnyycsLog import logger;
from .bnyyceCtrl import *;

__all__ = [
    "User"
];



class User:

    def __init__(self) -> None:
        self.res = Res.Res_RefusePage();
        self.tab = -1;
        self.cmd = '';
        self.arg = {};
        self._cmd_ready = False;
        return;
    
    @property
    def page(self):
        #return CHR_CLR + CHR_T_FC_BLUE + b"Hello World" + CHR_T_RST + CHR_CRLF;
        return self.res.draw(self.tab);
    
    @property
    def line(self):
        return b"\033[0;33m >> \033[0;34m%s\033[0m" % bytes(self.cmd, "ascii");
    
    def update(self, inp):
        for c in inp:
            self.tab = (self.tab + 2) % (len(self.res.cmds) + 1) - 1;
            self.cmd = self.res.cmds[self.tab] if self.tab >= 0 else self.cmd;
        return None;
