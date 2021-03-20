# -*- coding:utf-8 -*-
# 1.epoll并不是比select好
# 在并发很高的时候，连接活跃度并不是很高，epoll比select好
# 并发性不高，同时连接很活跃，select比epoll好

# 通过非阻塞IO来实现

import socket
from urllib.parse import urlparse
import time

def get_url(url):
    #通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = '/' if url.path == '' else url.path

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, 80))
    except BlockingIOError as e:
        pass

    while True:
        try:
            client.send(f'GET {path} HTTP/1.1\r\nHost:{host}\r\nConnection:close'
                        f'\r\n\r\n'.encode('utf8'))
            break
        except OSError as e:
            pass

    data = b''
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break

    data = data.decode('utf8')
    html_data = data.split('\r\n\r\n')[1]
    print(html_data)
    client.close()


if __name__ == '__main__':
    get_url('http://www.baidu.com')
