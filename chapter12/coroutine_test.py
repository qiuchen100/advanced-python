# -*- coding: utf-8 -*-

def get_url(url):
    #do something
    html = get_html(url)
    #parse html
    urls = parse_url(html)

def get_html(url):
    pass

def parse_url(html):
    pass


# 传统函数调用，过程 A->B->C
# 出现了协程 -> 有多个入口的函数；可以暂停的函数(可以向暂停的地方传入值)

def gen_func():
    # 1.可以产出值 2.可以接收值(调用方传递进来的值)
    html = yield 'http://www.baidu.com'
    print(html)
    yield 2
    yield 3
    return "ok"

# 1.生成器不只可以产出值，还可以接收值

if __name__ == '__main__':
    gen = gen_func()
    url = next(gen)
    html = 'sina'
    t = gen.send(html)
    # t = gen.send(html)
    print(t)
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))