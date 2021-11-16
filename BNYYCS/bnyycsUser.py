
# -*- coding: UTF-8 -*-

from . import bnyycsRes as Res;

from .bnyycsLog import logger;
from .bnyycsCtrl import *;

__all__ = [
    "User",
    "User_BNYYCS"
];



# User()
# 用户控制的基类，不在本类实现用户控制的具体形式，只定义公共接口；
# .tab          : int                                   // 该用户的焦点tab顺序，只读；
# .cmds         : [str]                                 // 该用户的待选指令，可写，由Shell传入，
#                                                       // 为字符串类型的数组，每个元素为一条指令；
# .draw(res, params)                                    // 该用户的一次绘制，res为绘制时的统一资源标识符，
#               : bytes                                 // 一个标准的user的draw应当返回一个可以实现画面绘制的bytes序列，
#                                                       // 绘制的控制序列应当遵循常用的，如VT100的控制协议，和80x24的尺寸，
#                                                       // 一个res应当只绘制屏幕下部80x4的区域，并余下(80,24)字符不绘制，
#                                                       // 限制范围因为Shell中可能会调用Res在上方80x20绘制画面，
#                                                       // 保留字符是为了避免绘制(80,24)字符后可能的换行导致内容推出屏幕，
#                                                       // 绘制的过程应当使用相对坐标，绘制前光标置于(1,21)，即下80x4区域的第一个字符位；
# .update(inps:[bytes], params)                         // 向资源发送一次接受，params是Shell当前的环境参数，
#               : str                                   // 返回update表示交由Shell执行一条指令；
class User:

    def __init__(self) -> None:
        self._tab = -1;
        self._cmd = '';
        self._cmds = [];
        self._params = {};
        return;
    
    @property
    def tab(self):
        return self._tab;

    @property
    def cmds(self):
        return self._cmds;
    
    @cmds.setter
    def cmds(self, value):
        assert type(value) == list;
        for elm in value:
            assert type(elm) == str;
        self._cmds == value;

    def draw(self, res, params = {}):
        return b'';

    def update(self, inps = [], params = {}):
        self._params = params;
        for inp in inps:
            ...;
            # do sth to inps;
        return None;



# User_BNYYCS()
# 用户控制的BNYYCS类，实现一个具有基本交互功能的类；
# .tab          : int                                   // 该用户的焦点tab顺序，只读，
#                                                       // 与cmds列表对应，指定-1表示无焦点；
# .cmds         : [str]                                 // 该用户的待选指令，可写，由Shell传入，
#                                                       // 为字符串类型的数组，每个元素为一条指令，
#                                                       // 在用户使用↑↓键时根据当前tab顺序辅助输入对应cmds，
#                                                       // 在用户使用Tab键时根据当前已输入指令执行辅助输入补全，或cmds下一，或不操作；
# .draw(res)                                            // 该用户的一次绘制，res为绘制时的统一资源标识符，
#               : bytes                                 // 在画面下方提供一个单行输入位置；
# .update(inps:[bytes], params)                         // 向资源发送一次接受，params是Shell当前的环境参数，
#               : str                                   // 返回update表示交由Shell执行一条指令；
class User_BNYYCS:

    def __init__(self) -> None:
        self.tab = -1;
        self.cmd = '';
        self.cmds = [];
        self._cmd_ready = False;
        return;
    
    def draw(self, res, params = {}):
        _scmd = self.cmd.split(maxsplit = 1);
        _cmd = (_scmd[0] + ' ') if len(_scmd) >= 1 else '';
        _para = (_scmd[1] if len(_cmd) <= 76 else _scmd[1][76 - len(_scmd[0]) - 5] + '...') if len(_scmd) >= 2 else '';
        _rspace = b'%*s' % ((76 - len(bytes(_cmd + _para, 'ascii'))), b'');
        _ret = (
            CHR_T_FC_YELLO + b' >> ' +
            CHR_T_FC_RED + bytes(_cmd, 'ascii') +
            CHR_T_FC_BLUE + bytes(_para, 'ascii') + _rspace +
            CHR_T_RST
        );
        return _ret

    def update(self, inps = [], params = {}):
        for inp in inps:
            self.tab = (self.tab + 2) % (len(self.cmds) + 1) - 1;
            self.cmd = self.cmds[self.tab] if self.tab >= 0 else self.cmd;
        return None;
