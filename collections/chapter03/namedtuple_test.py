# -*- coding:utf-8 -*-
from collections import namedtuple

# namedtuple非常节省空间，相对于类
User = namedtuple('User', ['name', 'age', 'height'])

user = User(name='QQ', age=30, height=175)
print(user.height)
print(type(user.height))

print(type(User))
print(type(user))