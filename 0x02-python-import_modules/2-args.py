#!/usr/bin/python3
import sys

if __name__ == "__main__":
    pl = ""
    count = 0
    header_end = "."
    arg_len = len(sys.argv)
    count = arg_len - 1
    if count > 1:
        pl = "s"
        header_end = ":"
    elif count == 1:
        header_end = ":"
    print("{} argument".format(count) + pl + header_end)
    for i in range(count):
        if i == count:
            print("{}: {}".format(i + 1, sys.argv[i + 1]), end="")
        else:
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
    pass
