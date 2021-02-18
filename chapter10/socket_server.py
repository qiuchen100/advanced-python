# -*- coding: utf-8 -*-

import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 7300))
server.listen()


# 获取从客户端发送的数据
# data = sock.recv(1024)
# data_str = data.decode('utf8')
# print(data_str)
# sock.send(f'Hello, {data_str}!'.encode('utf8'))
# server.close()


def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode('utf8'))
        if data.decode('utf8') == 'bye':
            sock.send('bye bye'.encode('utf8'))
            sock.close()
            break
        re_data = input("请回复：")
        sock.send(re_data.encode('utf8'))


if __name__ == '__main__':
    while True:
        sock, addr = server.accept()
        client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
        client_thread.start()
        # threading.current_thread().setDaemon(True)
    # print('exit!')
    # server.close()
