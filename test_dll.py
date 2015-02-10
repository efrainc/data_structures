# Test file for dll.py
# Authors Mark, Efrain, Henry

import pytest  # used for exception testing
import dll


@pytest.fixture(scope='function')
def empty_dll():
    """Fixture generates empty doubly linked list for testing."""
    return dll.Dll()


@pytest.fixture(scope='function')
def populated_dll():
    """Fixture generates a populated doubly linked list."""
    populated = dll.Dll()
    populated.append('first')
    populated.append('second')
    populated.append('third')
    populated.append('fourth')
    populated.append(5)
    populated.append(6)
    return populated


def test_init():
    """Test doubly link list class constructor."""

    a = dll.Dll()
    assert a.head is None
    assert a.tail is None


def test_insert(empty_dll, populated_dll):
    """Test insert by adding node to empty and populated dll
    """
    # adding to an empty doubly link list
    empty_dll.insert("Mark")
    assert "Mark" == empty_dll.head.value
    assert "Mark" == empty_dll.tail.value
    print empty_dll.head.next
    assert empty_dll.head.next is None
    assert empty_dll.head.previous is None
    empty_dll.insert(3)
    assert 3 == empty_dll.head.value
    assert "Mark" == empty_dll.tail.value
    assert "Mark" == empty_dll.head.previous.value
    assert empty_dll.tail.next.value == 3
    assert empty_dll.head.next is None
    assert empty_dll.head.previous.value == "Mark"
    # Test insert into populated list.
    populated_dll.insert("Henry")
    assert "Henry" == populated_dll.head.value
    assert 6 == populated_dll.tail.value
    assert "first" == populated_dll.head.previous.value
    assert populated_dll.head.next is None
    populated_dll.insert("Efrain")
    assert "Efrain" == populated_dll.head.value
    assert 6 == populated_dll.tail.value
    assert "Henry" == populated_dll.head.previous.value
    assert populated_dll.head.next is None


def test_append(empty_dll, populated_dll):
    """Test append by adding node to empty and populated dll
    """
    # adding to an empty doubly link list
    empty_dll.append("Mark")
    assert "Mark" == empty_dll.head.value
    assert "Mark" == empty_dll.tail.value
    assert empty_dll.head.next is None
    assert empty_dll.head.previous is None
    empty_dll.append(3)
    assert "Mark" == empty_dll.head.value
    assert 3 == empty_dll.tail.value
    assert 3 == empty_dll.head.previous.value
    assert empty_dll.tail.next.value == "Mark"
    assert empty_dll.head.next is None
    assert empty_dll.head.previous.value == 3
    # Test append into populated list.
    populated_dll.append("Henry")
    assert "first" == populated_dll.head.value
    assert "Henry" == populated_dll.tail.value
    assert populated_dll.tail.previous is None
    assert "second" == populated_dll.head.previous.value
    assert populated_dll.head.next is None
    populated_dll.append("Efrain")
    assert "first" == populated_dll.head.value
    assert "Efrain" == populated_dll.tail.value
    assert "second" == populated_dll.head.previous.value
    assert "Henry" == populated_dll.tail.next.value
    assert populated_dll.head.next is None
    assert populated_dll.tail.previous is None


def test_pop(empty_dll, populated_dll):
    """Test pop method with a populated and empty dll.
    """
    # pop from dll with one value
    empty_dll.insert("Mark")
    assert empty_dll.pop() == "Mark"
    assert empty_dll.head is None
    assert empty_dll.tail is None
    # Confirm Attribute error with pop from empty dll
    with pytest.raises(AttributeError):
        assert empty_dll.pop() is None
    # Confirming pop from populated dll
    assert populated_dll.pop() == "first"
    assert populated_dll.head.next is None
    assert populated_dll.head.previous.value == "third"
    assert populated_dll.head.value == "second"
    assert populated_dll.tail.value == 6



def test_shift(empty_dll, populated_dll):
    """Test shift method with a populated and empty dll.
    """
    # shift from dll with one value
    empty_dll.insert("Mark")
    assert empty_dll.shift() == "Mark"
    assert empty_dll.head is None
    assert empty_dll.tail is None
    # Confirm Attribute error with shift from empty dll
    with pytest.raises(AttributeError):
        assert empty_dll.shift() is None
    # Confirming shift from populated dll
    assert populated_dll.shift() == 6
    assert populated_dll.tail.previous is None
    assert populated_dll.tail.next.value == "fourth"
    assert populated_dll.head.value == "first"
    assert populated_dll.tail.value == 5


def test_remove(populated_dll):
    """ Test remove with a populated and empty dll.
    """
    populated_dll.remove("third")
    # Confirm Attribute error withn searching for val not in the dll
    with pytest.raises(AttributeError):
        assert populated_dll.remove("third") is None
    with pytest.raises(AttributeError):
        assert empty_dll.remove("test") is None
    assert populated_dll.count == 5


# def test_remove():
#     """Test removal of nodes."""
#     # Test remove of node in middle of linked list
#     a = dll.Dll()
#     a.insert("Henry")
#     a.insert("Efrain")
#     a.insert("Last")
#     a.remove(a.search("Henry"))
#     assert a.size() == 2
#     assert str(a) == "('Last', 'Efrain')"
#     # Test removal of the first node
#     a.remove(a.search("Last"))
#     assert a.size() == 1
#     assert str(a) == "('Efrain')"
#     # Test removal of last node
#     a.remove(a.search("Efrain"))
#     assert a.size() == 0
#     assert str(a) == "()"


# def test_str():
#     """Test  of string formatting with integers and strings."""

#     a = dll.Dll()
#     assert str(a) == "()"
#     a.insert("Mark")
#     a.insert("Henry")
#     a.insert(1232)
#     a.insert("Efrain")
#     a.insert("Last")
#     a.insert(4545)
#     assert str(a) == "(4545, 'Last', 'Efrain', 1232, 'Henry', 'Mark')"
#     # Test string evaluates to a tuple literal
#     assert eval(str(a)) == (4545, 'Last', 'Efrain', 1232, 'Henry', 'Mark')



# def test_size():
#     """Test Size with pop and remove commands."""

#     a = dll.Dll()
#     a.insert("Mark")
#     a.insert("Henry")
#     a.insert("Efrain")
#     a.insert("Last")
#     a.display()
#     assert a.size() == 4
#     a.remove(a.search("Henry"))
#     assert a.size() == 3
#     a.pop()
#     assert a.size() == 2
#     a.pop()
#     assert a.size() == 1
#     a.pop()
#     assert a.size() == 0


# def test_search():
#     """Return the node containing value in the list, if present, else None."""

#     a = dll.Dll()
#     a.insert("Mark")
#     a.insert("Henry")
#     a.insert(1232)
#     a.insert("Efrain")
#     a.insert("Last")
#     a.insert(4545)
#     assert a.search("Mark").value == "Mark"
#     assert a.search(1232).value == 1232
#     # Test ability to find first node value
#     assert a.search(4545).value == 4545
#     # Test search for non-existing item
#     assert a.search("George") is None
