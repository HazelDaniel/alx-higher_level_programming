#!/usr/bin/python3

def remove_char_at(str, n):
    length = len(str)
    if (n >= length):
        return str
    else:
        if (n == 0 and length >= 2):
            return (str[1:])
        if (n + length >= 0 and n >= 0):
            rem = n + 1
            if rem >= length or n - 1 == -1:
                return str
            return (str[:n] + str[rem:length])
        else:
            return str
