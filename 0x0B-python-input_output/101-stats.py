#!/usr/bin/python3
"""a module that reads from standard input and computes the metrics"""
import sys


def print_stats(size, status_codes):
    """a function that prints accumulated metrics """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    size = 0
    status_codes = {}
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1
            line = line.split()
            try:
                size += int(line[-1])
            except (ValueError, IndexError):
                pass
            try:
                if line[-2] in codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass
        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
