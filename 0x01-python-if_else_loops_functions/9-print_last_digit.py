#!/usr/bin/python3
def print_last_digit(number):
    if number < 10:
        number = -number
    last_digit = number % 10
    print("{}".format(last_digit), end='')
    return (last_digit)
