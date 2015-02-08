#! /usr/bin/env python

# Efrain Camacho Parenthetical Assignment

import pytest
from parenthetics import paren_checker as pc

def test_function():
    """Test various configuration of paraenthesis using pc function"""
    strings_container = random_strings()
    assert pc(strings_container[0]) == 0
    assert pc(strings_container[1]) == 0
    assert pc(strings_container[2]) == 1
    assert pc(strings_container[3]) == -1
    assert pc(strings_container[4]) == -1

    return None

@pytest.fixture(scope='function')
def random_strings():
    """Fixture contains random strings for testing."""

    string_a = '(abcd)'
    string_b = '((D))()'
    string_c = '(((())'
    string_d = ')))((('
    string_e = '())('
    return string_a, string_b, string_c, string_d, string_e

#Testing guidelines
# Return 1 if the string is "open" (there are open parens that are not closed)
# Return 0 if the string is "balanced" (there are an equal number of open and closed parentheses in the string)
# Return -1 if the string is "broken" (a closing parens has not been proceeded by one that opens)