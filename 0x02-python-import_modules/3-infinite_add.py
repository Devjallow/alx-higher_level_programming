#!/usr/bin/python3
if __name__ == " __main__ ":
    """ print sum of all argument """
    import sys
    
    total = sum(map(int, sys.argv[1:]))
    print("{}".format(total))
