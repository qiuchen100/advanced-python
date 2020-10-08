# -*- coding: utf-8 -*-

try:
    print('code started')
    # raise IndexError
except KeyError as e:
    print('key error')
else:
    print('other error')
finally:
    print('finally')

print('-' * 50)


def exe_try():
    try:
        print('code started')
        raise KeyError
        return 1
    except KeyError as e:
        print('key error')
        return 2
    else:
        print('other error')
        return 3
    finally:
        print('finally')
        # return 4


t = exe_try()
print(t)


# 上下文管理器协议
class Sample:
    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print('exit')

    def do_something(self):
        raise ValueError('sample error')
        print('do_something')


if __name__ == '__main__':
    print('-' * 50)
    with Sample() as sample:
        sample.do_something()
