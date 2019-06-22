"""
Project: Hangman
Stage #4: Guess a word with a hint

Guess a word with a hint
Now our game has become quite hard, and your chances of guessing the word depend on the size of the list.
In our case with four words, there is only a 25% chance, so let's have mercy on the player and add a hint for them.

Input and output example
As in the previous stage, you should use the following word list: 'python', 'java', 'kotlin', 'javascript'

Let the game show the first 3 letters after the computer chose a word from the list.
Hidden letters should be replaced with dashes ("-").

H A N G M A N
Guess the word jav-: java
You survived!

H A N G M A N
Guess the word pyt---: pytnoh
You are hanged!
"""


import random


game_dictionary = ['python', 'java', 'kotlin', 'javascript']
correct_word = random.choice(game_dictionary)
see_word = correct_word[:3] + '-' * (len(correct_word) - 3)

print('H A N G M A N')
word = input(f'Guess the word {see_word}:')
print('You survived!' if word == correct_word else 'You are hanged!')
