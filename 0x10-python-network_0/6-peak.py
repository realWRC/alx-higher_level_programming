#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers
    """
    cap = len(list_of_integers)
    median = cap
    mdle = cap // 2

    if cap == 0:
        return None

    while True:
        median = median // 2
        if (mdle < cap - 1 and
                list_of_integers[mdle] < list_of_integers[mdle + 1]):
            if median // 2 == 0:
                median = 2
            mdle = mdle + median // 2
        elif median > 0 and list_of_integers[mdle] < list_of_integers[mdle - 1]:
            if median // 2 == 0:
                median = 2
            mdle = mdle - median // 2
        else:
            return list_of_integers[mdle]
