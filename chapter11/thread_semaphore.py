# -*- coding: utf-8 -*-

# Semaphore 是用于控制进入数量的锁
# 文件 读和写，写一半只用于一个线程写，读可以允许多个

# 做爬虫，控制并发数
import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super(HtmlSpider, self).__init__()
        self.url = url
        self.sem = sem # type: threading.Semaphore

    def run(self):

        time.sleep(2)
        print('got html text success')
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super(UrlProducer, self).__init__()
        self.sem = sem
    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider(f'http://www.baidu.com/{i}', self.sem)
            html_thread.start()



if __name__ == '__main__':
    sem = threading.Semaphore(4)
    url_producer = UrlProducer(sem)
    url_producer.start()