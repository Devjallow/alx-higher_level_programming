#!/usr/bin/python3
import sys
print("{} arguments:".format(len(sys.argv[1:])))
for arg in sys.argv:
    if len(sys.argv) == 1:
        pass
    else:
        print("{}: {}".format(len(sys.argv[arg]), arg))
