class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)

    def name(self):
        return self._name

    def age(self):
        return self._age


class AnotherDuck:
    def __init__(self, **kwargs):
        self._name = kwargs['name']
        self._age = kwargs['age']

    def name(self, n=None):
        if n:
            self._name = n
        try:
            return self._name
        except AttributeError:
            return None

    def age(self, a=None):
        if a:
            self._age = a
        try:
            return self._age
        except AttributeError:
            return None

    def __str__(self):
        return f'Duck {self._name} is {self._age} years old.'

    def __eq__(self, other):
        if isinstance(other, AnotherDuck):
            return self._age == other._age and self._name == other._name
        return False


def print_duck(o):
    print(f'Duck {o.name()} is {o.age()} years old.')


if __name__ == '__main__':
    duck = Duck('Donald', 13)
    duck.quack()
    duck.move()
    print_duck(duck)

    print_duck(Duck('Sasha', 37))

    print(AnotherDuck(name='Leo', age=2))
    print(AnotherDuck(name='Dandy', age=33))

    anotherDuck = AnotherDuck(name='Moss', age=32)
    anotherDuck.name('Mickey')
    anotherDuck.age(5)
    print(anotherDuck)
