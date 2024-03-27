import pytest
from calculations import add, subtract, multiply, divide, divide_by_0

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide(10, 0)

def test_divide_by_0():
    assert divide_by_0(10, 0) == 10
    assert divide_by_0(10, 2) == 5
