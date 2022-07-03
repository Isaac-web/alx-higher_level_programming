#!/usr/bin/python3

def multiple_returns(sentence):
    length, first_char = len(sentence), None
    if(length >= 0):
      first_char = sentence[0]
    return tuple([length, first_char])
