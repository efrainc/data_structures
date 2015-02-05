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
    populated_stack.push('seven')
    assert 'seven' == populated_stack.top.value
    populated_stack.push(8)
    assert 8 == populated_stack.top.value

def test_pop(populated_stack):
    """Test pop function, with empty and populated stacks."""
    assert 6 == populated_stack.pop()
    assert 5 == populated_stack.pop()
    assert 'fourth' == populated_stack.pop()
    assert 'third' == populated_stack.pop()
    assert 'second' == populated_stack.pop()
    assert 'first' == populated_stack.pop()
    #Test popping from an empty stack to raise an AttrubuteError;
    with pytest.raises(AttributeError):
        assert populated_stack.pop()

def test_str(populated_stack):
    """Test str to return a string version of a literal tuple."""
    assert str(populated_stack) == "(6, 5, 'fourth', 'third', 'second', 'first')"
    # Test string evaluates to a tuple literal
    assert eval(str(populated_stack)) == (6, 5, 'fourth', 'third', 'second', 'first')


@pytest.fixture(scope='function')
def empty_stack(request):
    """Fixture generates empty stack for testing."""
    return st.Stack()


@pytest.fixture(scope='function')
def populated_stack(request):
    """Fixture generates a populated stack."""
    populated = st.Stack()
    populated.push('first')
    populated.push('second')
    populated.push('third')
    populated.push('fourth')
    populated.push(5)
    populated.push(6)
    return populated
