# -*- coding: utf-8 -*-

class A:
    aa = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(2, 3)
# 属性查找方式
# 先查找对象，对象变量里不存在，则继续向上查找类变量
print(a.x, a.y, a.aa)
# print(A.x) 属性只会向上查找，不会往下查找

# 实际上只是给对象a的属性aa赋值为45，不影响类变量aa的值
a.aa = 45
print(a.x, a.y, a.aa)

b = A(2, 3)
print(b.x, b.y, b.aa)

A.aa = 45
print(a.x, a.y, a.aa)

b = A(2, 3)
print(b.x, b.y, b.aa)