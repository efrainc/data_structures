"""Method to determine if string contains proper parenthetics.
Returns 1 if string is 'open', not all parentheses have been closed.
Returns 0 if string is balanced.
Returns -1 if string is 'broken', a closing parens has not been preceed by an
    open parentese.
"""
import stack as st


def parenthetics(input_string):
    only_parens = st.Stack()
    for letter in input_string:
        if letter == '(' or letter == ')':
            only_parens.push(letter)
    out = check_parens(only_parens)
    # Reduce values greater than 1 to 1 and less than -1 to -1
    if out != 0:
        out = out / abs(out)
    return out


def check_parens(input_stack):
    if input_stack.top:
        parens = input_stack.pop()
        if parens == '(':
            return check_parens(input_stack) + 1
        if parens == ')':
            return check_parens(input_stack) - 1
    return 0