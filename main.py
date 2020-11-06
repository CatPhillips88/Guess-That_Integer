import random

guess = random.randint(1,10)

attempted_guesses = 0

num_guess = int(input('Pick a number... '))

while attempted_guesses < 5:
   if num_guess == guess:
    print('You\'ve guessed correctly!')
    attempted_guesses += 1
    print(attempted_guesses)
   else:
    print('Guess Again!')
    attempted_guesses += 1
    print(attempted_guesses)