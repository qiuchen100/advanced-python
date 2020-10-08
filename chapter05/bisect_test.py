# -*- coding: utf-8 -*-
import bisect

# 用来处理已经排序的序列,用来维持已排序的序列，生序
# 二分查找

inter_list = []
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)
print(inter_list)