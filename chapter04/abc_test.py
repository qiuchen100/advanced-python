# -*- coding: utf-8 -*-

# 我们去检查某个类是否有某种方法

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


company = Company(['Bob', 'Tom', 'Jane'])
print(len(company))
print(hasattr(company, '__len__'))

from collections.abc import Sized
print(isinstance(company, Sized))

# 我们在某些情况之下希望判定某个对象的类型
# 我们需要强制某个子类必须实现某些方法

import abc

# class CacheBase():
#     def get(self, key):
#         raise NotImplementedError
#
#     def set(self, key, value):
#         raise NotImplementedError
#
# class RedisCache(CacheBase):
#     pass
#
# redisCache = RedisCache()
# redisCache.set("key", "value")

class CacheBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass

class RedisCache(CacheBase):

    def __init__(self):
        self.__kv = {}

    def get(self, key):
        return self.__kv[key]

    def set(self, key, value):
        self.__kv[key] = value

redisCache = RedisCache()
redisCache.set("key", "value")
print(redisCache.get('key'))
print(type(redisCache))