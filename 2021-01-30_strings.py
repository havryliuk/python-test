
print('Hello, World'.swapcase())
print('Hello, World! {} {}'.format(42 * 7, 'AA'.lower()))
print("""
        Hello,
        World!
        
        {}""".format(1 == 2))


class MyString(str):
    def __str__(self):
        return self[::-1]


s = MyString('Hello, World!')
print(s)

print('sasha'.capitalize())
print('hello, natasha. how are you?'.title())

s1 = 'Hello, '
s2 = 'World!'
print(s1 + s2)

print('{0}: the numbers are {1:<9} and {0:>05}'.format(1, 43))
print('the numbers are {second:,} {first} and {first}'
      .format(first = 33, second = 1444354)
      .replace(',','.'))
print('the number is {:f}'.format(3))
print('the number is {:.2f}'.format(34))

print('{:x}'.format(3452))
print('{:o}'.format(15))
print('{:b}'.format(12))

x = 24532452
print(f'the number is {x}')

s3 = 'This is a long string with a bunch of words in it.'
s3_list = s3.split()
print(s3_list)
print(s3.split('i'))
print(' - '.join(s3_list))
