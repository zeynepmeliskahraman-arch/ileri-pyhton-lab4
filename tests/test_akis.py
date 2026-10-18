from itertools import islice, takewhile
import pytest
from uzay_oyunu.akis import (
    fibonacci,
    yakit_gostergesi,
    satirlari_oku,
    ayristir,
    uzun_yolculuklar,
    rota_sayaci,
)

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

def test_yakit_gostergesi():
    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]

    g = yakit_gostergesi(10, 5)
    assert next(g) == 5
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)

def test_seyir_boru_hatti():
    toplam_yakit = sum(y for _, _, y in ayristir(satirlari_oku("veri/seyir.txt")))
    assert toplam_yakit == 88

    kayitlar = ayristir(satirlari_oku("veri/seyir.txt"))
    uzunlar = [hedef for _, hedef, _ in uzun_yolculuklar(kayitlar, 10)]
    assert uzunlar == ['sirius', 'centauri', 'orion', 'kara_delik']

def test_rota_sayaci():
    baglantilar = {
        "dünya": ["sirius", "orion"],
        "sirius": ["orion", "kara_delik"],
        "orion": ["centauri", "sirius"],
        "centauri": ["orion"],
        "kara_delik": []
    }
    say = rota_sayaci(baglantilar)
    assert say("dünya", 3) == 5