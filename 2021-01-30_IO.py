def print_file():
    f = open('lines.txt', 'r')
    print(type(f))
    for line in f:
        print(line.rstrip())


def copy_file():
    infile = open('lines.txt', 'rt')
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        outfile.writelines(line)
#        print(line.rstrip(), file=outfile)
        print('.', end="", flush=True)
    outfile.close()
    print('\nDONE')


def copy_binary_file():
    infile = open('berlin.jpg', 'rb')
    outfile = open('berlin_copy.jpg', 'wb')
    while True:
        buffer = infile.read(10240)
        if buffer:
            outfile.write(buffer)
            print('.', end='', flush=True)
        else:
            break
    outfile.close()
    print('\nDone.')


if __name__ == '__main__':
    print_file()
    copy_file()
    copy_binary_file()
