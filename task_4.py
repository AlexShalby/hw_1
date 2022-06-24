def bananas(s) -> set:
    result = set()
    banana = ''
    len_s = len(s)
    index = 0

    for _, sym in enumerate('banana'):
        if sym == s[index]:
            banana += sym
            index += 1
        else:
            banana += '-'
            index += 1
    print(banana)
    return result


if __name__ == '__main__':
    bananas("bbanana")
    # assert bananas("banann") == set()
    # assert bananas("banana") == {"banana"}
    # assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
    #                                 "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
    #                                 "-ban--ana", "b-anana--"}
    # assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    # assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
