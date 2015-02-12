import pytest
import priorityq


def test_insert(empty_pqueue):
    """Test adding items to the list with correct priority"""
    # tests that adding lower priority doesn't change first
    empty_pqueue.insert(1, 1)
    assert empty_pqueue.peek() == 1
    empty_pqueue.insert(2, 2)
    assert empty_pqueue.peek() == 1
    empty_pqueue.insert(3, 3)
    assert empty_pqueue.peek() == 1
    # tests that lower priorities were inserted correctly
    assert empty_pqueue.pop() == 1
    assert empty_pqueue.pop() == 2
    assert empty_pqueue.pop() == 3
    # tests that adding higher priority is returned first
    empty_pqueue.insert(1, 3)
    assert empty_pqueue.peek() == 1
    empty_pqueue.insert(2, 2)
    assert empty_pqueue.peek() == 2
    empty_pqueue.insert(3, 1)
    assert empty_pqueue.peek() == 3


def test_pop(populated_pqueue):
    """Test that pop removes the item with the highest priority"""
    queue_expected = [2, 5, 8, 3, 6, 9, 4, 7, 10]
    for x in queue_expected:
        assert populated_pqueue.pop() == x
    with pytest.raises(AttributeError):
        populated_pqueue.pop()


def test_peek():
    """Displays the highest prioritiy item without removing
    it from the list"""
    pass


@pytest.fixture(scope='function')
def empty_pqueue():
    return priorityq.Pq()


@pytest.fixture(scope='function')
def populated_pqueue():
    populated = priorityq.Pq()
    for x, y in zip(range(2, 11), [1, 2, 3] * 3):
        populated.insert(x, y)
    return populated
