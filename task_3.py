def zeros(n):
    '''

    :param n: n < 5 ** 5
    '''
    zero = 0
    for i in range(n):
        if (i + 1) % 625 == 0:
            zero += 1
        if (i + 1) % 125 == 0:
            zero += 1
        if (i + 1) % 25 == 0:
            zero += 1
        if (i + 1) % 5 == 0:
            zero += 1
    return zero


if __name__ == '__main__':
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
    assert zeros(100) == 24
    assert zeros(1000) == 249
