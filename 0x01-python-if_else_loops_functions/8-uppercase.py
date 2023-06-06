#!/usr/bin/python3
string = "{}"


def uppercase(str):
    for i in range(0, len(str)):
        if (i == len(str) - 1):
            global string
            string = "{}\n"
        else:
            string = "{}"
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            print(string.format(chr(ord(str[i]) - 32)), end="")
        else:
            print(string.format(str[i]), end="")
