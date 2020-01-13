def is_fuzz(num):
    if num % 3 == 0:
        return 'fuzz'
    return ''


def is_buzz(num):
    if num % 5 == 0:
        return 'buzz'
    return ''


def fuzz_buzz(num):
    for i in range(num + 1):
        x = is_fuzz(i) + is_buzz(i) or i
        print(x)


if __name__ == '__main__':
    fuzz_buzz(30)
