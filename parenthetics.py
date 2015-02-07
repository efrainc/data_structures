"""Method to determine if string contains proper parenthetics.
Returns 1 if string is 'open', not all parentheses have been closed.
Returns 0 if string is balanced.
Returns -1 if string is 'broken', a closing parens has not been preceed by an 
    open parentese.
"""
import stack


def parenthetics(input_string):
