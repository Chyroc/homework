def gcdIter(a, b):
    if a > b:
        max = a
        min = b
    else:
        max = b
        min = a

    while True:
        temp = max % min
        if temp == 0:
            return min

        if temp > min:
            max = temp
        else:
            max = min
            min = temp


def gcdRecur(a, b):
    if a < b:
        a, b = b, a

    temp = a % b
    if temp == 0:
        return b

    return gcdRecur(temp, b)


if __name__ == '__main__':
    for i in [[2, 12], [6, 12], [9, 12], [17, 12]]:
        print(gcdIter(i[0], i[1]))
        print(gcdRecur(i[0], i[1]))
