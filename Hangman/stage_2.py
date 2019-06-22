"""
Project: Hangman
Stage #2: Guess the word

Guess the word
At this stage, you will create a real game. It will be simple, but there will be two possible outcomes (you can see in the examples below how they look like). Let's first print a welcome message and then ask a player to guess the word we set for the game. If our player manages to guess the exact word, the game reports "win"; otherwise it will "hang" the player.

You should print You survived! if the user guessed the word and You are hanged! otherwise. By the way, the word python should be the correct word to win the game.

Input and output example
Example 1

H A N G M A N
Guess the word: python
You survived!

Example 2

H A N G M A N
Guess the word: java
You are hanged!
where Guess the word: is an input invitation message.
"""


print('H A N G M A N')
word = input('Guess the word:')
print('You survived!' if word == 'python' else 'You are hanged!')
