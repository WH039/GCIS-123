from node_stack import Stack

def test_creation():
    
    
    test_stack = Stack()

    assert test_stack.is_empty() == True
    assert str(test_stack) == '[]'

def test_push():
    # setup
    stack = Stack()
    # innvoke
    stack.push(1)
    stack.push(2)
    # analyze
    assert stack.is_empty() == False
    assert str(stack) == '[1 -> 2]'

def test_len():
    # setup
    stack = Stack()
    # innvoke
    stack.push(1)
    stack.push(2)
    # analyze
    assert stack.is_empty() == False
    assert len(stack) == 2

def test_peek():
    # setup
    stack = Stack()
    # innvoke
    stack.push(1)
    stack.push(2)
    # analyze
    assert stack.peek == 1

def test_pop():
    # setup
    stack = Stack()
    stack.push(1)
    # innvoke
    value = stack.pop()
    # analyze
    assert stack.pop == 1
    assert str(stack) == '[]'
    assert len(stack) == 0