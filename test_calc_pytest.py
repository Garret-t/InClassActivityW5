import pytest
from calc import add, sub, multiply, divide

def test_add():
    assert add(1,2) == 3
    assert add(-1,2), 1
    assert add(-1,-2), -3

def test_sub():
    assert sub(2, 1) == 1
    assert sub(1,-2) == 3
    assert sub(-1, 1) == -2
    assert sub(-1,-1) == 0
    
def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(-2, 3) == -6
    assert multiply(2, -3) == -6
    assert multiply(-2, -3) == 6
    assert multiply(0, 1) == 0

def test_divide():
    assert divide(2,1)== 2
    assert divide(-2,1)== -2
    assert divide(-2,-2)== 1
    assert divide(0,1) == 0

def test_divide_zero():
    #Do not want to allow division by 0
    assert divide(1,0) == None