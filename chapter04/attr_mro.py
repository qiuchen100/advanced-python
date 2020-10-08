# -*- coding: utf-8 -*-

class A:
    name = 'A'

    def __init__(self):
        self.name = 'obj'

a = A()
print(a.__dict__)
print(A.__dict__)
print(a.name)

class D:
    name = 'D'

class E:
    name = 'E'

class B(D):
    # name = 'B'
    pass

# class C(D):
#     name = 'C'

class C(E):
    name = 'C'

# MRO算法
# A->B->D->C->E
class A1(B, C):
    pass

a1 = A1()
print(a1.name)

# 查找顺序
print(A1.__mro__)



class D1:
    def __init__(self):
        self.name = 'self d'

class E1:
    name = 'E'

class B1(D1):
    name = 'B'
    pass

# class C(D):
#     name = 'C'

class C1(E):
    name = 'C'

# MRO算法
# A->B->D->C->E
class A11(B1, C1):
    name = 'A11'
    pass

a11 = A11()
print(a11.name)
print(A11.__mro__)