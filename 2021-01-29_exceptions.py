def exceptions():
    string = 'foo'
    try:
        x = int(string)
        y = 5/0
    except ValueError as e:
        print(f'Cannot parse \'{string}\' into an integer\n(message: {e})')
    except:
        raise TypeError("Something went wrong!")
    else:
        print(f'{x} and {y}')


if __name__ == '__main__':
    exceptions()
