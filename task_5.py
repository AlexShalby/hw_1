def count_find_num(primesL, limit):
    list_fist = []
    list_num = []
    mul = multiply(primesL)
    if mul <= limit:
        list_fist += [multiply(primesL)]
        for i in range(10000):
            if mul * multiply(primesL) <= limit:
                list_fist += [multiply(primesL) * mul]
                mul *= multiply(primesL)
            else:
                break
    else:
        return []

    iter = 1

    for elem in primesL:
        mul = multiply(primesL)
        while True:
            if mul * elem <= limit:
                list_fist += [mul * elem]
                mul *= elem
                iter += 1
            else:
                break

    for el in list_fist:
        for elem in primesL:
            for power in range(iter + 1):
                if el * (elem ** power) <= limit:
                    list_num += [el * (elem ** power)]

    return [len(list(set(list_num + list_fist))), max(list_num)]


def multiply(lst):
    answer = 1
    for i in lst:
        answer *= i
    return answer


if __name__ == '__main__':
    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]

    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]

    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []
