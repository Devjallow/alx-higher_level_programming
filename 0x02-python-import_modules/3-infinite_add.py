#!/usr/bin/python3
if __name__ == " __main__ ":
    """ print sum of all argument """
    import sys

    args = sys.argv[1:]
    sumTotal = 0
    for arg in args:
        sumTotal += int(arg)
    print("{}".format(sumTotal))
