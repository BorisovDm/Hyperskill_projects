"""
Project: Smart Calculator (Python)
Stage #1: 2+2

Description
Write a program that reads two integer numbers from the same line and prints their sum in the standard output.
Numbers can be positive, negative, or zero.

Input/Output example
The example below shows input and the corresponding output. Your program should work in the same way.
5 8
13
Do not add extra characters after the output.
"""


if __name__ == '__main__':
    arguments = list(map(int, input().split()))
    assert len(arguments) == 2
    result = sum(arguments)
    print(result)
