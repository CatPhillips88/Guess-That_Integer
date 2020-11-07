import random

guess = random.randint(1,10)

attempted_guesses = 0

while attempted_guesses < 5:
   num_guess = int(input('\nPick a number... '))

   if num_guess == 1001:
       message = input('Would you like to exit game? ')
       if message == 'yes':
           print('\nSORRY TO SEE YOU LEAVE! SEE YOU NEXT TIME ON GUESS THAT INTEGER!')
           break
       elif message == 'no':
           num_guess = int(input('Please continue to pick a number... '))

   if num_guess > 10 and num_guess != guess:
       print('SORRY, GUESS ONLY NUMBERS BETWEEN 1 AND 10!')
   elif num_guess != guess and num_guess > guess:
       print('GUESS AGAIN, GO LOWER!')
       attempted_guesses += 1
       print(f'CURRENT GUESS: {attempted_guesses}')
   elif num_guess != guess and num_guess < guess:
       print('GUESS AGAIN, GO HIGHER!')
       attempted_guesses += 1
       print(f'CURRENT GUESS: {attempted_guesses}')
   elif num_guess == guess:
       print('YOU\'VE GUESSED CORRECTLY!')
       attempted_guesses += 1
       print(f'CURRENT GUESS: {attempted_guesses}')
       break

if num_guess != guess and attempted_guesses == 5:
    print('\nBETTER LUCK NEXT TIME ON GUESS THAT INTEGER!')


print(F'TOTAL GUESSES: {attempted_guesses}')