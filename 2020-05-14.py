def ternary_operator():
    hungry = True
    x = 'Feed the bear now!' if hungry else 'Do not feed the bear.'
    print(x)


def arithmetic_operators():
    x = 10
    y = 3
    z = x / y
    print(f'result is {z}')

    z = x // y
    print('integer division result: {}'.format(z))

    z = x % y
    print('remainder: ' + f'{z}')


def binary_operators():
    x = 45
    print(f'{x:08b}')
    print(f'{x:02x}')


if __name__ == '__main__':
    ternary_operator()
    arithmetic_operators()
    binary_operators()
