def check_prime_number(x):
    if x == 1:
        return False
    elif x == 2:
        return True

    for i in range(2, x):
        if x % i == 0:
            return False

    return True


if __name__ == '__main__':
    for i in range(1, 101):
        if check_prime_number(i):
            print(i)
