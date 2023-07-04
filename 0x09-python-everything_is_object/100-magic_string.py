#!/usr/bin/python3
def magic_string():
    magic_string.inner = getattr(magic_string, "inner", 0) + 1
    return ", ".join(["Bestschool" for _ in range(magic_string.inner)])
