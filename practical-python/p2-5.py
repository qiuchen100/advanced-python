# -*- coding: utf-8 -*-
#快速找到公共键

from random import randint, sample

a = sample('abcdefgh', 3)
print(a)

a = sample('abcdefgh', randint(3, 6))
print(a)

d1 = {k : randint(1, 4) for k in sample('abcdefgh', randint(3, 6))}
d2 = {k : randint(1, 4) for k in sample('abcdefgh', randint(3, 6))}
d3 = {k : randint(1, 4) for k in sample('abcdefgh', randint(3, 6))}

print(d1.keys())
print(d2.keys())
print(d3.keys())
print(d1.keys() & d2.keys() & d3.keys())