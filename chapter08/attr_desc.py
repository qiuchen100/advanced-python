# -*- coding: utf-8 -*-
from datetime import date, datetime
import numbers


class IntField:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('Int value need!')
        if value < 0:
            raise ValueError('Positive value need!')
        self.value = value

    def __delete__(self, instance):
        pass


class NonDataIntField:
    def __get__(self, instance, owner):
        return 25

class User:
    age = IntField()

    tt = NonDataIntField()

    def __init__(self):
        self.name = 'weizhi'




if __name__ == '__main__':
    user = User()
    user.age = 30
    print(user.age)
    print(getattr(user, 'age'))
    print(user.__dict__)
    print(User.__dict__)
    user2 = User()

    print(user2.age)
    user2.__dict__['age'] = 'abc'
    print(user2.age)

    print(user2.tt)
    user2.__dict__['tt'] = 'abc'
    print(user2.tt)