# -*- coding: utf-8 -*-

import asyncio
from urllib.parse import urlparse
import time


async def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = '/' if url.path == '' else url.path

    # 建立socket连接
    reader, writer = await asyncio.open_connection(host, 80)
    writer.write(f'GET {path} HTTP/1.1\r\nHost:{host}\r\nConnection:close\r\n\r\n'.encode('utf8'))
    lines = []
    async for raw_line in reader:
        line = raw_line.decode('utf8')
        lines.append(line)
    data = '\n'.join(lines)
    html_data = data.split('\r\n\r\n')
    return html_data

    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.connect((host, 80))
    # client.send(f'GET {path} HTTP/1.1\r\nHost:{host}\r\nConnection:close'
    #             f'\r\n\r\n'.encode('utf8'))

    # data = b''
    # while True:
    #     try:
    #         d = client.recv(1024)
    #     except BlockingIOError as e:
    #         continue
    #     if d:
    #         data += d
    #     else:
    #         break
    #
    # data = data.decode('utf8')
    # html_data = data.split('\r\n\r\n')[1]
    # print(html_data)
    # client.close()


async def main():
    url_template = 'http://shop.projectsedu.com/goods/{}/'
    urls = list(url_template.format(i) for i in range(1, 20))
    tasks = []
    for url in urls:
        # task = loop.create_task(get_url(url))
        task = asyncio.ensure_future(get_url(url))
        tasks.append(task)
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    start_time = time.time()
    loop.run_until_complete(main())
    print(time.time() - start_time)
