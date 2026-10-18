from itertools import islice, takewhile
from typing import Generator

def fibonacci() -> Generator[int, None, None]:
    """Sonsuz Fibonacci sayıları üreten bir üreteç."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:
    """Her next() çağrısında yakıtı tüketim kadar azaltıp kalan yakıtı üreten üreteç."""
    while yakit > 0:
        yakit -= tuketim
        if yakit < 0:
            yakit = 0
        yield yakit
        if yakit == 0:
            break

import re
from typing import Generator, Tuple

def satirlari_oku(yol: str) -> Generator[str, None, None]:
    """Dosyadaki boş ve # ile başlayan satırları atlayarak satırları üretir."""
    with open(yol, "r", encoding="utf-8") as f:
        for satir in f:
            temiz = satir.strip()
            if temiz and not temiz.startswith("#"):
                yield temiz

def ayristir(satirlar: Generator[str, None, None]) -> Generator[Tuple[str, str, int], None, None]:
    """Her satırdan (kaynak, hedef, yakit) demeti üretir."""
    for satir in satirlar:
        match = re.search(r"(.+?)\s*(?:->|>)\s*(.+?)\s+(\d+)", satir)
        if match:
            kaynak, hedef, yakit = match.groups()
            yield (kaynak.strip(), hedef.strip(), int(yakit))

def uzun_yolculuklar(kayitlar: Generator[Tuple[str, str, int], None, None], esik: int) -> Generator[Tuple[str, str, int], None, None]:
    """Yakıtı eşik değerinden büyük olan yolculukları süzer."""
    for kaynak, hedef, yakit in kayitlar:
        if yakit > esik:
            yield (kaynak, hedef, yakit)

from functools import lru_cache
from typing import Dict, List

def rota_sayaci(baglantilar: Dict[str, List[str]]):
    """Verilen galaksi bağlantılarına göre belirli adımda kaç farklı rota olduğunu hesaplayan önbellekli sayıcı döndürür."""
    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        if adim == 0:
            return 1
        toplam = 0
        komsular = baglantilar.get(gezegen, [])
        for komsu in komsular:
            toplam += rota_sayisi(komsu, adim - 1)
        return toplam
    return rota_sayisi

import time

def aralik(sure: int) -> Generator[float, None, None]:
    """Zamanlayıcı üreteci: Belirtilen süre boyunca geçen zamanı üretir."""
    baslangic = time.time()
    while time.time() - baslangic < sure:
        yield time.time() - baslangic
        time.sleep(0.1)  # CPU'yu yormamak için kısa bir uyku (meşgul beklemeyi önler)
        