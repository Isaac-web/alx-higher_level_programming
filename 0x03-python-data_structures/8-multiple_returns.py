#!/usr/bin/python3

def multiple_returns(sentence):
    length, first_char = len(sentence), None
    
    if(length > 0):
      first_char = sentence[0]
    result  = length, first_char
    return result
