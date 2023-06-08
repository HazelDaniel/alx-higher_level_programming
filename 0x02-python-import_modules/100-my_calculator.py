#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    import sys

    arv = sys.argv
    arg_len = len(arv)
    if arg_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    match(arv[2]):
        case '+':
            print("{} + {} = {}\
            ".format(arv[1], arv[3], add(int(arv[1]), int(arv[3]))))
        case '-':
            print("{} - {} = {}\
            ".format(arv[1], arv[3], sub(int(arv[1]), int(arv[3]))))
        case '-':
            print("{} * {} = {}\
            ".format(arv[1], arv[3], mul(int(arv[1]), int(arv[3]))))
        case '/':
            print("{} / {} = {}\
            ".format(arv[1], arv[3], div(int(arv[1]), int(arv[3]))))
        case '_':
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
