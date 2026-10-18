from itertools import islice, takewhile
from uzay_oyunu.akis import fibonacci

def test_fibonacci_genel():
    g = fibonacci()
    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 1

    assert list(islice(fibonacci(), 12)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    kucuk_yuz = list(takewhile(lambda x: x < 100, fibonacci()))
    assert all(x < 100 for x in kucuk_yuz)
    assert 89 in kucuk_yuz
    assert 144 not in kucuk_yuz

def test_fibonacci_tek_kullanimlik():
    g = fibonacci()
    ilk_calisma = list(islice(g, 5))
    ikinci_calisma = list(islice(g, 5))
    assert ilk_calisma != ikinci_calisma