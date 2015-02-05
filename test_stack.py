# Test file for stack.py
# Authors Mark, Efrain, Henry

import pytest
import stack as st

def test_init():
    """Test stack constructor."""
    a = st.Stack()
    assert isinstance(a, st.Stack)

def test_push(populated_stack):
    """Test push function, with empty and populated stacks."""



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
    populated.push('four')
    return populated