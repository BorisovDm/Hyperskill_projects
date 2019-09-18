"""
Project: Smart Calculator (Python)
Stage #2: 2+2+

Description
Write a program that reads two numbers in a loop and prints the sum in the standard output.
If a user enters only a single number, the program should print the same number.
If a user enters an empty line, the program should ignore it.

When the command /exit is entered, the program must print "Bye!" (without quotes), and then stop.

Input/Output example
The example below shows input and the corresponding output. Your program should work in the same way.

17 9
26
-2 5
3

7
7
/exit
Bye!
"""


if __name__ == '__main__':
    while True:
        input_line = input().strip()
        if input_line == '':
            continue

        if input_line == '/exit':
            print('Bye!')
            break

        arguments = map(int, input_line.split())
        print(sum(arguments))
