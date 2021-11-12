
import logging as __logging__;

VERSION = 'v20211111';

__logger__ = __logging__.getLogger(__name__);
__logger__.setLevel(__logging__.DEBUG);
__logger_ch__ = __logging__.StreamHandler();
__logger_ch__.setLevel(__logging__.DEBUG);
__logger_formatter__ = __logging__.Formatter(fmt='\033[0m%(asctime)s \033[1;34m[%(levelname)s]\033[0;33m[%(name)s]\033[0m >> %(message)s', datefmt='%H:%M');
__logger_ch__.setFormatter(__logger_formatter__);
__logger__.addHandler(__logger_ch__);
__logger__.info('Module Loaded.');
__bnyycs_main__.__logger__ = __logger__;
__bnyycs_user__.__logger__ = __logger__;
__bnyycs_res__.__logger__ = __logger__;



from . import bnyycsMain as __bnyycs_main__;
from . import bnyycsUser as __bnyycs_user__;
from . import bnyycsRes as __bnyycs_res__;

__all__ = (
);

__author__ = "Tarcadia, Mundanity-fc";
__url__ = u"https://github.com/Tarcadia/Prototype.BNYYCS/";
__copyright__ = "Copyright 2021";
__credits__ = ["Tarcadia", "Mundanity-fc"];
__license__ = "GNU GENERAL PUBLIC LICENSE VERSION 3";
__version__ = VERSION;