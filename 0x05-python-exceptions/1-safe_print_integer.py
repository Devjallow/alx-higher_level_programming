#!/usr/bin/python3
def save_print_interger(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
