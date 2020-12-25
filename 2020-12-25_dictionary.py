def dictionary():
    return {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr', 'giraffe': """I'm a giraffe!""", 'dragon': 'rawr'}


def constructor_dictionary():
    return dict(kitten='meow', puppy='ruff!', lion='grrr', giraffe="""I'm a giraffe!""", dragon='rawr')


if __name__ == '__main__':
    dictionary = dictionary()
    for animal in dictionary:
        print(f'{animal} says {dictionary[animal]}')

    print(dictionary)

    print(dictionary.items())
    print(dictionary.keys())
    print(dictionary.values())
    print(dictionary['lion'])
    print(dictionary.get('Sasha'))
    dictionary['lion'] = 'I am a lion'

    print('lion' in dictionary)
