# -*- coding: utf-8 -*-

import asyncio
import time


def callback(sleep_time):
    print(f'sleep {sleep_time}s success.')


def callback2(loop):
    print(f'sleep {loop.time()}s success.')
    

def stop(loop):
    loop.stop()


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # loop.call_soon(callback, 2)
    # loop.call_soon(callback, 1)
    # loop.call_soon(callback, 3)
    # loop.call_soon(stop, loop)
    # loop.call_later(2, callback, 2)
    # loop.call_later(1, callback, 1)
    # loop.call_later(3, callback, 3)
    now = loop.time()
    loop.call_at(now+2, callback2, loop)
    loop.call_at(now+1, callback2, loop)
    loop.call_at(now+3, callback2, loop)
    loop.call_at(now+3, stop, loop)
    loop.run_forever()
    # stop(loop)
    cost_time = time.time() - start_time
    print(f'cost {cost_time}')
