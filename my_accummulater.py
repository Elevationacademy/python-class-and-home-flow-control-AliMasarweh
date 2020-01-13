import operator
from itertools import accumulate


def my_accumulate(obj):
    accumulater = obj[0]
    for i in range(len(obj)):
        if i != 0:
            accumulater += obj[i]

        yield accumulater


if __name__ == '__main__':
    lst = ['Ali', 'xyz', 'lel']
    string = 'Ali Masa'
    tup = (123, 532, 1212, 91023, 121)

    for accumulated in my_accumulate(lst):
        print(accumulated)

    for accumulated in my_accumulate(string):
        print(accumulated)

    for accumulated in my_accumulate(tup):
        print(accumulated)

    '''
    Ali
    Alixyz
    Alixyzlel
    A
    Al
    Ali
    Ali 
    Ali M
    Ali Ma
    Ali Mas
    Ali Masa
    123
    655
    1867
    92890
    93011
    '''