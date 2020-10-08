# -*- coding: utf-8 -*-

class A:
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        # super(B, self).__init__() Python2的用法
        super().__init__() # super函数是获取它的父类
        print('B')

class C(A):
    def __init__(self):
        super().__init__()
        print('C')

class D(B, C):
    def __init__(self):
        super().__init__()
        print('D')


if __name__ == '__main__':
    # b = B()
    d = D()


# mixin模式特点
# 1. Mixin功能单一
# 2. 不和基类关联,可以和任意基类组合，基类可以不和mixin关联就能初始化成功
# 3. 在mixin中不要使用super这种用法