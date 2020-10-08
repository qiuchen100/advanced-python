# -*- coding: utf-8 -*-
from collections.abc import Iterable, Iterator

class Company(object):
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def __getitem__(self, item):
        return self.employee_list[item]

if __name__ == '__main__':
    company = Company(['Bob', 'Jane', 'Tom'])
    my_iter = iter(company)
    for item in my_iter:
        print(item)

    print(isinstance(company, Iterable))