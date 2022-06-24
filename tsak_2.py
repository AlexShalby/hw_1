def int32_to_ip(int32):
    Y1 = int32 // 256 ** 3
    Y2 = (int32 - Y1 * 256 ** 3) // 256 ** 2
    Y3 = (int32 - Y1 * 256 ** 3 - Y2 * 256 ** 2) // 256
    Y4 = int32 - Y1 * 256 ** 3 - Y2 * 256 ** 2 - Y3 * 256

    return f'{Y1}.{Y2}.{Y3}.{Y4}'


if __name__ == '__main__':
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"