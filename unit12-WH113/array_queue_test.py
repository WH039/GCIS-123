from array_queue import Queue

def test_creation():
    queue = Queue()

    assert queue.is_empty() == True
    assert str(queue) == '[]'
    assert len(queue) == 0

def test_enqueue():
    queue = Queue()

    queue.enqueue(1)

    assert queue.is_empty() == False
    assert str(queue) == '[1]'
    assert len(queue) == 1

def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    value = queue.dequeue()

    assert queue.is_empty() == False
    assert str(queue) == '[2, 3]'
    assert len(queue) == 2

def test_resize():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue()
    queue.dequeue(5)

    assert str(queue) == '[2, 5]'

