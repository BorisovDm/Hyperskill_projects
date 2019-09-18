"""
Project: Smart Calculator
Stage 6/7: Variables

Description
At this stage, your program should support variables.
We suppose that the name of a variable (identifier) can contain only Latin letters.
The case is also important; for example, n is not the same as N.
The value can be an integer number or a value of another variable.

Use dict to support variables.

The assignment statement may look like the following:
n = 3
m=4
a  =   5
b = a

A variable can have a name consisting of more than one letter.
count = 10

To print the value of a variable you should just type its name.
N = 5
N
5

It should be possible to set a new value to an existing variable.
a = 1
a = 2
a = 3
a
3

If an identifier or value of a variable is invalid, the program must print a message like the one below.
a1 = 8
Invalid identifier
n = a2a
Invalid assignment
a = 7 = 8
Invalid assignment

If a variable is not declared yet, the program should print "Unknown variable".
a = 8
b = c
Unknown variable
e
Unknown variable

Handle as many incorrect inputs as possible.
The program must never throw the NumberFormatException or any other exception.

It is important to note, all variables must store their values between calculations of different expressions.

Input/Output example
a = 3
b = 4
c = 5
a + b - c
2
b - c + 4 - a
0
a = 800
a + b + c
809
BIG = 9000
BIG
9000
big
Unknown variable
/exit
Bye!

The program should not stop until the user enters the /exit command.
"""


def eval_line(s, var_dict):
    parts = s.split()

    if len(parts) % 2 != 1:
        raise ValueError

    line_value = 0
    sign = 1

    for idx, elem in enumerate(parts):
        if idx % 2 == 0:  # number
            if elem.isalpha():
                elem = var_dict[elem]

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
    variable_dict = dict()

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

        if '=' in input_line:
            if input_line.count('=') > 1:
                print('Invalid assignment')
                continue

            variable, value = (_.strip() for _ in input_line.split('='))

            if not variable.isalpha():
                print('Invalid identifier')

            elif value.isdigit():
                variable_dict[variable] = int(value)

            elif value.isalpha():
                if value in variable_dict:
                    variable_dict[variable] = variable_dict[value]
                else:
                    print('Unknown variable')

            else:
                print('Invalid assignment')

            continue

        try:
            print(eval_line(input_line, variable_dict))
        except ValueError:
            print('Invalid expression')
        except KeyError:
            print('Unknown variable')
