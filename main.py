#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import BNYYCS;


serv = BNYYCS.__bnyycs_main__.BNYYCS(host = "localhost");
with serv.open() as updates:
    for x in updates:
        pass;
    
print('end');
