import random

print('Hello! What\'s your name?')
name = input()
number = random.randint(1, 100)
print(name + ', guess the number from 1 to 100.')
print('You have only 5 attempts...')
print()

attempt = 1
for attempt in range(1, 6):
    print(str(attempt) + '. Take a guess:', end=' ')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('The number is larger.')
    if guess > number:
        print('The number is smaller.')
    if guess == number:
        break

if guess == number:
    print('\nGood job! You have guessed number \'' + str(number) + '\' in ' + str(attempt) + ' attempts.')
if guess != number:
    print('\nYou haven\'t guessed. My number is ' + str(number) + '.')
