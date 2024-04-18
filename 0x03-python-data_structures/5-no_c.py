#!/usr/bin/python3
def no_c(my_string):
    changed_string = ""
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        changed_string += my_string[i]
    return changed_string
