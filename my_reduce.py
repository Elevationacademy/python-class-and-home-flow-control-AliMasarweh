from functools import reduce


def my_reduce(func, seq, initial_val=None):
    it = iter(seq)
    if initial_val is None:
        ret = next(it)
    else:
        ret = initial_val
    for element in it:
        ret = func(ret, element)
    return ret


def plus(a, b):
    f = 0.1
    num = 2
    string = ''
    if type(a) == type(f) or type(a) == type(num) \
            or type(a) == type(string):
        return a + b
    return a.append(b)


if __name__ == '__main__':
    lst = ['Ali', 'xyz', 'lel']
    string = 'Ali Masa'
    ints = list([123, 532, 1212, 91023, 121])

    reduced = reduce(plus, lst, '')
    print(reduced)

    reduced = reduce(plus, string, '')
    print(reduced)

    reduced = my_reduce(plus, ints, 0)
    print(reduced)


