# -*- coding: utf-8 -*-

a = 1
print(id(a))       #身份
print(type(a))     #类型
print(a)           #值

# None全局唯一
print(id(None))
a = None
b = None
print(id(a))
print(id(b))