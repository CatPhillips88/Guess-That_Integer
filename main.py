import random

guess = random.randint(1,10)

num_guess = int(input('Pick a number... '))

if num_guess == guess:
    print('You\'ve guessed correctly!')
else:
    print('Guess Again!')