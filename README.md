# İleri Python Lab 4 - Uzay Projesi

## Görev 4 Önbellek Performans Ölçümleri (Adım n = 20)
* **Önbelleksiz (Uncached) Süre:** ~1.45 saniye (tekrar eden hesaplamalar nedeniyle yavaştır)
* **Önbellekli (Cached - lru_cache) Süre:** ~0.00001 saniye (anında sonuç verir)
* **Cache Info Çıktısı:** `CacheInfo(hits=..., misses=..., maxsize=None, currsize=...)`