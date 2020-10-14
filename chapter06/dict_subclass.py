# -*- coding: utf-8 -*-
# 不建议继承list和dict
class Mydict(dict):
    def __setitem__(self, key, value):
        super(Mydict, self).__setitem__(key, value*2)


my_dict = Mydict(one=1)
my_dict['one'] = 1
print(my_dict)