import pytest
import parenthetics as pa


def test_return_one():
    # test method returns 1 if an open string is passed
    test_str = u'(()'
    assert pa(test_str) == 1
    # test with other characters
    test_str2 = u'aaaaa(bbbb(bbbbb)bbbb'
    assert pa(test_str2) == 1
    # test with multiple open parentheses
    test_str3 = u'aaaaa(bbbb((bbbbb)bbbb()('
    assert pa(test_str3) == 1


def test_return_zero():
    # test method returns zero if a string is balanced
    test_str = u'()'
    assert pa(test_str) == 0
    # test with other characters
    test_str2 = u'aaaaa(bbbb(bbbbb)bbbb)'
    assert pa(test_str2) == 0
    # test with multiple parentheses
    test_str3 = u'aaaaa(bbbb((bbbbb)bbbb)())()'
    assert pa(test_str3) == 0


def test_return_neg_one():
    # test method returns -1 if a string is broken
    test_str = u')'
    assert pa(test_str) == 0
    # test with other characters
    test_str2 = u'aaaaabbbb(bbbbb)bbbb)'
    assert pa(test_str2) == 0
    # test with multiple parentheses
    test_str3 = u'aaaaa(bbbb((bbbbb)bbbb)())())'
    assert pa(test_str3) == 0
    # test with multiple parentheses and unmatched
    test_str4 = u'aaaaa(bbbb))((bbbbb)bbbb)())()'
    assert pa(test_str4) == 0
    # test with multiple and unmatched parentheses
    test_str5 = u'aaaaa(bbbb))((bbbbb)bbbb)())()'
    assert pa(test_str5) == 0
