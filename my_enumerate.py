def my_enumerate(obj):
    for i in range(len(obj)):
        yield i, obj[i]


if __name__ == '__main__':
    lst = ['Ali', 'xyz', 'lel']
    string = 'Ali Masa'
    tup = (123, 532, 1212, 91023, 121, 'asd')

    for i, item in my_enumerate(lst):
        print(i, item)

    for i, item in my_enumerate(string):
        print(i, item)

    for i, item in my_enumerate(tup):
        print(i, item)