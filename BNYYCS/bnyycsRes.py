
# -*- coding: UTF-8 -*-

import math;

from .bnyycsLog import logger;
from .bnyyceCtrl import *;

__all__ = [
    "splitres",
    "Resource",
    "Res_RefusePage",
];



# res = str
# 本系统使用的统一资源标识符，
# 形如"res:<path>[:<type>[:<param>[:<param...>]]]"



# splitres(res:res) : list[str]
# 用于拆分一个res为各个分段，
# 去除头部res标准，返回各个分段；

def splitres(res:str):
    s = res.split(':');
    assert s[0] == 'res';
    return s[1:];



# Resource(res:res)
# 资源的基类，不在本类实现资源的具体形式，只定义公共接口；
#   res         : res                                   // 实例化资源的res标识符；
#
# .res          : res                                   // 该资源的res标识符；
# .cmds         : [str]                                 // 该资源的待选指令；
# .run(cmd:str, *args)                                  // 向资源发送一条指令执行；
#               : none
# .draw(tab:int)                                        // 该资源的一次绘制；
#               : bytes                                 // tab为绘制时的焦点位置；

class Resource:
    
    def __init__(self, res, **kwargs) -> None:
        self.res = res;
        self.cmds = [];
        return;
    
    def run(self, cmd, *args, **kwargs):
        return;

    def draw(self, tab):
        return;

class Res_RefusePage(Resource):

    def __init__(self, res = 'res::refuse', **kwargs) -> None:
        self.res = res;
        self.cmds = ['back', 'quit'];
        s = splitres(res);
        self.reason = s[3] if len(s) >= 3 else '';
    
    def run(self, cmd, *args, **kwargs):
        return;

    def draw(self, tab):
        _reason = self.reason if len(self.reason) <= 72 else self.reason[:69] + '...';
        _lspace = b'%*s' % (math.ceil((72 - len(bytes(_reason, 'ascii'))) / 2), b'');
        _rspace = b'%*s' % (math.floor((72 - len(bytes(_reason, 'ascii'))) / 2), b'');
        _midwords = bytes(_reason, 'ascii');
        _elem_back = CHR_T_RST + CHR_T_BC_WHITE + b'[ BACK ]' + CHR_T_RST if tab == 0 else b'[ BACK ]';
        _elem_quit = CHR_T_RST + CHR_T_BC_WHITE + b'[ QUIT ]' + CHR_T_RST if tab == 1 else b'[ QUIT ]';
        return b''.join([
        CHR_CLR,
        CHR_CSI_CUP,
        CHR_T_FC_YELLO,
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
        CHRf_CSI_CUP(14, 36), _elem_back,
        CHRf_CSI_CUP(16, 36), _elem_quit,
        CHRf_CSI_CUP(24, 80),
        CHR_T_RST
        ]);
    

