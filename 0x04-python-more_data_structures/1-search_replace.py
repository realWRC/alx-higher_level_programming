#!/usr/bin/python3
def search_replace(my_list, search, replace):
    modified_list = my_list[:]
    for i in range(len(modified_list)):
        if modified_list[i] == search:
            modified_list[i] = replace
    return modified_list
