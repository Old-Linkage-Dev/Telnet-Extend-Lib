#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import logging as __logging__;

VERSION = 'v20211111';

__logger__ = __logging__.getLogger(__name__);
__logger__.setLevel(__logging__.DEBUG);
__logger_ch__ = __logging__.StreamHandler();
__logger_ch__.setLevel(__logging__.DEBUG);
__logger_formatter__ = __logging__.Formatter(fmt='\033[0m%(asctime)s \033[1;34m[%(levelname)s]\033[0;33m[%(name)s]\033[0m >> %(message)s', datefmt='%H:%M');
__logger_ch__.setFormatter(__logger_formatter__);
__logger__.addHandler(__logger_ch__);
__logger__.info('Running...');



import BNYYCS;

serv = BNYYCS.__bnyycs_main__.BNYYCS(host = "localhost");
try:
    with serv.open() as updates:
        for update in updates:
            if update:
                __logger__.debug(update);
except:
    __logger__.info('Ended.');