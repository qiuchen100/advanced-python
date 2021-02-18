# -*- coding: utf-8 -*-


import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
# windows上默认选择select linux上默认epoll

# 使用select完成http请求

selector = DefaultSelector()
url_template = 'http://shop.projectsedu.com/goods/{}/'
urls = list(url_template.format(i) for i in range(1, 20))


class Fetcher:
    def __init__(self, url):
        self.url = url
        url = urlparse(self.url)
        self.path = '/' if url.path == '' else url.path
        self.host = url.netloc
        self.data = b''
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send(f'GET {self.path} HTTP/1.1\r\nHost:{self.host}\r\n'
                         f'Connection:close\r\n\r\n'.encode('utf8'))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            print('*' * 100)
            selector.unregister(key.fd)
            data = self.data.decode('utf8')
            html_data = data.split('\r\n\r\n')[1]
            print(html_data)
            # selector.unregister(key.fd)
            self.client.close()
            urls.remove(self.url)

    def get_url(self):
        # 通过socket请求html
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass
        # 注册
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    """事件循环，不停的请求socket的状态并调用对应的回调函数"""
    while urls:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)
    # 回调+事件循环


if __name__ == '__main__':
    import time
    start_time = time.time()
    for url in urls:
        Fetcher(url).get_url()
    loop()
    print(time.time() - start_time)

