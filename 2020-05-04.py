def practice_type_and_id() :
    new_map = {'a': 345, 'b': 489}
    second_map = {'a': 345, 'b': 489}

    print(new_map)
    print(type(new_map))

    print(id(new_map))
    print(id(second_map))

    print(id(new_map.get('a')))
    print(id(second_map.get('a')))

    first_value = new_map.get('a')
    second_value = second_map.get('a')
    if first_value is second_value:
        print('{} equals {}'.format(id(first_value), id(second_value)))

    if new_map.__eq__(second_value) and isinstance(new_map, dict):
        print('dicts are equal and first dict is a dict')


if __name__ == '__main__':
    practice_type_and_id()