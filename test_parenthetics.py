# Test file for parenthetics.property

import parenthetics as p


def test_parenthetics_open():
    """Tests a string with:
    open parens that are not properly closed.
    """
    cases = ["(", "(((((a))))", "((a", "(a(a)", "(a)b(bb",
             "(b)(b(b)", "((bbb)cc((bbb))"]

    for i in cases:
        assert p.parenthetics(i) == 1


def test_parenthetics_balanced():
    """Tests a string with:
    an equal number of open and closed parentheses.
    """
    cases = ["", "(a)a", "()a()a", "(a)(b)(c)", "((abc))",
             "(((acd))d)", "(()())", "((())())"]

    for i in cases:
        assert p.parenthetics(i) == 0


def test_parenthetics_broken():
    """Tests a string with:
    a closing parens that has not been proceeded by one that opens.
    """
    cases = [")", "a(a(((a)))))a", ")c)c", ")d(d)", "(d)d)",
             "())aaaaaaa()", "(())abc())"]

    for i in cases:
        assert p.parenthetics(i) == -1
