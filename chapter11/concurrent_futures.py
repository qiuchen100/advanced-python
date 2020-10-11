# -*- coding: utf-8 -*-
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
from concurrent.futures import Future

# 未来对象，task的返回容器

# 线程池
## 主线程中可以获取某一个线程的状态或者某一个任务的状态，
## 以及返回值

## 当一个线程完成的时候，我们的主线程能够立即知道，并拿到返回值

## futures可以让多线程与多进程编码接口一致

import time

def get_html(times):
    time.sleep(times)
    print(f'get page {times} success')
    return times

executor = ThreadPoolExecutor(max_workers=2)

# 通过submit函数提交执行的函数到线程池中，submit是立即返回
# task1 = executor.submit(get_html, (3))  # Future产生的对象
# task2 = executor.submit(get_html, (2))
#
# #done方法用于判定某个任务是否完成
# print(task1.done())
# print(task2.done())
# t = task2.cancel()
# print(t) # cancel失败 在执行期间是cancel不掉的
# time.sleep(2)
#
#
# print(task1.done())
# print(task2.done())
#
# # result方法可以获取task的执行结果
# print(task1.result())
# print(task2.result())

urls = [3, 2, 4]
all_task = [executor.submit(get_html, (url)) for url in urls]
wait(all_task, return_when=FIRST_COMPLETED)
print('main')
for future in as_completed(all_task):
    data = future.result()
    print(f'get {data} page success!')

# # 通过executor获得已经完成的task, 按进程放入的顺序获得返回结果
# for data in executor.map(get_html, urls):
#     print(f'get {data} page success!')
