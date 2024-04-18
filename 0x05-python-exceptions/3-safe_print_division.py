#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        compute = a / b
    except ZeroDivisionError:
        compute = None
    finally:
        print("Inside result:", "{}".format(compute))
    return compute
