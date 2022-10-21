#!/usr/bin/python3
"""Just a regular module"""


def find_peak(list_of_integers):
    """
        Returns the peak of of numbers provided
        Args:
            list_of_integers(int): List of intergers
        Return: the peak
    """
    peak = None
    for i in range(len(list_of_integers)):
        current, left, right = list_of_integers[i], 0, 0
        if i > 0:
            left = list_of_integers[i-1]
        if i < len(list_of_integers) - 1:
            right = list_of_integers[i+1]
        if current > left and current > right:
            peak = current
        elif current == left and current == right:
            peak = current
    return peak
