# -*- coding: utf-8 -*-


def gen_func():
    # 1.可以产出值 2.可以接收值(调用方传递进来的值)
    # yield 'http://www.baidu.com'
    try:
        yield 'http://www.baidu.com'
    except GeneratorExit as ex:
        raise ex
    # yield 'http://www.baidu.com'
    yield 2
    yield 3
    return "ok"


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    # gen.close()
    print(next(gen))
