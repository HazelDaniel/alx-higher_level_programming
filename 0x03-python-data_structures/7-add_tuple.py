#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    seq1, seq2 = list(tuple_a), list(tuple_b)
    seq1.extend([0, 0])
    seq2.extend([0, 0])
    seq1, seq2 = seq1[:2], seq2[:2]
    res = [0, 0]
    res[0] = seq1[0] + seq2[0]
    res[1] = seq1[1] + seq2[1]
    return (tuple(res))
