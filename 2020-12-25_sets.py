def set_a():
    return set("We're gonna need a bigger boat.")


def set_b():
    return set("I'm sorry, Dave. I'm afraid I can't do that.")


if __name__ == '__main__':
    set_1 = set_a()
    set_2 = set_b()
    print(set_1)
    print(sorted(set_2))

    # only in set 1
    print(set_1 - set_2)
    # in set 1, in set 2 and in both
    print(set_1 | set_2)
    # in both sets only
    print(set_1 & set_2)
    # in set 1 or in set 2 but not in both
    print(set_1 ^ set_2)