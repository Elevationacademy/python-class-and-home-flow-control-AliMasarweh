import random

lower_characters_lst = list('abcdefghijklmnopuvwxyz')
upper_characters_lst = list('abcdefghijklmnopuvwxyz'.upper())
numbers_lst = list('0123456789')


def count_lower(string: str):
    return len(list(filter(str.islower, string)))


def count_upper(string: str):
    return len(list(filter(str.isupper, string)))


def has_a_number(string: str):
    for i in range(10):
        if str.count(str(i)):
            return True

    return False


def len_min_max(string: str, min, max):
    return min < len(string) < max


def validate(password: str):
    return count_lower(password) >= 4 and count_upper(password) >= 2 \
           and has_a_number(password) and len_min_max(8, 20)


def generate_random_valid_password():
    lenght = random.randint(8, 20)
    num_of_lowers = random.randint(4, lenght // 2)

    lenght -= num_of_lowers
    num_of_uppers = random.randint(2, lenght // 2)

    lenght -= num_of_uppers
    num_of_numbers = lenght

    password = random.sample(lower_characters_lst, num_of_lowers)
    password += random.sample(upper_characters_lst, num_of_uppers)
    password += random.sample(numbers_lst, num_of_numbers)

    random.shuffle(password)
    return password


if __name__ == '__main__':
    lst = list('abcdefghijklmnopuvwxyz')
    print(lst)
    samples = random.sample(lst, 10)
    print(samples)
    random.shuffle(samples)
    print(samples)
    random.shuffle(samples)
    print(samples)
