# -*- coding: utf-8 -*-

import inspect

frame = None
def foo():
    bar()


def bar():
    global frame
    frame = inspect.currentframe()


#Python.exe会用一个叫做PyEval_EvalFrameEx(c函数)去执行foo函数，首先创建一个栈帧

"""
python一切皆对象，栈帧对象，字节码对象
当foo调用子函数bar，又会创建一个栈帧
所有当栈帧都是分配在堆内存上，这就决定了栈帧可以独立于调用者存在
"""
import dis
print(dis.dis(foo))

foo()
print(frame.f_code.co_name)
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)


def gen_func():
    yield 78
    name = 'qq'
    yield 40
    age = 30
    return 'ali'

gen = gen_func()
print(dis.dis(gen))
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
print(next(gen))
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
print(next(gen))
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

print(gen.gi_code)