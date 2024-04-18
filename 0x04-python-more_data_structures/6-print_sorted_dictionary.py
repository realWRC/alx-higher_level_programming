#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    organised_dict = sorted(a_dictionary)
    for i in organised_dict:
        print("{}: {}".format(i, a_dictionary[i]))
