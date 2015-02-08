#! /usr/bin/env python
# parenthetics - recursive version
#
# by Henry Grantham

from __future__ import unicode_literals


def parenthetics(text, open_parens=0):
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

    # reached end of text block:
    if not text and open_parens == 0:
        return 0
    elif not text and open_parens > 0:
        return 1

    if text[0] == ')':
        open_parens -= 1
        # if there are more closed parens than open, return -1
        if open_parens < 0:
            return -1
        return parenthetics(text[1:], open_parens)
    elif text[0] == '(':
        return parenthetics(text[1:], open_parens+1)
    else:
        return parenthetics(text[1:], open_parens)
