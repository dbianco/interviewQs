from ejercicios.ej1 import sum_men_13


def test_sum_men_13_0():
    assert sum_men_13((2, 5, 14)) == 7

def test_sum_men_13_1():
    assert sum_men_13((3, 5, 0, 13, 12)) == 20

def test_sum_men_13_2():
    assert sum_men_13(()) == 0

