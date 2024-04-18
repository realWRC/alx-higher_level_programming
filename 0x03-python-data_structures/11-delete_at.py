#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    final_list = my_list[:]

    for i in range(len(final_list)):
        if final_list[i] % 2 == 0:
            final_list[i] = True
        else:
            final_list[i] = False
    return (final_list)
