#!/usr/bin/python3

def roman_to_int(roman_string):
    sum = 0
    if (str(type(roman_string)) != "<class 'str'>"):
        return sum
    roman_dict = dict([('M', 1000), ('D\
', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)])
    for i, c in enumerate(roman_string):
        if not roman_dict.get(c, None):
            return sum
        if (i < len(roman_string) - 1 and
                roman_dict[c] < roman_dict.get(roman_string[i + 1], 0)):
            sum += -roman_dict[c]
        else:
            sum += roman_dict[c]
    return sum
