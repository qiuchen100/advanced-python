# -*- coding: utf-8 -*-

# 1.loop会被放到future中
# 2.取消future(task)

import asyncio
import time
import random


async def get_html(id, sleep_time):
    print(f'task No{id} starting')
    await asyncio.sleep(sleep_time)
    print(f'task No{id} done after {sleep_time}s.')


if __name__ == '__main__':
    tasks = [get_html(i, random.randint(1, 5)) for i in range(5)]
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print('cancel task')
            print(task.cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()

