from ejercicios.ej2 import char_after_before

def test_char_ab():
    assert char_after_before("abcXY123XYijk", "XY") == "c13i"
