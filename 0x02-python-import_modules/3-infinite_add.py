#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sumint = 0
    for x in range(1, len(argv)):
        sumint += int(argv[x])
    print("{}".format(sumint))
