#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
first_word = str[39:(39 + len("object-oriented programming "))]
middle_word = str[-22:-17]
last_word = str[0:6]
print(f"{first_word}{middle_word}{last_word}")
