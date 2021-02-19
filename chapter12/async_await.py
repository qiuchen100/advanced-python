# -*- coding: utf-8 -*-
# Python为了将语义更明确，就引入了async和await来定义原生协程
import types

# async def downloader(url):
#     return 'qiuchen'


@types.coroutine
def downloader(url):
    yield 'qiuchen'


async def download_url(url):
    html = await downloader(url)
    return html


if __name__ == '__main__':
    coro = download_url('http://www.baidu.com')
    coro.send(None)
    # try:
    #     coro.send(None)
    # except StopIteration as e:
    #     print(e.value)
