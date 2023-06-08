#!/usr/bin/python3
def print_alphabet(current):
    print(chr(current), end='')
    current + 1 < ord('Z') and print_alphabet(current + 1)


print_alphabet(ord('A'))
