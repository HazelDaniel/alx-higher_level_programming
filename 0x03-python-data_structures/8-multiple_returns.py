#!/usr/bin/python3
def multiple_returns(sentence):
    if (not len(sentence)):
        return None, None
    return len(sentence), sentence[0]
