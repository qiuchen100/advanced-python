# -*- coding: utf-8 -*-

# total = 0
#
#
# async def add():
#     global total
#     for i in range(1000000):
#         total += 1
#
#
# async def desc():
#     global total
#     for i in range(1000000):
#         total -= 1
#
#
# if __name__ == '__main__':
#     import asyncio
#     tasks = [add(), desc()]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(total)

import asyncio
from asyncio import Lock
import aiohttp

cache = {}
lock = Lock()


async def get_stuff(url):
    async with lock:
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request('GET', url)
        cache[url] = stuff
        return stuff


async def parse_stuff(url):
    stuff = await get_stuff(url)
    #do something parse


async def use_stuff(url):
    stuff = await get_stuff(url)
    #do something use