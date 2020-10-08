# -*- coding: utf-8 -*-
import random


def get_random_words(length = 100):
    all_char = '0123456789qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJIKOLP'
    index = len(all_char) - 1
    words_length = random.randint(length / 2, length)

    words = [all_char[random.randint(0, index)] for _ in range(words_length)]
    word_str = ''.join(words) + '{|}'
    return word_str

def my_readlines(f, split):
    buf = ''
    while True:
        while split in buf:
            pos = buf.index(split)
            yield buf[:pos]
            buf = buf[pos + len(split):]
        chunk = f.read(4096*10)
        if not chunk:
            yield buf
            break
        buf += chunk

def my_read(f, size):
    while True:
        chunk = f.read(size * 10)
        if not chunk:
            break
        yield chunk

if __name__ == '__main__':
    # with open('input.txt', 'a+') as f:
    #     for i in range(1500):
    #         word = get_random_words()
    #         f.write(word)
    with open('input.txt') as f:
        for line in my_read(f, 512):
            print(line)