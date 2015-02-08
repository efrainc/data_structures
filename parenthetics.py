#! /usr/bin/env python

# Efrain Camacho Parenthetics Assignmetn

def paren_checker(text):
    """Checks to confirm each opening paren is closed correcrly."""
    encoded_string = text.encode('utf-8')
    count = 0
    for i in encoded_string:
        if i == ')':
            count -= 1
        elif i == '(':
            count += 1
        if count < 0:
            return -1
    if count > 1:
            return 1
    return 0

