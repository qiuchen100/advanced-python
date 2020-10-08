# -*- coding: utf-8 -*-

class Cat(object):
    def say(self):
        print('I am a cat.')


class Dog(object):
    def say(self):
        print('I am a dog.')

    def __getitem__(self, item):
        return 'dog'


class Duck(object):
    def say(self):
        print('I am a duck.')


animal = Cat
animal().say()

dog = Dog()

# for d in dog:
#     print(d)

a = ['a1', 'a2']
name_set = set()
name_set.add('s1')
name_set.add('s2')
a.extend(name_set)
print(a)