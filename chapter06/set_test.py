# -*- coding:utf-8 -*-
# set集合    frozenset 不可变集合

s = set('abcdcdea')
print(s)

s = set(['568', 'ccc', 'ccc', 'oio'])
print(s)

fs = frozenset('yyuughcd')
print(fs)

another_set = set(['ty', 'oio', '567', '568'])
s.update(another_set)
print(s)
print(s - another_set)
print(s & another_set)
print(s and another_set)
print(s | another_set)
print(s or another_set)

# print(fs.union(another_set))
# print(fs)

# set性能很高 hash算法