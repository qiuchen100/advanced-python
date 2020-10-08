# -*- coding: utf-8 -*-
class User:
    def __new__(cls, *args, **kwargs):
        '''
        对象的生成过程
        :param args:
        :param kwargs:
        '''
        print(' in new ')
        return super().__new__(cls)

    def __init__(self, name):
        print(' in init ')
        self.name = name

# new是用来控制对象的生成过程，在对象生成之前
# init是用来完善对象的（初始化）
# 如果new方法不返回对象，则不会调用init函数


if __name__ == '__main__':
    user = User(name='qqq')
    print(user.name)
