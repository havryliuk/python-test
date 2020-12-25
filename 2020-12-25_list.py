def my_list():
    return range(10)


if __name__ == '__main__':
    for i in my_list():
        print(i, end=' ')
    print()

    another_sequence = [x * 2 for x in my_list()]
    print(another_sequence)

    seq3 = [x for x in my_list() if x % 3 != 0]
    print(seq3)

    tuple1 = [(x, x**2) for x in my_list()]
    print(tuple1)

    dict_1 = {x: x**3 for x in my_list()}
    print(dict_1)
