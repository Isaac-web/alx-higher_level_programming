#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    length = len(my_list)
    result = []
    if not length:
        return
    for index in range(length):
        if my_list[index]%2 == 0:
            result.append(True)
            continue
        result.append(False)
    return result
