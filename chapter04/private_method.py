# -*- coding: utf-8 -*-
from chapter04.class_method import Date
class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2020 - self.__birthday.year


class Student(User):
    def __init__(self, birthday):
        self.__birthday = birthday

if __name__ == '__main__':
    user = User(Date(1990,2,1))
    print(user.get_age())
    print(user._User__birthday) # 私有属性并未真正隐藏

    stu = Student(Date(1990,2,1))
    print(stu._Student__birthday)