def while_loop():
    secret = 'Swordfish'
    guess = ''

    while guess.lower() != secret.lower():
        guess = input("What's the secret word? ")


def for_loop():
    animals = ('bear', 'bunny', 'dog', 'cat', 'cow')
    for animal in animals:
        print(animal, sep=' ')

    for number in range(5, 10):
        print(number)


def additional_controls():
    password = 'juswenko'
    guess = ''
    auth = False
    attempt = 1
    max_attempts = 5

    while guess != password:
        if attempt > max_attempts:
            break
        guess = input(f"{attempt}: Enter the password: ")
        attempt += 1
    else:
        auth = True

    print("Authorised" if auth else "Permission denied")


if __name__ == '__main__':
    while_loop()
    for_loop()
    additional_controls()
