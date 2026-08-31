# Assignment 12.1, "list_stack_test.py"
# by Weicheng Huang

from list_stack import Stack

def test_creation():
    # setup

    # invoke
    stack = Stack()
    # analyze
    assert stack.is_empty() == True
    assert str(stack) == '[]'

def test_push():
    # setup
    stack = Stack()
    # invoke
    stack.push(1)
    first_push = str(stack)
    stack.push(2)
    # analyze
    assert stack.is_empty() == False
    assert first_push == '[1]'
    assert str(stack) == '[1, 2]'

def test_pop():
    # setup
    stack = Stack()
    # invoke
    stack.push(1)
    stack.push(2)
    pop = stack.pop()
    # analyze
    assert stack.is_empty() == False
    assert str(stack) == '[2]'
    assert pop == 1

def test_peek():
    # setup
    stack = Stack()
    # invoke
    stack.push(1)
    stack.push(2)
    stack.push(3)
    peek = stack.peek()
    # analyze
    assert stack.is_empty() == False
    assert peek == 1