#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    importfunc = dir()
    for x in range(0, len(importfunc)):
        if importfunc[x][:2] != "__":
            print("{:s}".format(importfunc[x]))
