#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        high_score = list(a_dictionary.keys())[0]
        for i in a_dictionary.keys():
            if a_dictionary[i] > a_dictionary.get(high_score):
                high_score = i
        return high_score
