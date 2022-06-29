#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            print("{}".format((chr(i) - 32)))
        else:
            print("{}".format(chr(i)))
