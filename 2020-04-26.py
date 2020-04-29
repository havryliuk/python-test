import platform


# main function (comment :))
def main():
    print_version()


def print_version():
    message = 'Python version is {}'
    version = platform.python_version()
    print(message.format(version))


if __name__ == '__main__':
    main()
