from decimal import *


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
    l = [1, 'a', 3, 4]
    l[1] = 'b'
    print(l)

    tuple = (1, 'a', 3, 4)
    print(tuple)


    print(range(10), end=" ")
    print(range(5, 11), end=" ")
    print(range(70, 90, 10), end=" ")


if __name__ == '__main__':
    if_function()
    for_function(['one', 'two', 'three', 'four', 'five'])

    s = str('new string {}').upper().format('arg')
    print(s)

    numbers()
    booleans()
    sequences()
