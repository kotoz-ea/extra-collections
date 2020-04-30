import pytest

from tests import *
from extra.lists.queue import Queue




def test_creating_empty_queue():
    # empty queue
    q = Queue()
    assert q._max_capacity == float("inf")
    assert len(q) == 0
    assert q.is_empty()
    with pytest.warns(UserWarning): assert q.dequeue() == None
    with pytest.raises(IndexError): q.top()
    q.clear() #not to through any errors
    assert q._max_capacity == float("inf")
    assert not q.is_full()
    # empty queue with max_capacity == 0
    q = Queue(max_capacity=0)
    assert q._max_capacity == 0
    assert len(q) == 0
    assert q.is_empty()
    with pytest.warns(UserWarning): assert q.dequeue() == None
    with pytest.raises(IndexError): q.top()
    with pytest.warns(UserWarning): q.enqueue(get_value() )
    q.clear() #not to through any errors
    assert q._max_capacity == 0
    assert q.is_full()


def test_queue_with_max_capacity():
    cap = get_pos_int()
    lst = get_list(length=cap)
    q = Queue(max_capacity=cap)
    assert q._max_capacity == cap
    for i in lst:
        q.enqueue(i)
    assert len(q) == cap
    assert not q.is_empty()
    assert q.is_full()
    for _ in range(cap):
        assert q.dequeue() == lst.pop(0)
    assert len(q) == 0
    assert q.is_empty()
    assert q.is_full() == False
    q.enqueue(get_value())
    # test max capacity after clear
    q.clear()
    assert q._max_capacity == cap


def test_queue_with_invalid_max_capacity():
    with pytest.raises(TypeError): Queue(max_capacity=get_list())
    with pytest.raises(TypeError): Queue(max_capacity=get_string())
    with pytest.raises(ValueError): Queue(max_capacity=get_neg_int())
    with pytest.raises(ValueError): Queue(max_capacity=get_neg_float())


def test_creating_queue_with_random_values():
    # queue with random values
    lst = get_list(length=100)
    q = Queue()
    for i in lst:
        q.enqueue(i)
    assert len(q) == len(lst)
    assert q.top() == lst[0]
    assert not q.is_empty()
    assert not q.is_full()
    for _ in range(len(lst)):
        assert q.top() == lst[0]
        assert q.dequeue() == lst.pop(0)
    assert len(q) == 0
    assert q.is_empty()
    with pytest.warns(UserWarning): assert q.dequeue() == None
    assert q.is_full() == False


def test_queue_with_known_values():
    q = Queue(max_capacity=3)
    q.enqueue(2)
    q.enqueue(40)
    q.enqueue(800)
    assert len(q) == 3
    with pytest.warns(UserWarning): q.enqueue(16000)
    assert q.top() == 40
    assert q.dequeue() == 40
    assert not q.is_empty()
    assert not q.is_full()
    q.clear()
    assert q.is_empty()
    assert q._max_capacity == 3
    assert q.is_full() == False


def test_enqueue_method():
    q = Queue()
    with pytest.raises(ValueError): q.enqueue(None)
    q.enqueue('')
    q.enqueue(get_value())
    q.enqueue(get_int())
    q.enqueue(get_string())
    q.enqueue(get_float())
    q.enqueue(get_list())


