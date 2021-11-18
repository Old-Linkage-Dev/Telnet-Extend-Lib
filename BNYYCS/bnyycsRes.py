
# -*- coding: UTF-8 -*-

import math;

from .bnyycsLog import logger;
from .bnyycsCtrl import *;

__all__ = [
    "splitres",
    "ResLoader"
    "ResLoader_BNYYCS",
    "Resource",
    "Res_RefusePage",
    "Res_SamplePage",
];



# res = bytes
# 本系统使用的统一资源标识符，
# 形如"res:<path>[:<type>[:<param>[:<param...>]]]"



# splitres(res:res) : list[bytes]
# 用于拆分一个res为各个分段，
# 去除头部res标准，返回各个分段；

def splitres(res : bytes):
    assert type(res) == bytes;
    s = res.split(b':');
    assert s[0] == b'res';
    return s[1:];



# ResLoader()
# ResLoader的基类，是用于资源加载的类，管理各个Res，
# 应当能够提供动态的加载，使得文件的更新可以在线加载，
# 建议是一个单例模式的类，以便实现以上功能；
class ResLoader:

    def __init__(self) -> None:
        return;
    
    def getres(self, res):
        return Resource();



# ResLoader_BNYYCS()
# 用于资源加载的类，管理各个Res，
# 应当能够提供动态的加载，使得文件的更新可以在线加载，
# 建议是一个单例模式的类，以便实现以上功能；
class ResLoader_BNYYCS(ResLoader):

    def __init__(self) -> None:
        return;
    
    def getres(self, res):
        return Res_SamplePage();



# Resource(res:res, params)
# 资源的基类，不在本类实现资源的具体形式，只定义公共接口；
#   res         : res                                   // 实例化资源的res标识符；
#   params      : dict                                  // Shell当前的环境参数，
#
# .res          : res                                   // 该资源的res标识符；
# .cmds         : [bytes]                               // 该资源的待选指令；
# .draw(tab:int, params)                                // 该资源的一次绘制，tab为绘制时的焦点位置，params是Shell当前的环境参数，
#               : bytes                                 // 一个标准的res的draw应当返回一个可以实现画面绘制的bytes序列，
#                                                       // 绘制的控制序列应当遵循常用的，如VT100的控制协议，和80x24的尺寸，
#                                                       // 一个res应当只绘制屏幕上部80x20的区域，一方面这有利于避免绘制(80,24)后的换行推出屏幕，
#                                                       // 另一方面因为Shell中可能会通过其他调用在画面下部绘制辅助内容，
#                                                       // 绘制的过程应当使用相对坐标，绘制前系统会清屏，光标归位左上；
# .run(cmd:bytes, *args, params)                        // 向资源发送一条指令执行，args是指令带入的参数
#               : none                                  // params是Shell当前的环境参数；
# .update(inps:[bytes], params)                         // 向资源发送一次接受，params是Shell当前的环境参数，
#               : bytes                                 // 返回update表示交由Shell执行一条指令；

class Resource:
    
    def __init__(self, res = b'res::blank', params = {}) -> None:
        self.res = res;
        self.cmds = [];
        self.params = params;
        return;
    
    def draw(self, tab, params = {}):
        return;
    
    def run(self, cmd, *args, params = {}):
        return;
    
    def update(self, recv, params = {}):
        return;



class Res_RefusePage(Resource):

    def __init__(self, res = b'res::refuse', params = {}) -> None:
        self.res = res;
        self.cmds = [b'back', b'quit'];
        s = splitres(res);
        self.reason = s[3] if len(s) >= 3 else b'';
    
    def draw(self, tab, params = {}):
        _reason = (self.reason if len(self.reason) <= 72 else self.reason[:69] + b'...') if self.reason else b'NO REASON PRESENTED';
        _lspace = b'%*s' % (math.ceil((72 - len(_reason)) / 2), b'');
        _rspace = b'%*s' % (math.floor((72 - len(_reason)) / 2), b'');
        _elem_back = CHR_T_RST + CHR_T_BC_WHITE + b'[ BACK ]' + CHR_T_RST if tab == 2 else CHR_T_FC_LBLUE + b'[ BACK ]' + CHR_T_RST;
        _elem_quit = CHR_T_RST + CHR_T_BC_WHITE + b'[ QUIT ]' + CHR_T_RST if tab == 3 else CHR_T_FC_LBLUE + b'[ QUIT ]' + CHR_T_RST;
        _ret = (
            CHR_T_FC_YELLO +
            b'#==============================================================================#' + CHR_CRLF +
            b'| CONNECTION INFORMATION                                                       |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'| The atempt to visit this site is refused,                                    |' + CHR_CRLF +
            b'| The reason to the rufusing is:                                               |' + CHR_CRLF +
            b'|   '                   + _lspace + _reason + _rspace +                   b'   |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                SUPPORTED BY PROTOTYPE BNYYCS |' + CHR_CRLF +
            b'#==============================================================================#' + CHR_CRLF +
            CHRf_CSI_CUMOV(-7, 35) + _elem_back, CHR_CRLF +
            CHRf_CSI_CUMOV(1, 35) + _elem_quit, CHR_CRLF
        );
        return _ret
    
    def update(self, inps = [], params = {}):
        return;

    def run(self, cmd, *args, params = {}):
        return;



class Res_SamplePage(Resource):

    def __init__(self, res = b'res::sample', params = {}) -> None:
        self.res = res;
        self.cmds = [b'test "this is a test"', b'help', b'back', b'quit'];
        self._lastcmd = b'';
        return;
    
    def draw(self, tab, params = {}):
        _lastcmd = (self._lastcmd if len(self._lastcmd) <= 72 else self._lastcmd[:69] + b'...') if self._lastcmd != b'' else b'NO CMD';
        _lspace = b'%*s' % (math.ceil((72 - len(_lastcmd)) / 2), b'');
        _rspace = b'%*s' % (math.floor((72 - len(_lastcmd)) / 2), b'');
        _elem_lastcmd = CHR_T_FC_LBLUE + _lspace + _lastcmd + _rspace + CHR_T_RST;
        _elem_test = CHR_T_RST + CHR_T_BC_WHITE + b'[ TEST ]' + CHR_T_RST if tab == 0 else CHR_T_FC_LBLUE + b'[ TEST ]' + CHR_T_RST;
        _elem_help = CHR_T_RST + CHR_T_BC_WHITE + b'[ HELP ]' + CHR_T_RST if tab == 1 else CHR_T_FC_LBLUE + b'[ HELP ]' + CHR_T_RST;
        _elem_back = CHR_T_RST + CHR_T_BC_WHITE + b'[ BACK ]' + CHR_T_RST if tab == 2 else CHR_T_FC_LBLUE + b'[ BACK ]' + CHR_T_RST;
        _elem_quit = CHR_T_RST + CHR_T_BC_WHITE + b'[ QUIT ]' + CHR_T_RST if tab == 3 else CHR_T_FC_LBLUE + b'[ QUIT ]' + CHR_T_RST;
        _ret = (
            CHR_T_FC_LBLUE +
            b'#==============================================================================#' + CHR_CRLF +
            b'| A SAMPLE PAGE                                                                |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'| This is a sample page to show the basic components of a page.                |' + CHR_CRLF +
            b'| Here is a line of commands sent in, printed as an element:                   |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'| Here are some selective elements with commands attached, which you can try   |' + CHR_CRLF +
            b'| selecting between them, if it is supported.                                  |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                                              |' + CHR_CRLF +
            b'|                                                SUPPORTED BY PROTOTYPE BNYYCS |' + CHR_CRLF +
            b'#==============================================================================#' + CHR_CRLF +
            CHRf_CSI_CUMOV(-15, 4) + _elem_lastcmd + CHR_CRLF +
            CHRf_CSI_CUMOV(4, 35) + _elem_test + CHR_CRLF +
            CHRf_CSI_CUMOV(1, 35) + _elem_help + CHR_CRLF +
            CHRf_CSI_CUMOV(1, 35) + _elem_back + CHR_CRLF +
            CHRf_CSI_CUMOV(1, 35) + _elem_quit + CHR_CRLF
        );
        return _ret;
    
    def update(self, inps = [], params = {}):
        return;

    def run(self, cmd, *args, params = {}):
        self._lastcmd = cmd;
        return;




