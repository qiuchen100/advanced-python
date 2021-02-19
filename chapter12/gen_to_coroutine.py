# -*- coding: utf-8 -*-
import inspect


def gen_func():
    yield 1
    return 'qiuchen'


if __name__ == '__main__':
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    print(next(gen))
    print(inspect.getgeneratorstate(gen))
    try:
        print(next(gen))
    except StopIteration as e:
        pass
    print(inspect.getgeneratorstate(gen))
