x = '-47.5'
y = int(47)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')

z = float(x)
print(f'z is {type(z)}')
print(f'z is {z}')

a = abs(z)
print(f'a is {type(a)}')
print(f'a is {a}')

times, remainder = divmod(y, 3)
print(f'{y}/3 is {times} with remainder {remainder}')

complex_number = y + 73j
complex_number = complex(y, 73)
print(f'complex type is {type(complex_number)}')
print(f'complex number is {complex_number}')

s = 'Hello, World.'
print(repr(s))
print(ascii(s))

print(chr(128406))
print(ord('🖕'))

t = (1, 2, 3, 4, 5)
print(len(t))
for i in reversed(t):
    print(i, end=' ')
print(sum(t))
print(sum(t, 20))
print(max(t))
print(min(t))
print(any(t))
print(all(t))

t2 = (6, 7, 8, 9, 10)
for a, b in zip(t, t2):
    print(f'{a} - {b}')

animals = ('cat', 'dog', 'rabbit', 'cow')
for i, v in enumerate(animals):
    print(f'{i+1}: {v}')

print(isinstance(animals, tuple))
