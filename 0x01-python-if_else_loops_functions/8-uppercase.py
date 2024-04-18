#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) in range(ord('a'), ord('z') + 1):
            character = chr(ord(x) - 32)
        else:
            character = x
        print("{}".format(character), end="")
    print('')
