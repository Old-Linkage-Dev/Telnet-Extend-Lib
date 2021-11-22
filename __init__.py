
# -*- coding: UTF-8 -*-

# 包的接口

# 该包的总接口，应当对包的细节进行过滤，提供良好的用户调用接口的总结；

from . import CONSTS;
from . import TELMain;
from . import TELShell;
from . import TELFront;

from .TELMain import *;
from .TELShell import *;
from .TELFront import *;

from .TELLog import logger;



__all__ = (
    [
        "CONSTS",
        "TELMain",
        "TELShell",
        "TELFront",
    ] +
    TELMain.__all__ +
    TELShell.__all__ +
    TELFront.__all__
);

__author__ = "Tarcadia, Mundanity-fc";
__url__ = "https://github.com/Tarcadia/Telnet-Extend-Lib";
__copyright__ = "Copyright 2021";
__credits__ = ["Tarcadia", "Mundanity-fc"];
__license__ = "GNU GENERAL PUBLIC LICENSE VERSION 3";
__version__ = "ProtoType 1.0.0";

logger.info('OLD.CLI Mod Loaded.');
logger.info('Locense: %s' % __license__);
logger.info('Version: %s' % __version__);
logger.info('Find on: %s' % __url__);
logger.info('%s (c) %s' % (__author__, __copyright__));