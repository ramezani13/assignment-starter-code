from is_factor import *

def test_factor1():
    assert is_factor(1, 1) is True

def test_factor2():
    assert is_factor(2, 10) is True

def test_factor3():
    assert is_factor(-5, 25) is True

def test_factor4():
    assert is_factor(5, 0) is False

def test_factor5():
    assert is_factor(0, 0) is False

def test_factor6():
    assert is_factor(2, 11) is False

def test_factor7():
    assert is_factor(10, 2) is False

def test_factor8():
    assert is_factor(0, 5) is False

