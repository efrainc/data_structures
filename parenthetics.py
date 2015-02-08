import stack as st


def parenthetics(input_string):
    """Method that will test string for proper parenthetics.
    Returns 1 if string is 'open', not all parentheses have been closed.
    Returns 0 if string is balanced.
    Returns -1 if string is 'broken', a closing parens has not been preceeded
    by an open parentese.
    """
    open_parens = st.Stack()
    for letter in input_string:
        if letter == u'(':   # add all open parens to stack
            open_parens.push(letter)
        # check that for every close parens there is an open in the stack
        if letter == u')':
            if open_parens.top:
                open_parens.pop()
                continue
            return -1   # if no open parens in stack
    if open_parens.top:     # if extra open parens
        return 1
    return 0        # parens must be balanced
