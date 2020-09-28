# -*- coding: utf-8 -*-#

"""
# @Author: github.com/qiuchen100
# @Date: 2020/5/5 14:11
# @Description: 函数和类也是对象，是Python语言中到第一公民
# @Modified By:
"""


def ask(name='Charles'):
    print(name)


class Person:
    def __init__(self):
        print('Charles')


# my_func = ask  # 将函数对象赋予给变量
# my_func('Jack')
#
# my_class = Person  # 类也可以是一个对象（模板对象），并赋予某个变量
# my_class()

obj_list = []
obj_list.append(ask)
obj_list.append(Person)  # 可以添加到集合对象中
for item in obj_list:
    print(item())


def print_type(item):  # 可以作为参数
    print(type(item))


print_type(Person)


def decorator_func():  # 可以作为返回值
    print('deco start')
    return ask


func = decorator_func()
func("Tom")