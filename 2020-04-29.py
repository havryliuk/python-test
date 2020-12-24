from decimal import Decimal


def if_function():
    x = 42
    y = 73

    if x > y:
        print(f'x < y: x is {x} and y is {y}.')
    elif x < y:
        print('inside {} block'.format('elif'))
    else:
        print('inside else block')
    print('outside if clause')


def for_function(words=None):
    if words is None:
        words = []
    for word in words:
        print(word, end=' ')
        print(type(word))


def numbers():
    print(f'37 / 12 = {37 / 12}')

    f = 3.2
    print(f)
    print(type(f))

    a = Decimal('.10')
    b = Decimal('.30')
    print('Decimal: 0.1 + 0.1 + 0.1 - 0.3 = {}'.format(a+a+a-b))
    print('Float: 0.1 + 0.1 + 0.1 - 0.3 = {}'.format(.1 + .1 + .1 - .3))


def booleans():
    t = True
    print(t)
    print(type(t))


def sequences():
    my_list = [1, 'a', 3, 4]
    my_list[1] = 'b'
    print(my_list)

    my_tuple = (1, 'a', 3, 4)
    print(my_tuple)

    range_10 = range(10)
    for x in range_10:
        print(x, end=" ")
    print()

    range_5_11 = range(5, 11)
    for x in range_5_11:
        print(x, end=" ")
    print()

    range_70_91_step_9 = range(70, 91, 9)
    for x in range_70_91_step_9:
        print(x, end=" ")
    print()


if __name__ == '__main__':
    if_function()
    for_function(['one', 'two', 'three', 'four', 'five'])

    s = str('new string {}').upper().format('arg')
    print(s)

    numbers()
    booleans()
    sequences()
