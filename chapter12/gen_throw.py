# -*- coding: utf-8 -*-


def gen_func():
    # 1.可以产出值 2.可以接收值(调用方传递进来的值)
    try:
        yield 'http://www.baidu.com'
    except Exception as e:
        pass
    # yield 'http://www.baidu.com'
    yield 2
    yield 3
    return "ok"


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    i = gen.throw(Exception, 'download error')
    print(i)  # 2
    print(next(gen))
    gen.throw(Exception, 'download error2')
