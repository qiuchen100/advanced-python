# -*- coding: utf-8 -*-

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __setitem__(self, key, value):
        self.employee.append(value)

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

    def __str__(self):
        return ','.join(self.employee)

    def __repr__(self):
        return ','.join(self.employee)


company = Company(['Bob', 'Tom', 'Jane'])
employee_list = company.employee
for employee in employee_list:
    print(employee)
print('-' * 50)
company[len(company)] = 'Kate'

for emp in company:
    print(emp)
print('-' * 50)
for emp in company[:2]:
    print(emp)

print(len(company))
print(company)
print(repr(company))


class Nums(object):
    def __init__(self, num):
        self.num = num

    def __int__(self):
        return self.num

    def __abs__(self):
        return abs(self.num)

my_num = Nums(-56)
print(int(my_num))
print(abs(my_num))


class MyVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otherVecotor):
        if not isinstance(otherVecotor, MyVector):
            raise TypeError('Must be MyVector!')
        re_vector = MyVector(self.x + otherVecotor.x, self.y + otherVecotor.y)
        return re_vector

    def __str__(self):
        return f'x : {self.x} , y : {self.y}'

first_vector = MyVector(1, 3)
second_vector = MyVector(2, 7)
third_vector = first_vector + second_vector
print(third_vector)

a = ['a1', 'a2']
a.extend(company)
print(a)

