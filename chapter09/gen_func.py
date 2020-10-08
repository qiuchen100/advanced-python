# -*- coding: utf-8 -*-

# 生成器函数，函数里只要有yield关键字


def gen_func():
    for i in range(4):
        yield i


def pop_func():
    return 1

def gen_fib(index):
    i, a, b = 0, 0, 1
    while i < index:
        yield b
        a, b = b, a+b
        i += 1


if __name__ == '__main__':
    # 生成器对象, python编译字节码的时候就产生了
    gen = gen_func()
    # 值
    pop = pop_func()
    print(type(gen))
    print(type(pop))
    for value in gen:
        print(value)
    print('*' * 50)
    fib = gen_fib(10)
    for f in fib:
        print(f)

