# -*- coding: utf-8 -*-

def add(a, b):
    a += b
    return a


class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)

if __name__ == '__main__':
    a = 1
    b = 2
    c = add(a, b)
    print(c)
    print(a, b)

    a = [1, 2]
    b = [3, 4]
    c = add(a, b)
    print(c)
    print(a, b)

    a = (1, 2)
    b = (3, 4)
    c = add(a, b)
    print(c)
    print(a, b)

    staffs = ['qq1', 'qq2']
    com1 = Company('mycom', staffs)
    com1.add('qq3')
    print(com1.staffs)
    com1.remove('qq1')
    print(com1.staffs)
    print(staffs)

    com2 = Company('com2')
    com2.add('bb2')
    com3 = Company('com3')
    com2.add('bb3')
    print(com2.staffs)
    print(com3.staffs)
    print(com2.staffs is com3.staffs)
    print(Company.__init__.__defaults__)

