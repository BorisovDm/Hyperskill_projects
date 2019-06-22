"""
Project: Hangman
Stage #5: Letter by letter

Letter by letter
Let's make the game iterative. It's time to make it resemble the classical Hangman a bit more: a player should guess letters in the word instead of typing the entire word at once. If the player guesses a letter, it should be uncovered in the word. For now, start with the defeat case and add 8 tries to guess a letter that appears in the word. When the player runs out of attempts, the game ends.

Input and output example
A player should have 8 tries and enter letters. If the letter doesn't occur in the word, the computer takes one try away, even if the user already inputted this letter before. If the player doesn't have any more attempts, the game should end and the program should show a losing message. Otherwise, the player can continue to input letters.

Notice that if a player has more tries but he actually guessed the word, it doesn't mean anything. Determining the winning conditions will be in the next stage, in this stage you should print how well user guesses the word on every user attempt to input a letter. Try to match your input with the example below (it is important for testing to print a new line before printing guessed letters).

Also, use the following word list: 'python', 'java', 'kotlin', 'javascript' so your program can be tested more reliably.


H A N G M A N

----------
Input a letter: a

-a-a------
Input a letter: i

-a-a---i--
Input a letter: o
No such letter in the word

-a-a---i--
Input a letter: o
No such letter in the word

-a-a---i--
Input a letter: p
No such letter in the word

-a-a---ip-
Input a letter: p

-a-a---ip-
Input a letter: h
No such letter in the word

-a-a---ip-
Input a letter: k
No such letter in the word

Thanks for playing!
We'll see how well you did in the next stage


H A N G M A N

----
Input a letter: j

j---
Input a letter: i
No such letter in the word

j---
Input a letter: g
No such letter in the word

j---
Input a letter: o
No such letter in the word

j---
Input a letter: a

ja-a
Input a letter: v

java
Input a letter: a

java
Input a letter: j

Thanks for playing!
We'll see how well you did in the next stage


"""


# import random
# from collections import defaultdict
#
#
# n_attempts = 8
# game_dictionary = ['python', 'java', 'kotlin', 'javascript']
# correct_word = random.choice(game_dictionary)
# current_word = ['-'] * len(correct_word)
#
# letter_mapping = defaultdict(list)
# for idx, symbol in enumerate(correct_word):
#     letter_mapping[symbol].append(idx)
#
# print('H A N G M A N')
#
# for _ in range(n_attempts):
#     print(''.join(current_word))
#     letter = input('Input a letter:').strip()
#
#     assert len(letter) == 1
#     if letter in letter_mapping:
#         for idx in letter_mapping[letter]:
#             current_word[idx] = letter
#     else:
#         print('No such letter in the word')
#
#     # print()
#
# print('Thanks for playing!')
# print("We'll see how well you did in the next stage", end='')


import random
from collections import defaultdict


n_attempts = 8
game_dictionary = ['python', 'java', 'kotlin', 'javascript']
correct_word = random.choice(game_dictionary)
current_word = ['-'] * len(correct_word)

letter_mapping = defaultdict(list)
for idx, symbol in enumerate(correct_word):
    letter_mapping[symbol].append(idx)

print('H A N G M A N')

for _ in range(n_attempts):
    print()
    print(''.join(current_word))
    letter = input('Input a letter:').strip()

    assert len(letter) == 1
    if letter in letter_mapping:
        for idx in letter_mapping[letter]:
            current_word[idx] = letter
    else:
        print('No such letter in the word')

print('Thanks for playing!')
print("We'll see how well you did in the next stage")
