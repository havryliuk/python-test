class Animal:
    def __init__(self, **kwargs):
        if 'type' in kwargs:
            self._type = kwargs['type']
        if 'name' in kwargs:
            self._name = kwargs['name']
        if 'sound' in kwargs:
            self._sound = kwargs['sound']

    def type(self, t=None):
        if t:
            self._type = t
        try:
            return self._type
        except AttributeError:
            return None

    def name(self, n=None):
        if n:
            self._name = n
        try:
            return self._type
        except AttributeError:
            return None

    def sound(self, s=None):
        if s:
            self._sound = s
        try:
            return self._sound
        except AttributeError:
            return None

    def __str__(self):
        return f'The {self.type()} is named {self._name} and says "{self.sound()}"'


class Duck(Animal):
    def __init__(self, **kwargs):
        self._type = 'duck'
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)


class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)

    def kill(self, s):
        print(f'{self.name()} will kill {s}!')


class ReverseString(str):
    def __str__(self):
        return self[::-1]


if __name__ == '__main__':
    kitten = Kitten(name='Fluffy', sound='meow')
    duck = Duck(name='Donald', sound='quack')
    print(kitten)
    print(duck)

    kitten.kill('humans')

    print(ReverseString('Hello, World!'))
