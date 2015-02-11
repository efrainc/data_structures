import pytest
import binheap


def test_init():
    """Test init of binheap Class."""
    test = binheap.Binheap()
    assert type(test.items) is list


def test_push(empty_binheap, populated_binheap):
    """Test push with large and small numbers to empty and populated binheaps."""
    empty_binheap.push(1)
    assert empty_binheap.items[0] == 1
    empty_binheap.push(2)
    assert empty_binheap.items[0] == 2
    assert empty_binheap.items[1] == 1
    empty_binheap.push(3)
    assert empty_binheap.items[0] == 3
    assert empty_binheap.items[1] == 1
    assert empty_binheap.items[2] == 2

    populated_binheap.push(10)
    h_list = [10, 9, 7, 8, 4, 3, 6, 2, 5]
    for item in range(len(h_list)):
        assert populated_binheap.items[item] == h_list[item]



# def test_pop(empty_binheap, populated_binheap):
#     """Test pop with large and small numbers to empty and populated binheaps."""
#     with pytest.raises(AttributeError):
#         assert empty_binheap.pop() is None
#     assert populated_binheap.pop() == 9
#     assert populated_binheap.pop() == 8
#     assert populated_binheap.pop() == 7
#     assert populated_binheap.pop() == 6
#     assert populated_binheap.pop() == 5
#     assert populated_binheap.pop() == 4
#     assert populated_binheap.pop() == 3
#     assert populated_binheap.pop() == 2



@pytest.fixture(scope='function')
def empty_binheap():
    return binheap.Binheap()

@pytest.fixture(scope='function')
def populated_binheap():
    populated = binheap.Binheap()
    for x in range(2, 10):
        populated.push(x)
    return populated
