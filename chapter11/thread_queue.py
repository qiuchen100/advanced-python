# -*- coding: utf-8 -*-
import time
import threading
from chapter11 import variables
import queue



def get_detail_html(queue):
    # 爬取文章详情页
    while True:
        if queue.empty():
            print('没抓到')
            time.sleep(3)
            continue
        url = queue.get()
        print(url)
        print('get detail html start')
        time.sleep(3)
        print('get detail html end')
        break

def get_detail_url(queue):
    # 爬取文章列表页
    print('get detail url start')
    for i in range(20):
        time.sleep(1)
        queue.put(f'http://projectedu.com/{i}')
    print('get detail url end')


if __name__ == '__main__':
    detail_url_queue = queue.Queue(maxsize=1000)

    item_thread = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    item_thread.start()
    detail_threads = []
    for i in range(10):
        detail_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        detail_thread.start()
        detail_threads.append(detail_thread)
    start_time = time.time()
    item_thread.join()
    for detail_thread in detail_threads:
        detail_thread.join()
    end_time = time.time()
    print(len(variables.detail_url_list))
    print(f'last time : {end_time - start_time}')


