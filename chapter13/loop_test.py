# -*- coding: utf-8 -*-
# 事件循环+回调（驱动生成器）+epoll(IO多路复用)
# asyncio是python用于解决异步IO编程的一整套解决方案
# tornado gevent twisted(scrapy, django channels)

import asyncio
import time
import types


@types.coroutine
def my_sleep(sleep_time):
    start = time.time()
    while time.time() - start < sleep_time:
        yield None
    return 'done'


async def get_html(url):
    print('start get url')
    t = await my_sleep(2)
    # await asyncio.sleep(2)
    print('end get url')
    return t


def callback(future):
    print('send email done!')


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(get_html('http://www.baidu.com')) for i in range(10)]
    for task in tasks:
        task.add_done_callback(callback)
    loop.run_until_complete(asyncio.wait(tasks))
    for task in tasks:
        print(task.result())
    # future = asyncio.ensure_future(get_html('http://www.baidu.com'))
    # task = loop.create_task(get_html('http://www.baidu.com'))
    # loop.run_until_complete(task)
    # print(task.result())
    print(time.time() - start_time)
