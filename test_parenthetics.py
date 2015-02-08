# Test file for parenthetics.property

import pytest  # used for exception testing
import parenthetics as p


def test_parenthetics_open():
    """Tests a string with:
    an open paren that is not closed.
    """
    single = "("
    nested_single = "(((((a))))"
    double = "((a"
    extra_beginning = "(a(a)"
    extra_end = "(a)b(bb"
    extra_middle = "(b)(b(b)"
    nested_extra_middle = "((bbb)cc((bbb))"
    assert p.parenthetics(single) == 1
    assert p.parenthetics(nested_single) == 1
    assert p.parenthetics(double) == 1
    assert p.parenthetics(extra_beginning) == 1
    assert p.parenthetics(extra_end) == 1
    assert p.parenthetics(extra_middle) == 1
    assert p.parenthetics(nested_extra_middle) == 1


def test_parenthetics_balanced():
    """Tests a string with:
    an equal number of open and closed parentheses.
    """
    no_parens = ""
    single = "(a)a"
    double = "()a()a"
    triple = "(a)(b)(c)"
    nested = "((abc))"
    double_nested = "(((acd))d)"
    double_inside_nested = "(()())"
    nested_inside_nested = "((())())"
    assert p.parenthetics(no_parens) == 0
    assert p.parenthetics(double) == 0
    assert p.parenthetics(single) == 0
    assert p.parenthetics(triple) == 0
    assert p.parenthetics(nested) == 0
    assert p.parenthetics(double_nested) == 0
    assert p.parenthetics(double_inside_nested) == 0
    assert p.parenthetics(nested_inside_nested) == 0


def test_parenthetics_broken():
    """Tests a string with:
    a closing parens that has not been proceeded by one that opens.
    """
    single = ")"
    nested_single = "a(a(((a)))))a"
    double = ")c)c"
    extra_beginning = ")d(d)"
    extra_end = "(d)d)"
    extra_middle = "())aaaaaaa()"
    nested_extra_middle = "(())abc())"
    assert p.parenthetics(single) == -1
    assert p.parenthetics(nested_single) == -1
    assert p.parenthetics(double) == -1
    assert p.parenthetics(extra_beginning) == -1
    assert p.parenthetics(extra_end) == -1
    assert p.parenthetics(extra_middle) == -1
    assert p.parenthetics(nested_extra_middle) == -1
