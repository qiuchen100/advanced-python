# -*- coding: utf-8 -*-
import time
import threading
# 对于io操作来说，多线程和多进程性能差别不大
# 1.通过Thread类实例化


def get_detail_html(url):
    print('get detail html start')
    time.sleep(2)
    print('get detail html end')

# 2.通过集成Thread来实现多线程


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)


    def run(self):
        print(f'{self.name} get detail html start')
        time.sleep(2)
        print(f'{self.name} get detail html end')


if __name__ == '__main__':
    # thread1 = threading.Thread(target=get_detail_html, args=('www.baidu.com',))
    # thread2 = threading.Thread(target=get_detail_html, args=('www.sina.com',))
    # start_time = time.time()
    # thread1.start()
    # thread2.start()
    # thread1.join()
    # thread2.join()
    # end_time = time.time()
    # print(f'last time : {end_time - start_time}')

    thread1 = GetDetailUrl('thread1')
    thread2 = GetDetailUrl('thread2')
    start_time = time.time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    end_time = time.time()
    print(f'last time : {end_time - start_time}')

