# -*- coding: utf-8 -*-

from collections import abc

a = [1, 2]
c = a + [3, 4]
print(c)

# print(a)
# b = a.extend([3, 4])
# print(a)
# print(b)
a += (3, 4)
print(a)
