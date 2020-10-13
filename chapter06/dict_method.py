# -*- coding:utf-8 -*-
a = {'qq1': {'company': 'xxx1'},
     'qq2': {'company': 'xxx2'},
     }

# print(a)
# # 清空
# a.clear()
# print(a)

# 浅拷贝
new_dict = a.copy()
new_dict['qq1']['company'] = 'yyy1'
print(new_dict['qq1']['company'])
print(a['qq1']['company'])
print(id(a['qq2']))
print(id(new_dict['qq2']))

# 深拷贝
import copy
new_dict = copy.deepcopy(a)
new_dict['qq1']['company'] = 'zzz1'
print(new_dict['qq1']['company'])
print(a['qq1']['company'])
print(id(a['qq2']))
print(id(new_dict['qq2']))

# fromkeys
l = ['huashi', 'wuda', 'hanyang', 'wuda']
new_dict = dict.fromkeys(l, 999)
print(new_dict)

# get
print(new_dict.get('wud', 888))

for k, v in new_dict.items():
    print(k, v)

# setdefault 没有就添加进去
d = new_dict.setdefault('asima', 777)
print(new_dict, d)
d = new_dict.setdefault('wuda', 777)
print(new_dict, d)
d = new_dict.setdefault('qq1', 777)
print(new_dict, d)
new_dict.update(a)
print(new_dict)

new_dict.update(hanyang=30,qq6=True)
print(new_dict)

new_dict.update([('xxx', 22), ('ww', 0)])
print(new_dict)