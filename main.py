import random

guess = random.randint(1,10)

attempted_guesses = 0

while attempted_guesses < 5:
   num_guess = int(input('Pick a number... '))

   if num_guess != guess and num_guess > guess:
       print('GUESS AGAIN, GO LOWER!')
       attempted_guesses += 1
       print(attempted_guesses)
   elif num_guess != guess and num_guess < guess:
       print('GUESS AGAIN, GO HIGHER')
       attempted_guesses += 1
       print(attempted_guesses)
   elif num_guess == guess:
       print('YOU\'VE GUESSED CORRECTLY')
       attempted_guesses += 1
       print(attempted_guesses)
