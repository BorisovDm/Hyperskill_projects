"""
Project: Smart Calculator (Python)
Stage #3: Count them all

Description
At this stage, the program should read an unlimited sequence of numbers from the standard input and calculate their sum.
Also, add a /help command to print some information about the program.

Input/Output example
The example below shows input and the corresponding output. Your program should work in the same way.

4 5 -2 3
10
4 7
11
6
6
/help
The program calculates the sum of numbers
/exit
Bye!
"""


if __name__ == '__main__':
    while True:
        input_line = input().strip()
        if input_line == '':
            continue

        if input_line == '/help':
            print('The program calculates the sum of numbers')

        if input_line == '/exit':
            print('Bye!')
            break

        arguments = map(int, input_line.split())
        print(sum(arguments))
