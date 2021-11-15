#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import logging;

VERSION = 'v20211111';

logger = logging.getLogger(__name__);
logger.setLevel(logging.DEBUG);
_logger_ch = logging.StreamHandler();
_logger_ch.setLevel(logging.DEBUG);
_logger_formatter = logging.Formatter(fmt='\033[0m%(asctime)s \033[1;34m[%(levelname)s]\033[0;33m[%(name)s]\033[0m >> %(message)s', datefmt='%H:%M');
_logger_ch.setFormatter(_logger_formatter);
logger.addHandler(_logger_ch);
logger.info('Running...');



import traceback;
import time;
import BNYYCS;

# 初始化BNYYCS模块
# BNYYCE模块通过open/close对进行访问，open返回一个update的迭代器
# open可使用with进行
# 开始轮询和

##  serv = BNYYCS.BNYYCS(
##      host = "localhost",
##      port = 23,
##      backlog = 4,
##      poolsize = 3,
##      block = True,
##      shellclass = BNYYCS.Shell_Caster,
##      shell = 'python still_alive_credit_fortelnet.py'
##  );

##  serv = BNYYCS.BNYYCS(
##      host = "localhost",
##      port = 23,
##      backlog = 4,
##      poolsize = 3,
##      block = True,
##      shellclass = BNYYCS.Shell_Echo,
##      prt = True
##  );

serv = BNYYCS.BNYYCS(
    host = "localhost",
    port = 23,
    backlog = 4,
    poolsize = 16,
    block = True,
    shellclass = BNYYCS.Shell_BNYYCE,
    maxidle = 300
);

#serv = BNYYCS.BNYYCS(host = "localhost");

try:
    with serv.open() as updates:
        for update in updates:
            time.sleep(0.5);
            if update:
                logger.debug(update);
except Exception as err:
    logger.error(err);
    logger.debug(traceback.format_exc());
    logger.critical('Main Loop run into an exception.');