class Cat:

    def meow(self):
        m = 'M'
        print(f'{m:<5}eoooow...')

    def sleep(self):
        print('Kitty is sleeping... zzz')


if __name__ == '__main__':
    cat = Cat()
    cat.meow()
    cat.sleep()
    print(type(cat))
