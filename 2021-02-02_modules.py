import sys
import os
import random
import datetime

v = sys.version_info
print(v)
print('Python version {}.{}.{} {}'.format(*v))

print(sys.platform)
print(os.name)
print(os.getenv('PATH'))
print(os.getcwd())
print(os.urandom(15).hex())

print(random.randint(1, 10000))
m = list(range(15))
random.shuffle(m)
print(m)

print(datetime.datetime.now())
