#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)
    for i in range(list_len):
        print("{}".format(my_list[list_len - (i + 1)]), end="\n")
