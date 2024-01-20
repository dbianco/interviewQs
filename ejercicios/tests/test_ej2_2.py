from ejercicios.ej2_2 import *

def test1():
    assert groupSum([2, 4, 8], 10) == True

def test2():
    assert groupSum([6, 1], 10) == True

def test3():
    assert groupSum([5], 10) == True


def test4():
    assert groupSum3elem([2, 4, 8], 10) == True

def test5():
    assert groupSum3elem([2, 4, 8], 9) == False
