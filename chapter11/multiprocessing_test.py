# -*- coding: utf-8 -*-

# import os
# import time
# print('start')
# t = 'newnewnew'
# pid = os.fork()
# print(t)
# print('qq')
# if pid == 0:
#     print(f'子进程：{os.getpid()}  父进程：{os.getppid()}')
# else:
#     print(f'我是父进程：{os.getpid()}')
#
# time.sleep(2)

from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import random
import os

# 多进程编程
import time
def get_html(n):
    print(os.getpid())
    time.sleep(n)
    return n

class MyProgress(multiprocessing.Process):
    def __init__(self, n):
        super(MyProgress, self).__init__()
        self.n = n

    def run(self):
        print(os.getpid())
        time.sleep(self.n)
        return self.n

def hello(n):
    print(n)

if __name__ == '__main__':
    # progress = multiprocessing.Process(target=get_html, args=(random.randint(2, 4), ))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join()

    # progress = MyProgress(random.randint(2, 4))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join()
    pool = multiprocessing.Pool(3)
    rusult = pool.apply_async(get_html, args=(random.randint(2, 4), ), callback=hello)
    print(rusult.get())

    print('-'*70)
    for result in pool.imap_unordered(get_html, [1, 5, 3]):
        print(result)

    pool.close()
    pool.join()