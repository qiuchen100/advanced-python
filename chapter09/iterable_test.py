# -*- coding: utf-8 -*-

# 迭代器是访问集合内元素的一种方式，一般用来遍历数据
# 迭代器无法按下标访问数据，迭代器同时提供了一种惰性方式访问数据
# [] list , __iter__

from collections.abc import Iterable, Iterator
a = [1, 2]
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))

class T:
    def __init__(self):
        self._iter = [1, 2, 3, 4]
        self.start = 0
        self.end = len(self._iter)
    def __iter__(self):
        return iter(self._iter)

    # def __next__(self):
    #     if self.start >= self.end:
    #         raise StopIteration()
    #     value = self._iter[self.start]
    #     self.start += 1
    #     return value


t = T()
print(isinstance(t, Iterable))
print(isinstance(t, Iterator))
for tt in t:
    print(tt)
