# -*- coding: utf-8 -*-

# 提取0-20之间的奇数
odd_list = [i for i in range(20) if i % 2 == 1]
print(odd_list)

# 列表推导式性能高于列表操作
odd_list = [i * i for i in range(20) if i % 2 == 1]
print(odd_list)

# 生成器表达式
odd_list = (i * i for i in range(20) if i % 2 == 1)
print(type(odd_list))
for o in odd_list:
    print(o)


# 字典推导式
my_dict = {'num'+str(i) : i * i for i in range(20) if i % 2 == 1}
print(my_dict)

# 集合推导式
my_set = {'num'+str(i) for i in range(20) if i % 2 == 1}
print(my_set)