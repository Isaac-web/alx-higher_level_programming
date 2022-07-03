#!/usr/bin/python3

def no_c(my_string):
    chars = list(my_string)
    for i in range(len(chars)):
        if chars[i] == "c" or chars[i] == "C":
            chars[i] = ""
    return "".join(chars)
