
# -*- coding: UTF-8 -*-

from . import bnyycsRes as Res;

from .bnyycsLog import logger;
from .bnyyceCtrl import *;

__all__ = [
    "User"
];



class User:

    def __init__(self) -> None:
        self.tab = -1;
        self.cmd = '';
        self.cmds = [];
        self._cmd_ready = False;
        return;
    
    def draw(self, res, **kwargs):
        return b"\033[0;33m >> \033[0;34m%s\033[0m" % bytes(self.cmd, "ascii");

    def update(self, recv, **kwargs):
        for c in recv:
            self.tab = (self.tab + 2) % (len(self.cmds) + 1) - 1;
            self.cmd = self.cmds[self.tab] if self.tab >= 0 else self.cmd;
        return None;
