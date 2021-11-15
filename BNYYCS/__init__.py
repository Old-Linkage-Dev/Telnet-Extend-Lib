
from . import bnyycsMain as _bnyycs_main;
from . import bnyycsShell as _bnyyce_shell;
from . import bnyycsUser as _bnyycs_user;
from . import bnyycsRes as _bnyycs_res;
from . import bnyycsLog as _bnyycs_log;

from .bnyycsLog import logger;
from .bnyycsMain import *;
from .bnyycsShell import *;
from .bnyycsUser import *;
from .bnyycsRes import *;



__all__ = (
    _bnyycs_main.__all__
  + _bnyyce_shell.__all__
  + _bnyycs_user.__all__
  + _bnyycs_res.__all__
);

__author__ = "Tarcadia, Mundanity-fc";
__url__ = u"https://github.com/Tarcadia/Prototype.BNYYCS/";
__copyright__ = "Copyright 2021";
__credits__ = ["Tarcadia", "Mundanity-fc"];
__license__ = "GNU GENERAL PUBLIC LICENSE VERSION 3";
__version__ = "ProtoType 1.0.0";

logger.info('BNYYCS Mod Loaded.');
logger.info('Locense: %s' % __license__);
logger.info('Version: %s' % __version__);
logger.info('Find on: %s' % __url__);
logger.info('%s (c) %s' % (__author__, __copyright__));
