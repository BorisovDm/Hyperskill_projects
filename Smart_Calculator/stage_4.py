"""
Project: Smart Calculator (Python)
Stage #4: Add subtractions

Description
At this stage, your calculator should support the addition + and subtraction - operators.

The program must calculate expressions like these: 4 + 6 - 8, 2 - 3 - 4, and so on.
It must support both unary and binary minus operators.
If the user has entered several operators following each other, the program still should work (like Java or Python REPL).
Interpret two adjacent minus signs as a plus.

Modify the result of the /help command to explain these operations.

Decompose your program using functions to make it easy to understand and edit later.

Input/Output example
8
8

-2 + 4 - 5 + 6
3
9 +++ 10 -- 8
27
3 --- 5
-2
14       -   12
2
/exit
Bye!
The program should not stop until the user enters the /exit command.
"""


if __name__ == '__main__':
    while True:
        input_line = input().strip()
        if input_line == '':
            continue

        if input_line == '/help':
            print('The program calculates the sums and subtractions of numbers')

        if input_line == '/exit':
            print('Bye!')
            break

        print(eval(input_line))
