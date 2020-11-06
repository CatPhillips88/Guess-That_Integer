import random

guess = random.randint(1,10)

# The variable 'num_guess' assigns an input which prompts players to enter an integer.
# A conditional test via an if statement, tests whether the user input matches a random number generated in the variable
# 'guess'.

# If the condition is met via a true boolean value then a message prints to terminal, otherwise the user will be asked
# pick another number.
# The if statement is nested in a while loop to execute as long as the attempted guesses are less than 5. The default
# attempts have been set to default number - 0. Upon each input, 1 point should be added to attempted guesses value
# until a game is won or attempted guesses have exceeded after 5 tries rendering a false boolean value.

# First Attempt: Condition works, however 1 input is looped over 5 times as matching guess.
# The goal is to prompt players to pick another number within 5 attempts, if not guessed the matched number the
# first time.

num_guess = int(input('Pick a number... '))
attempted_guesses = 0

while attempted_guesses < 5:
   if num_guess == guess:
    print('You\'ve guessed correctly!')
    attempted_guesses += 1
    print(attempted_guesses)
   else:
    print('Guess Again!')
    attempted_guesses += 1
    print(attempted_guesses)