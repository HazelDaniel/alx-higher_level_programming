#!/usr/python3

def weight_average(my_list=[]):
    sum = 0
    sum_div = 0
    if (not my_list):
        return 0
    for (x, y) in my_list:
        print((sum_div, y))
        sum += (x * y)
        sum_div += y
    if sum_div == 0:
        sum_div = 1
    return (sum / sum_div)
