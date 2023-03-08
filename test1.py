import pytest
from calc import Calc

def test_1():
    assert Calc(2,2).suma() == 4

def test_2():
    assert Calc(2,2).resta() == 0

def test_3():
    assert Calc(2,2).prod() == 4

def test_4():
    assert Calc(2,2).div() == 1

def test_5():
    with pytest.raises(ZeroDivisionError):
        Calc(2,0).div

def test_6():
    assert Calc(2,2).mod() == 0