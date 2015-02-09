#! /usr/bin/env python
# parenthetics - version using stack
#
# by Henry Grantham

from __future__ import unicode_literals

import stack


def parenthetics(text):
    """Determines if a string is "open", "balanced", or "broken" given a string.

    Takes a unicode string (text) as input and returns one of
    three possible values:
    1 if the string is "open"
        (there are open parens that are not closed)
    0 if the string is "balanced"
        (there are an equal number of matching open and closed parenthasis)
    1 if the string is "broken"
    (a closing parens has not been proceeded by one that opens)
    """

    # number of open parens
    parens = stack.Stack()

    text_list = list(text)

    while text_list:
        element = text_list.pop(0)
        if element == ')' and parens.top:  # case ) and ( on stack, pop one off
            parens.pop()
        elif element == ')':  # case of ), but no ( on stack then "broken"
            return -1
        elif element == '(':  # case of (, push a ( onto stack
            parens.push('(')  # doesn't matter what value is
    if parens.top:
        return 1
    return 0
