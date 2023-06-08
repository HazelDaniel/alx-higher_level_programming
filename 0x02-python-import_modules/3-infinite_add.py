#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
    arg_len = len(sys.argv)
    arv = sys.argv
    if arg_len == 1:
        print(sum)
    else:
        for i in range(1, arg_len):
            sum += int(arv[i])
        print(sum)
