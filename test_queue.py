# Test file for queue.py
# Authors Mark, Efrain, Henry

import pytest
import queue as que

def test_init():
    """Test queue constructor."""
    a = que.Queue()
    assert a.front is None
    assert a.back is None

def test_enqueue(empty_queue, populated_queue):
    """Test enqueue with empty and populated queue."""
    empty_queue.enqueue('first')
    assert isinstance(empty_queue.front, que.Node)
    assert isinstance(empty_queue.back, que.Node)
    # assert empty_queue.front.pointer is None
    # assert empty_queue.back.pointer is None
    assert 'first' == empty_queue.back.value
    populated_queue.enqueue(7)
    assert 'first' == populated_queue.front.value

def test_dequeue(populated_queue):
    """Test dequeue with populated and empty queus."""
    assert 'first' == populated_queue.dequeue()
    assert 'second' == populated_queue.dequeue()
    assert 'third' == populated_queue.dequeue()
    assert 'fourth' == populated_queue.dequeue()
    assert 5 == populated_queue.dequeue()
    assert 6 == populated_queue.dequeue()
    # Test popping from an empty queue to raise an AttrubuteError;
    with pytest.raises(AttributeError):
        assert populated_queue.dequeue()

def test_enqueue_and_dequeue(empty_queue, populated_queue):
    """Test enqueues mixed with dequeues."""
    empty_queue.enqueue('first')
    empty_queue.enqueue('second')
    assert 'first' == empty_queue.front.value
    assert 'second' == empty_queue.back.value  
    assert 'first' == empty_queue.dequeue()
    assert 'second' == empty_queue.front.value
    assert 'second' == empty_queue.back.value
    empty_queue.enqueue('third')
    empty_queue.enqueue('fourth')
    assert 'second' == empty_queue.dequeue()
    assert 'third' == empty_queue.front.value
    assert 'fourth' == empty_queue.back.value


def test_size(empty_queue, populated_queue):
    """Test the size of queue. Unpopulated will return 0.
    populated will return number of entries."""
    assert 0 == empty_queue.size()
    assert 6 == populated_queue.size()
    populated_queue.dequeue()
    populated_queue.dequeue()
    assert 4 == populated_queue.size()

@pytest.fixture(scope='function')
def empty_queue():
    """Fixture generates empty queue for testing."""
    return que.Queue()


@pytest.fixture(scope='function')
def populated_queue():
    """Fixture generates a populated queue."""
    populated = que.Queue()
    populated.enqueue('first')
    populated.enqueue('second')
    populated.enqueue('third')
    populated.enqueue('fourth')
    populated.enqueue(5)
    populated.enqueue(6)
    return populated
