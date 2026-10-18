from functools import reduce, partial

# Örnek galaksi verisi
galaksi_verisi = [
    {"gezegen": "dünya", "komsular": ["sirius", "mars"]},
    {"gezegen": "centauri", "komsular": ["orion"]},
    {"gezegen": "sirius", "komsular": ["orion", "kara_delik"]},
    {"gezegen": "orion", "komsular": ["centauri", "sirius"]},
    {"gezegen": "kara_delik", "komsular": []},
]

def analiz_et(veriler):
    """Galaksi verileri üzerinde map/filter/reduce ve liste üreteci karşılaştırması yapar."""
    
    # 1. Gezegen adlarının büyük harfli listesi
    buyuk_map = list(map(lambda x: x["gezegen"].upper(), veriler))
    buyuk_liste = [v["gezegen"].upper() for v in veriler]
    
    # 2. En az iki bağlantısı olan gezegenler
    iki_plus_filter = list(map(lambda x: x["gezegen"], filter(lambda x: len(x["komsular"]) >= 2, veriler)))
    iki_plus_liste = [v["gezegen"] for v in veriler if len(v["komsular"]) >= 2]
    
    # 3. Toplam bağlantı sayısı
    toplam_reduce = reduce(lambda acc, x: acc + len(x["komsular"]), veriler, 0)
    toplam_sum = sum(len(v["komsular"]) for v in veriler)
    
    return buyuk_liste, iki_plus_liste, toplam_sum

# functools.partial ile hiz=3 sabit yeni fonksiyon türetme
def yolculuk(hiz: int, mesafe: int) -> float:
    """Mesafeyi hıza bölerek süreyi hesaplar."""
    return mesafe / hiz

hizli_yolculuk = partial(yolculuk, hiz=3)

# YORUM: Liste üreteçleri (list comprehension) ve sum() fonksiyonu, 
# lambda ve map/filter'a kıyasla çok daha doğal, sezgisel ve okunabilir bir Python sözdizimi sunar.