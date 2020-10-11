from __future__ import print_function
import sys

def anything():
    return "print"

def hello(what):
    print('Hello, {}!'.format(what))

def say_what():
    return 'world'

def one():
    a, b = 1, 2
    return a + b

def two():
    a, b = "co", "de"
    return a + b

def three():
    a, b = 1, 9
    return b - a

def four():
    a, b = "zadanie", " 5."
    return a + b

def main():
    hello(say_what())
    return 0


if __name__ == '__main__':
    sys.exit(main())
