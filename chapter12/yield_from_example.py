# -*- coding: utf-8 -*-

final_result = {}


def sales_sum(prod_name):
    print(f'sales_sum: {prod_name}')
    total = 0
    nums = []
    while True:
        x = yield
        if not x:
            break
        print(f'{prod_name}的销量是: {x}')
        total += x
        nums.append(x)
    return total, nums


def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(f'{key}销量统计完成!')


def main():
    data_sets = {
        'Bobby牌面膜': [1200, 1500, 3000],
        'Kitty牌面膜': [800, 2800, 1900],
        'July牌面膜': [450, 900, 1200],
    }
    for key, dataset in data_sets.items():
        print(f'start key: {key}')
        m = middle(key)
        m.send(None)  # 预激middle协程
        for value in dataset:
            m.send(value)
        m.send(None)  # 发送None结束协程
        print(final_result)


if __name__ == '__main__':
    main()
