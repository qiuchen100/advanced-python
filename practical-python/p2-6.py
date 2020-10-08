# -*- coding: utf-8 -*-
#让字典有序
from collections import OrderedDict
from random import shuffle

d = {}
d['c'] = 1
d['b'] = 2
d['a'] = 3
print(d)

od = OrderedDict()
od['c'] = 1
od['b'] = 2
od['a'] = 3

print(od)

players = list('abcdefgh')
print(players)
shuffle(players)
print(players)