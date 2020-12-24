def main():
    kitten()


def kitten(n='Leo'):
    print(f'{n} Meow')


def kitten_variable_length(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Empty arguments')


def kitten_keyword_args(**kwargs):
    if len(kwargs):
        for keyword in kwargs:
            print('Kitten {} says {}'.format(keyword, kwargs[keyword]))
    else:
        print("empty dictionary")


def generate_infinitely():
    num = 0
    while True:
        yield num
        num += 1


def f1():
    return 1


if __name__ == '__main__':
    main()
    kitten_variable_length()
    kitten_variable_length(2, 'Sasha')

    x = ('sasha', 'leo', 'wat?')
    kitten_variable_length(*x)

    dictionary = dict(Buffy='meow', Zilla='grr', Angel='rawr')
    kitten_keyword_args(**dictionary)

    # returns None
    print(type(kitten()))

    infinite_flow = generate_infinitely()
    i: int
    for i in infinite_flow:
        print(i)
        infinite_flow.close()
        # infinite_flow.throw(ValueError)

    x = f1
    print(x())
    print(type(x))
