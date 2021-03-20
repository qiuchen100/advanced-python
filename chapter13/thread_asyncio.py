# -*- coding: utf-8 -*-

import asyncio
import concurrent
import socket
from urllib.parse import urlparse
import time

executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = '/' if url.path == '' else url.path

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))
    client.send(f'GET {path} HTTP/1.1\r\nHost:{host}\r\nConnection:close'
                f'\r\n\r\n'.encode('utf8'))

    data = b''
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    data = data.decode('utf8')
    html_data = data.split('\r\n\r\n')[1]
    print(html_data)
    client.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    url_template = 'http://shop.projectsedu.com/goods/{}/'
    urls = list(url_template.format(i) for i in range(1, 20))
    tasks = []
    start_time = time.time()
    for url in urls:
        task = loop.run_in_executor(executor, get_url, url)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start_time)

