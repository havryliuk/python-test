import platform


# main function (comment :))
def main():
    print_version()


def print_version():
    message = 'Python version is {}'
    version = platform.python_version()
    print(message.format(version))

    m = 'Python version is %d' % platform.python_version()
    print(m)

    name = 'Sasha'
    f_message = f'Hello world, {name}'
    print(f_message)


if __name__ == '__main__':
    main()
