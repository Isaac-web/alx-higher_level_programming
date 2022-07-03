#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result = []
    for index in range(len(my_list)):
        if my_list[index]%2 == 0:
            result.append(True)
            continue
        result.append(False)
    return result
