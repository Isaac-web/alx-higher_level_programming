#!/bin/usr/python3
"""Defines a LockedClass module"""


class LockedClass:
    """Defines a locked last can only have the attribute 'first_name'"""
    __slots__ = ["first_name"]
