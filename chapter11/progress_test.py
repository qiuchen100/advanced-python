# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
import time

# 多进程
# GIL导致CPU密集型操作无法利用多核的优势
# 多CPU操作用多进程编程。对io操作来说，使用多线程编程。
# 进程切换代价高于线程


# 1. 对于耗费CPU的操作，多进程优于多线程

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# 耗时27.06秒
# with ThreadPoolExecutor(3) as executor:
#     all_task = [executor.submit(fib, (35)) for _ in range(10)]
#     start_time = time.time()
#     for future in as_completed(all_task):
#         data = future.result()
#         print(f'exe result: {data}')
#     end_time = time.time()
#     cost_time = end_time - start_time
#     print(f"cost {str(cost_time)}!")

# 耗时10.6秒
# with ProcessPoolExecutor(3) as executor:
#     all_task = [executor.submit(fib, (35)) for _ in range(10)]
#     start_time = time.time()
#     for future in as_completed(all_task):
#         data = future.result()
#         print(f'exe result: {data}')
#     end_time = time.time()
#     cost_time = end_time - start_time
#     print(f"cost {str(cost_time)}!")


# 2. 对于耗费IO的操作，多线程优于多进程

def random_sleep(n):
    time.sleep(n)
    return n

# 耗时15秒
# with ThreadPoolExecutor(3) as executor:
#     all_task = [executor.submit(random_sleep, (n)) for n in range(6, 10)]
#     start_time = time.time()
#     for future in as_completed(all_task):
#         data = future.result()
#         print(f'exe result: {data}')
#     end_time = time.time()
#     cost_time = end_time - start_time
#     print(f"cost {str(cost_time)}!")


# 耗时15秒
with ProcessPoolExecutor(3) as executor:
    all_task = [executor.submit(random_sleep, (n)) for n in range(6, 10)]
    start_time = time.time()
    for future in as_completed(all_task):
        data = future.result()
        print(f'exe result: {data}')
    end_time = time.time()
    cost_time = end_time - start_time
    print(f"cost {str(cost_time)}!")