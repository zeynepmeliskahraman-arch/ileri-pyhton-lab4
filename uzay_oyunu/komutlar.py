# uzay_oyunu/komutlar.py
from functools import wraps

# Kayıtlı komutları tutacak sözlük
KOMUTLAR = {}

def komut(ad, aciklama=""):
    """Komutları kaydeden dekoratör. Aynı adla kayıt yapılırsa ValueError fırlatır."""
    def dekorator(func):
        if ad in KOMUTLAR:
            raise ValueError(f"Bu komut zaten kayıtlı: {ad}")
        # Fonksiyonu değiştirmeden (fonksiyon, aciklama) olarak kaydediyoruz
        KOMUTLAR[ad] = (func, aciklama)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return dekorator

@komut("yardim", "komutları listeler")
def yardim_komutu(durum):
    """Tüm kayıtlı komutları ve açıklamalarını listeler."""
    for ad, (func, aciklama) in KOMUTLAR.items():
        print(f"{ad}: {aciklama}")

@komut("envanter", "envanter eşyalarını gösterir")
def envanter_komutu(durum):
    """Oyuncunun envanterindeki credits ve engines bilgilerini gösterir."""
    credits = durum.get('credits', 0)
    engines = durum.get('engines', 0)
    print(f"Credits: {credits}, Engines: {engines}")

@komut("harita", "gidebileceğin gezegenleri gösterir")
def harita_komutu(durum):
    """Mevcut konumdan gidilebilecek bağlantıları listeler."""
    baglantilar = durum.get('baglantilar', [])
    print(", ".join(baglantilar))
    