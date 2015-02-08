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

    while text:
        if text[0] == ')':
            if not parens.top:  # case of ), but no ( on stack
                return -1
            parens.pop()  # if ( on stack, pop one off
        elif text[0] == '(':
            parens.push('(')  # doesn't matter what value is
        text = text[1:]
    if not parens.top:
        return 0
    else:
        return 1
