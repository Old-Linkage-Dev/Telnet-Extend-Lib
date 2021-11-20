
# -*- coding: UTF-8 -*-

import math;

from .bnyycsCtrl import *;

# 待解决问题
# 需要计算字符位宽，可以参考如https://www.zhangshengrong.com/p/noXQj671G6/的内容
# 需要统一字符编码问题，在bnyycsCtrl模块里已经定义了CHRSET_SYS和CHRSET_EXT的编码标准，
# 这里CHRSET_SYS我们要求本系统内的所有提供的内容应当满足CHRSET_SYS的字符集，并全部使用bytes的数据格式来传递信息流，
# 而CHRSET_EXT则是针对可能的用户输入做的约定，为的是避免不同用户间的编码不同，如使用ANSI-GBK的和使用UTF8的和使用ANSI其他的，
# 目前为止，还未找到通过telnet的option进行约定的形式，所以这里只能手动硬性规定了；

# 对于绘制来说，应当完全参照CHRSET_EXT的编码格式对系统的输入进行解码，后以字符为单位进行处理；
# 由于约定了CHRSET_EXT，我们也可以期望实现一个针对str类型的shell，以减少在bytes和str之间类型转换带来的痛苦和性能开销；
# 如果需要实现如此的一个shell，就也需要对应的实现一个将输入bytes数据流转为str的InputQueue类，以及实现一整套str的后台，
# 这部分工作量可以在主要功能完成后重新参照开发；

# 要期末考试了，暂缓开发；