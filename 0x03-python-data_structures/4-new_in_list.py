#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        list = [x for x in my_list]

        if idx < 0 or idx >= len(list):
            return list
        else:
            list[idx] = element
            return list


