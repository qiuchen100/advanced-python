# -*- coding: utf-8 -*-

# Python自省是通过一定的机制查询到对象的内部结构
from chapter04.class_method import Date

class Person:
    '''
    人
    '''
    name = "user"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == '__main__':
    user = Student('同济大学')

    # 通过__dict__查找属性
    print(user.__dict__)
    user.__dict__['school_name'] = '天津大学'
    print(user.school_name)
    print(Student.__dict__)
    print(Person.__dict__)
    print(dir(Person))
    print(dir(user))
