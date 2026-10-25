import pytest
from uzay_oyunu.dekoratorler import sure_olc

def test_sure_olc():
    @sure_olc
    def test_fonk(x, y=10):
        """Test docstringi"""
        return x + y

    # 1. __name__ ve __doc__ korunuyor mu?
    assert test_fonk.__name__ == "test_fonk"
    assert test_fonk.__doc__ == "Test docstringi"

    # 2. Adlı argümanlarla çağrı çalışıyor mu ve sonuç doğru dönüyor mu?
    sonuc = test_fonk(5, y=20)
    assert sonuc == 25

    from functools import lru_cache
from uzay_oyunu.dekoratorler import say

def test_say_dekoratoru():
    @say
    def topla(a, b):
        return a + b

    topla(1, 2)
    topla(3, 4)
    
    assert topla.cagri == 2
    