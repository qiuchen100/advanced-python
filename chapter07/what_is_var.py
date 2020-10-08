# -*- coding: utf-8 -*-

#python和java中的变量本质不一样，python的变量实质上是一个指针，大小固定（便利贴）

a = 1
# 1. a贴在1上面
# 2. 先生成对象，然后贴便利贴
# 3. 在java中是先开辟一块内存空间（盒子），然后把对象放到盒子里

a = [1, 2, 3]
b = a
b.append(4)
print(b)
print(a is b)

print('-' * 50)

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
print(a == b)
print(a is b)

print('-' * 50)

a = 99900000
b = 99900000
print(a == b)
print(a is b)

print('-' * 50)

a = 'aabbcc'
b = 'aabbcc'
print(a == b)
print(a is b)