# Test file for stack.py
# Authors Mark, Efrain, Henry

import pytest
import stack as st


def test_init():
    """Test stack constructor."""
    a = st.Stack()
    assert isinstance(a, st.Stack)

def test_push(empty_stack, populated_stack):
    """Test push function, with empty and populated stacks."""
    empty_stack.push('first')
    assert 'first' == empty_stack.top.value
    populated_stack.push('fifth')
    assert 'fifth' == populated_stack.top.value
    populated_stack.push('sixth')
    assert 'sixth' == populated_stack.top.value

def test_pop(populated_stack):
    """Test pop function, with empty and populated stacks."""
    assert 'fourth' == populated_stack.pop()
    assert 'third' == populated_stack.pop()
    assert 'second' == populated_stack.pop()
    assert 'first' == populated_stack.pop()
    with pytest.raises(AttributeError):
        assert populated_stack.pop()


@pytest.fixture(scope='function')
def empty_stack(request):
    empty = st.Stack()
    return empty


@pytest.fixture(scope='function')
def populated_stack(request):
    populated = st.Stack()
    populated.push('first')
    populated.push('second')
    populated.push('third')
    populated.push('fourth')
    return populated
