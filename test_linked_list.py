# Test file for linked_list.py
# Authors Mark, Efrain, Henry

import pytest # used fo exception tesitng
import linked_list as ll


def test_init():
    """Test link_list class constructor."""

    a = ll.Linked_list()
    assert isinstance(a, ll.Linked_list)


def test_insert():
    """Test insert by adding node to empty list and

    adding list with exisiting nodes."""

    a = ll.Linked_list()
    assert a.head is None
    a.insert("Mark")
    assert "Mark" == a.head.value
    assert a.head.pointer is None
    print str(a)
    a.insert("Henry")
    print str(a)
    assert "Henry" == a.head.value
    assert "Mark" == a.head.pointer.value


def test_pop():
    """Test pop methond with a populated and empty list.

    Validate pop output and removal"""

    a = ll.Linked_list()
    a.insert("Mark")
    a.insert("Henry")
    assert a.pop() == "Henry"
    # Confirming that Mark is the new Head and has no pointer
    assert "Mark" == a.head.value
    assert a.head.pointer is None
    b = ll.Linked_list()
    # Confirm Attribute error with pop from empty list
    with pytest.raises(AttributeError):
        assert b.pop() is None


def test_remove():
    """Test That """

    a = ll.Linked_list()
    a.insert("Mark")
    a.insert("Henry")
    a.insert("Efrain")
    a.insert("Last")
    a.remove(a.search("Henry"))
    assert a.size() == 3
    assert str(a) == "('Last', 'Efrain', 'Mark')"


def test_str():
    """Test  of string formatting with integers and strings"""

    a = ll.Linked_list()
    a.insert("Mark")
    a.insert("Henry")
    a.insert(1232)
    a.insert("Efrain")
    a.insert("Last")
    a.insert(4545)
    assert str(a) == "(4545, 'Last', 'Efrain', 1232, 'Henry', 'Mark')"


def test_size():
    """Test Size with pop and remove commands"""

    a = ll.Linked_list()
    a.insert("Mark")
    a.insert("Henry")
    a.insert("Efrain")
    a.insert("Last")
    a.display()
    assert a.size() == 4
    a.remove(a.search("Henry"))
    assert a.size() == 3
    a.pop()
    assert a.size() == 2
    a.pop()
    a.pop()
    assert a.size() == 0


def test_search():
    """Return the node containing value in the list, if present, else None"""

    a = ll.Linked_list()
    a.insert("Mark")
    a.insert("Henry")
    a.insert(1232)
    a.insert("Efrain")
    a.insert("Last")
    a.insert(4545)
    assert a.search("Mark").value == "Mark"
    assert a.search(1232).value == 1232
    assert a.search("George") is None
