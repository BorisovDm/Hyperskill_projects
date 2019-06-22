"""
Project: Hangman
Stage #6: Victory!

Add the victory condition
The recent version of the game is not as fun until we don't handle the player's victory.
A player wins when all the letters are guessed and there are still some tries left
(except the player uses his last try and actually guesses the word, he's lucky then!).

Notice that, in the previous stage, the user has only 8 attempts to guess letters.
The number of attempts was decreasing despite the fact that the user guessed one of the hidden letters in the word!
It needs to be changed - now the number of attempts should decrease only if there are no words to uncover.
And yes, if the word to guess is -a-a at the moment and the user printed a you should count this as a fail
and reduce the number of attempts by 1 (later we'll fix it in favor of the user).

Print No such letter in the word if the word guessed by the program doesn't contain this letter.

Print No improvements if the guessed word contains this letter but the user tried this letter before.

Input and output example
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

-a-a---ip-
Input a letter: p
No improvements

-a-a---ip-
Input a letter: h
No such letter in the word

-a-a---ip-
Input a letter: k
No such letter in the word
You are hanged!


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
Input a letter: a

ja-a
Input a letter: v

java
You guessed the word!
You survived!
"""


import random
from collections import defaultdict


n_attempts = 8
game_dictionary = ['python', 'java', 'kotlin', 'javascript']
correct_word = random.choice(game_dictionary)
current_word = ['-'] * len(correct_word)
entered_letters = set()

letter_positions = defaultdict(list)
for idx, _letter in enumerate(correct_word):
    letter_positions[_letter].append(idx)

print('H A N G M A N')

while n_attempts > 0:
    print('\n', ''.join(current_word), sep='')
    letter = input('Input a letter:').strip()

    assert len(letter) == 1

    if letter in letter_positions:
        if letter in entered_letters:
            print('No improvements')
            n_attempts -= 1
            continue

        entered_letters.add(letter)

        for idx in letter_positions[letter]:
            current_word[idx] = letter

        if ''.join(current_word) == correct_word:
            print()
            print(correct_word)
            print('You guessed the word!\nYou survived!')
            break

    else:
        print('No such letter in the word')
        n_attempts -= 1

else:
    print('You are hanged!')
