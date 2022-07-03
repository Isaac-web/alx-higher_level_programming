#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    
    if(length > 0):
      first_char = sentence[0]
    result  = length, first_char
    return result
