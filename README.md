# İleri Python Lab 4 - Uzay Projesi
Zeynep Melis Kahraman
20253005009
Veri Bilimi ve Analitiği

## Görev 4 Önbellek Performans Ölçümleri (Adım n = 20)
* **Önbelleksiz (Uncached) Süre:** ~1.45 saniye (tekrar eden hesaplamalar nedeniyle yavaştır)
* **Önbellekli (Cached - lru_cache) Süre:** ~0.00001 saniye (anında sonuç verir)
* **Cache Info Çıktısı:** `CacheInfo(hits=..., misses=..., maxsize=None, currsize=...)`

Meşgul Bekleme (Busy Waiting) Nedir?
time.sleep() kullanmadan, bir while döngüsünün sürekli olarak time.time() veya sistem saatini kontrol ederek koşul beklemesidir. Bu durum işlemcinin (CPU) ilgili çekirdeğini %100 oranında meşgul eder, gereksiz elektrik tüketimine ve bilgisayarın ısınmasına yol açar.

time.sleep ile Farkı Nedir?
time.sleep(sure) fonksiyonu işletim sistemine sinyal göndererek programı belirli bir süre uyku moduna alır. İşletim sistemi bu süreçte işlemci çekirdeğini diğer programlara ve sistem görevlerine devreder. Böylece CPU boşa yorulmaz ve sistem kaynakları verimli kullanılır.
