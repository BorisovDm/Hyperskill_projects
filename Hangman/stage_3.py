"""
Project: Hangman
Stage #3: Guess a random word

Guess a random word
If there is a predefined word, the game isn't replayable: you already know the word, so it makes no sense to guess it. At this stage, let's make the game more challenging by choosing a word from a special list with a variety of options. This way, our game won't be just a one-time entertainment.

Input and output example
Using the following word list: 'python', 'java', 'kotlin', 'javascript' , program the game to choose a random word from it. You can enter more words, but let's stick to these four for now.

Example 1

H A N G M A N
Guess the word: python
You survived!
In case the computer randomly chose python from the list.

Example 2

H A N G M A N
Guess the word: python
You are hanged!
In case the computer randomly chose something other than python from the list.

Example 3

H A N G M A N
Guess the word: C#
You are hanged!
"""


import random


game_dictionary = ['python', 'java', 'kotlin', 'javascript']
correct_word = random.choice(game_dictionary)

print('H A N G M A N')
word = input('Guess the word:')
print('You survived!' if word == correct_word else 'You are hanged!')
