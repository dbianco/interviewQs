from ejercicios.ej2_1 import char_after_before

def test1():
    assert char_after_before("abcXY123XYijk", "XY") == "c13i"

def test2():
    assert char_after_before("dahsYOUTabsdfgYOUTgfdt", "YOUT") == "sagg"

def test3():
    assert char_after_before("dahsYOUTabsdfgYOUTgfdtY", "YOUT") == "sagg"
