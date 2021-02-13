# -*- coding:utf-8 -*-
from collections.abc import Iterable
from collections import UserList


class MyItems:
    def __init__(self, my_list: list):
        self.my_list = my_list

    def __iter__(self):
        return MyItemsGen(my_items)

    def __len__(self):
        return len(self.my_list)

    # def __getitem__(self, item):
    #     return self.my_list[item]


class MyItemsGen:
    def __init__(self, my_items: MyItems):
        self.num = 0
        self.my_items = my_items

    def __next__(self):
        i = self.num
        while i < len(self.my_items):
            self.num += 1
            return self.my_items.my_list[i]
        raise StopIteration
        return


my_items = MyItems([78, 89, 66])

print(isinstance(my_items, Iterable))

for i in my_items:
    print(i)