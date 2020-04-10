"""
Project: Smart Calculator
Stage 7/7: I’ve got the power
"""


def eval_line(s, var_dict):
    for key in sorted(var_dict.keys(), key=len, reverse=True):
        s = s.replace(key, str(var_dict[key]))

    return int(eval(s))


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
        except (ValueError, SyntaxError):
            print('Invalid expression')
        except KeyError:
            print('Unknown variable')
