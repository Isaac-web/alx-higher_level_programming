#!/usr/bin/python3
"""Just a regular module"""


def find_peak(numbr):
    """
        Returns the peak of of numbers provided
        Args:
            list_of_integers(int): List of intergers
        Return: the peak
    """
    length = len(numbr)
    if length == 0:
        return None
    if length == 1:
        return (numbr[0])
    if length == 2:
        return numbr[0] if numbr[0] >= numbr[1] else numbr[1]

    for idx in range(0, length):
        value = numbr[idx]
        if (idx > 0 and idx < length - 1 and
                numbr[idx + 1] <= value and numbr[idx - 1] <= value):
            return value
        elif idx == 0 and numbr[idx + 1] <= value:
            return value
        elif idx == length - 1 and numbr[idx - 1] <= value:
            return value
    return pick
