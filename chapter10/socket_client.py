# -*- coding: utf-8 -*-

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 7300))
# client.send('ttttt'.encode('utf8'))
# data = client.recv(1024)
# print(data.decode('utf8'))
# client.close()
while True:
    re_data = input("请输入指令：")
    client.send(re_data.encode('utf8'))
    data = client.recv(1024)
    print(data.decode('utf8'))
    if re_data == 'bye':
        break

client.close()
