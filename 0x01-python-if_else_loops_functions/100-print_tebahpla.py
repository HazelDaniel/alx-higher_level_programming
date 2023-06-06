#!/usr/bin/python3

for i in reversed(range(97, 123)):
    j = 0
    if not (i % 2):
        pass
    else:
        j = 32
    print("{}".format(chr(i - j)), end="")
