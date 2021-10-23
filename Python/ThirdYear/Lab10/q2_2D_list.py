# Lab 10 Q2

import random


def gen_list():
    outer_list = []
    for i in range(10):
        inner_list = []
        for j in range(10):
            inner_list.append(random.randint(1, 100))
        outer_list.append(random.randint(1, 100))
    print(outer_list, inner_list)
    return outer_list


def main():
    outer_list = gen_list()
    print(outer_list[6])


main()
