def my_list():
    return ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']


def tuple_exercise():
    my_tuple = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')
    print(my_tuple)


if __name__ == '__main__':
    for i in my_list():
        print(i, end=' ')
    print()

    print(my_list()[1:5:3])
    print(my_list().index('Scissors'))

    another_list = my_list()
    another_list.insert(1, 'Computer')
    another_list.remove('Paper')
    another_list.append('Paper')
    print(len(another_list))
    removed = another_list.pop()
    another_list.pop(1)
    del another_list[1:3]
    print(', '.join(another_list))
    print(removed)

    tuple_exercise()
