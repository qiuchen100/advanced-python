# -*- coding:utf-8 -*-
# 1.epoll并不是比select好
# 在并发很高的时候，连接活跃度并不是很高，epoll比select好
# 并发性不高，同时连接很活跃，select比epoll好