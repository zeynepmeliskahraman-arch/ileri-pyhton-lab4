import pytest
from uzay_oyunu.dekoratorler import sure_olc, say, log_cagri


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

    from uzay_oyunu.dekoratorler import log_cagri

def test_log_cagri(capsys):
    @log_cagri
    def carp(a, b):
        return a * b

    sonuc = carp(3, b=4)
    assert sonuc == 12
    
    # Çıktıların konsola yazılıp yazılmadığını kontrol etme
    yakalanan = capsys.readouterr()
    assert "-> carp(3, b=4)" in yakalanan.out
    assert "<<- carp 12" in yakalanan.out

import pytest
from uzay_oyunu.komutlar import KOMUTLAR, komut, yardim_komutu, envanter_komutu, harita_komutu

def test_komut_kayit_ve_mukerrer():
    # Aynı isimle ikinci kez komut tanımlandığında ValueError fırlatmalı
    with pytest.raises(ValueError):
        @komut("yardim", "tekrar test")
        def sahte_komut(durum):
            pass

def test_komutlar_cikti(capsys):
    durum = {
        "credits": 100,
        "engines": 2,
        "baglantilar": ["orion", "dünya", "kara_delik"]
    }

    # Envanter testi
    envanter_komutu(durum)
    cikis = capsys.readouterr()
    assert "Credits: 100" in cikis.out
    assert "Engines: 2" in cikis.out

    # Harita testi
    harita_komutu(durum)
    cikis = capsys.readouterr()
    assert "orion, dünya, kara_delik" in cikis.out

from uzay_oyunu.dekoratorler import sinirla

def test_sinirla_dekoratoru():
    @sinirla(min_deger=0, max_deger=10)
    def deger_dondur(x):
        return x

    # Sınır içinde olan değer aynı kalmalı
    assert deger_dondur(5) == 5
    # Üst sınırın üzerindeki değer max_deger'e (10) çekilmeli
    assert deger_dondur(15) == 10
    # Alt sınırın altındaki değer min_deger'e (0) çekilmeli
    assert deger_dondur(-5) == 0
    