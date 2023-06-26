#!/bin/python3

def safe_print_integer(value):
    x = True

    try:
        print("{:d}".format(value + 0))
    except (TypeError, ValueError):
        x = False
    return x
