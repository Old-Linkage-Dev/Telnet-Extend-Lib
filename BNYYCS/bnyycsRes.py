
# -*- coding: UTF-8 -*-

import math;

from .bnyycsLog import logger;
from .bnyyceCtrl import *;

__all__ = [
    "splitres",
    "Resource",
    "Res_RefusePage",
    "Res_SamplePage",
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



# Resource(res:res, params)
# 资源的基类，不在本类实现资源的具体形式，只定义公共接口；
#   res         : res                                   // 实例化资源的res标识符；
#   params      : dict                                  // Shell当前的环境参数，
#
# .res          : res                                   // 该资源的res标识符；
# .cmds         : [str]                                 // 该资源的待选指令；
# .draw(tab:int, params)                                // 该资源的一次绘制，tab为绘制时的焦点位置，params是Shell当前的环境参数，
#               : bytes                                 // 一个标准的res的draw应当返回一个可以实现画面绘制的bytes序列，
#                                                       // 绘制的控制序列应当遵循常用的，如VT100的控制协议，和80x24的尺寸，
#                                                       // 一个res应当只绘制屏幕上部80x20的区域，一方面这有利于避免绘制(80,24)后的换行推出屏幕，
#                                                       // 另一方面因为Shell中可能会通过其他调用在画面下部绘制辅助内容，
#                                                       // 绘制的过程应当使用相对坐标，绘制前系统会清屏，光标归位左上；
# .run(cmd:str, params)                                 // 向资源发送一条指令执行，
#               : none                                  // params是Shell当前的环境参数；
# .update(recv:bytes, params)                           // 向资源发送一次接受，params是Shell当前的环境参数，
#               : str                                   // 返回update表示交由Shell执行一条指令；

class Resource:
    
    def __init__(self, res = 'res::blank', params = {}) -> None:
        self.res = res;
        self.cmds = [];
        self.params = params;
        return;
    
    def draw(self, tab, params = {}):
        return;
    
    def run(self, cmd, params = {}):
        return;
    
    def update(self, recv, params = {}):
        return;



class Res_RefusePage(Resource):

    def __init__(self, res = 'res::refuse', params = {}) -> None:
        self.res = res;
        self.cmds = ['back', 'quit'];
        s = splitres(res);
        self.reason = s[3] if len(s) >= 3 else '';
    
    def draw(self, tab, params = {}):
        _reason = self.reason if len(self.reason) <= 72 else self.reason[:69] + '...' if self.reason else b'NO REASON PRESENTED';
        _lspace = b'%*s' % (math.ceil((72 - len(bytes(_reason, 'ascii'))) / 2), b'');
        _rspace = b'%*s' % (math.floor((72 - len(bytes(_reason, 'ascii'))) / 2), b'');
        _midwords = bytes(_reason, 'ascii');
        _elem_back = CHR_T_RST + CHR_T_BC_WHITE + b'[ BACK ]' + CHR_T_RST if tab == 0 else b'[ BACK ]';
        _elem_quit = CHR_T_RST + CHR_T_BC_WHITE + b'[ QUIT ]' + CHR_T_RST if tab == 1 else b'[ QUIT ]';
        return (
            CHR_T_FC_YELLO,
            b'#==============================================================================#', CHR_CRLF,
            b'| CONNECTION INFORMATION                                                       |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'| The atempt to visit this site is refused,                                    |', CHR_CRLF,
            b'| The reason to the rufusing is:                                               |', CHR_CRLF,
            b'|   '                  + _lspace + _midwords + _rspace +                  b'   |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                SUPPORTED BY PROTOTYPE BNYYCS |', CHR_CRLF,
            b'#==============================================================================#', CHR_CRLF,
            CHRf_CSI_CUMOV(-7, 35), _elem_back, CHR_CRLF,
            CHRf_CSI_CUMOV(1, 35), _elem_quit, CHR_CRLF,
        );
    
    def update(self, recv, params = {}):
        return;

    def run(self, cmd, params = {}):
        return;



class Res_SamplePage(Resource):

    def __init__(self, res = 'res::sample', params = {}) -> None:
        self.res = res;
        self.cmds = ['test "this is a test"', 'help', 'back', 'quit'];
        self._lastcmd = '';
        return;
    
    def draw(self, tab, params = {}):
        _str_lastcmd = self._lastcmd if len(self._lastcmd) <= 72 else self._lastcmd[:69] + '...' if self._lastcmd else b'NO REASON PRESENTED';
        _lspace = b'%*s' % (math.ceil((72 - len(bytes(_str_lastcmd, 'ascii'))) / 2), b'');
        _rspace = b'%*s' % (math.floor((72 - len(bytes(_str_lastcmd, 'ascii'))) / 2), b'');
        _b_lastcmd = bytes(_str_lastcmd, 'ascii');
        _elem_lastcmd = _lspace + _b_lastcmd + _rspace;
        _elem_test = CHR_T_RST + CHR_T_BC_WHITE + b'[ TEST ]' + CHR_T_RST if tab == 0 else CHR_T_FC_LBLUE + b'[ TEST ]' + CHR_T_RST;
        _elem_help = CHR_T_RST + CHR_T_BC_WHITE + b'[ HELP ]' + CHR_T_RST if tab == 1 else CHR_T_FC_LBLUE + b'[ HELP ]' + CHR_T_RST;
        _elem_back = CHR_T_RST + CHR_T_BC_WHITE + b'[ BACK ]' + CHR_T_RST if tab == 2 else CHR_T_FC_LBLUE + b'[ BACK ]' + CHR_T_RST;
        _elem_quit = CHR_T_RST + CHR_T_BC_WHITE + b'[ QUIT ]' + CHR_T_RST if tab == 3 else CHR_T_FC_LBLUE + b'[ QUIT ]' + CHR_T_RST;
        _ret = (
            CHR_T_FC_LBLUE,
            b'#==============================================================================#', CHR_CRLF,
            b'| A SAMPLE PAGE                                                                |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'| This is a sample page to show the basic components of a page.                |', CHR_CRLF,
            b'| Here is a line of commands sent in, printed as an element:                   |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'| Here are some selective elements with commands attached, which you can try   |', CHR_CRLF,
            b'| selecting between them, if it is supported.                                  |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                                              |', CHR_CRLF,
            b'|                                                SUPPORTED BY PROTOTYPE BNYYCS |', CHR_CRLF,
            b'#==============================================================================#', CHR_CRLF,
            CHRf_CSI_CUMOV(-15, 5), _elem_lastcmd, CHR_CRLF,
            CHRf_CSI_CUMOV(4, 35), _elem_test, CHR_CRLF,
            CHRf_CSI_CUMOV(1, 35), _elem_help, CHR_CRLF,
            CHRf_CSI_CUMOV(1, 35), _elem_back, CHR_CRLF,
            CHRf_CSI_CUMOV(1, 35), _elem_quit, CHR_CRLF,
        );
        return _ret;
    
    def update(self, recv, params = {}):
        return;

    def run(self, cmd, params = {}):
        self._lastcmd = cmd;
        return;




