# -*- coding: utf-8 -*-
# 不建议继承list和dict
# class Mydict(dict):
#     def __setitem__(self, key, value):
#         super(Mydict, self).__setitem__(key, value*2)
#
#
# my_dict = Mydict(one=1)
# my_dict['one'] = 3
# print(my_dict)

# from collections import UserDict
#
#
# class Mydict(UserDict):
#     def __setitem__(self, key, value):
#         super(Mydict, self).__setitem__(key, value*2)
#
#     def __missing__(self, key):
#         return 67
#
#
# my_dict = Mydict(one=1)
# my_dict['one'] = 1
# print(hasattr(my_dict.__class__, '__setitem__'))
# print(hasattr(type(my_dict), '__setitem__'))
# print(type(my_dict))
# print(my_dict['sss'])

from collections import defaultdict
my_dict = defaultdict(dict)
my_dict['one'] = 1
print(my_dict['one'])
print(my_dict['two'])
