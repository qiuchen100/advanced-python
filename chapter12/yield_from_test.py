# -*- coding: utf-8 -*-
#
# Python3.3新加了yield from

from itertools import chain


my_list = [1, 2, 3]
my_dict = {
    'bobo1' : 'http://projectedu.com',
    'bobo2' : 'http://www.baidu.com',
}

def my_chain(*args, **kwargs):
    for iter in args:
        yield from iter
        # for item in iter:
        #     yield item

for value in my_chain(my_list, my_dict, range(5, 10)):
    print(value)