# -*- coding: utf-8 -*-

# __getattr__ __getattribute__
# __getattr__就是在查找不到属性的时候调用

from datetime import date


class User:
    def __init__(self, name, birthday, infos={}):
        self.name = name
        self.birthday = birthday
        self.infos = infos

    def __getattr__(self, item):
        return self.infos[item]

    def __getattribute__(self, item):
        return 'charles'


if __name__ == '__main__':
    user = User('QQ', date(year=1990, month=1, day=1), {'age': 35})
    print(user.name)
