from functools import reduce


def filter_func():
    return filter(lambda x: x % 3 == 0 and x % 5 == 0, [i for i in range(101)])


def reduce_func():
    def add(a, b):
        return a + b

    return reduce(add, filter(lambda x: x % 2 != 0, [i for i in range(101)]))


def map_func():
    return map(lambda x: x ** 3, filter(lambda x: x % 2 == 0, [i for i in range(101)]))


if __name__ == '__main__':
    print(list(filter_func()))
    print(reduce_func())
    print(list(map_func()))
