"""
Project: Smart Calculator (Python)
Stage 5/7: Error!

Description
Modify your program to handle different cases when the given expression has an invalid format.
The program should print "Invalid expression" in such cases.
The program must never throw any exception.

If a user enters an invalid command, the program must print "Unknown command".
All messages must be printed without quotes.
Do not forget to write methods to decompose your program.

Input/Output example
8 + 7 - 4
11
abc
Invalid expression
123+
Invalid expression
+15
15
18 22
Invalid expression

-22
-22
22-
Invalid expression
/go
Unknown command
/exit
Bye!
The program should not stop until the user enters the /exit command (like before).

"""


def eval_line(s):
    parts = s.split()

    if len(parts) % 2 != 1:
        raise ValueError

    line_value = 0
    sign = 1

    for idx, elem in enumerate(parts):
        if idx % 2 == 0:  # number
            line_value += sign * int(elem)
            sign = 1

        else:  # plus/minus
            for jdx in elem:
                if jdx == '+':
                    sign *= 1
                elif jdx == '-':
                    sign *= -1
                else:
                    raise ValueError

    return line_value


if __name__ == '__main__':
    while True:
        input_line = input().strip()
        if input_line == '':
            continue

        if input_line.startswith('/'):
            if input_line == '/help':
                print('The program calculates the sums and subtractions of numbers')

            elif input_line == '/exit':
                print('Bye!')
                break

            else:
                print('Unknown command')
            continue

        try:
            print(eval_line(input_line))
        except ValueError:
            print('Invalid expression')
