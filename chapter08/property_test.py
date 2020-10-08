# -*- coding: utf-8 -*-
from datetime import date, datetime

class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.__age = datetime.now().year - self.birthday.year

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

if __name__ == '__main__':
    user = User('QQ', date(year=1990, month=1, day=1))
    print(f'in {__file__} file.')
    print(user.age)