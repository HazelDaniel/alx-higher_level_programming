#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    ret = False

    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as e:
        print("Exception:", e, file=sys.stderr)
        ret = False
    else:
        ret = True
    return ret
