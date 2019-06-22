"""
Project: Hangman
Stage #7: Polishing the gameplay

Polishing the gameplay
Now that we are done with the basics, let's work on some details.

Notice that in the previous stage if the user entered the same letter twice
the program always reduces the number of attempts - regardless if this was a correct letter or not.
But it is not fair to the user, isn't it?
He gains no additional information about the situation on the field yet the program still reduces his attempts count.
This time if the user enters the same letter twice then the program should output You already typed this letter.

Also, you should check is the user print English lowercase letter or not.
If not, the program should print It is not an ASCII lowercase letter.

Also, you should check if the user printed exactly one letter.
If not, the program should print You should print a single letter.
Remember that zero is also not one!

Note, that all these three errors should not reduce attempts count.

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
You already typed this letter

-a-a---i--
Input a letter: p

-a-a---ip-
Input a letter: p
You already typed this letter

-a-a---ip-
Input a letter: h
No such letter in the word

-a-a---ip-
Input a letter: k
No such letter in the word

-a-a---ip-
Input a letter: a
You already typed this letter

-a-a---ip-
Input a letter: z
No such letter in the word

-a-a---ipt
Input a letter: t

-a-a---ipt
Input a letter: x
No such letter in the word

-a-a---ipt
Input a letter: b
No such letter in the word

-a-a---ipt
Input a letter: d
No such letter in the word

-a-a---ipt
Input a letter: w
No such letter in the word
You are hanged!


H A N G M A N

----
Input a letter: j

j---
Input a letter: i
No such letter in the word

j---
Input a letter: +
It is not an ASCII lowercase letter

j---
Input a letter: A
It is not an ASCII lowercase letter

j---
Input a letter: ii
You should print a single letter

j---
Input a letter: ++
You should print a single letter

j---
Input a letter:
You should print a single letter

j---
Input a letter: g
No such letter in the word

j---
Input a letter: a

ja-a
Input a letter: v
You guessed the word java!
You survived!
"""


import random
import string
from collections import defaultdict


n_attempts = 8
legal_letters = set(string.ascii_lowercase)
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

    if len(letter) != 1:
        print('You should print a single letter')
        continue

    if letter not in legal_letters:
        print('It is not an ASCII lowercase letter')
        continue

    if letter in entered_letters:
        print('You already typed this letter')
        continue

    entered_letters.add(letter)

    if letter in letter_positions:
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
