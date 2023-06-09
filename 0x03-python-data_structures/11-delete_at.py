#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    list_len = len(my_list)
    if (idx < -list_len or idx >= list_len):
        return my_list
    new_list = my_list.copy()
    my_list.clear()
    if (idx < 0):
        new_idx = idx + list_len
        my_list.extend(new_list[:new_idx])
        if (list_len > new_idx + 1):
            my_list.extend(new_list[new_idx + 1:])
    else:
        my_list.extend(new_list[:idx])
        if (list_len > idx + 1):
            my_list.extend(new_list[idx + 1:])
    return my_list
