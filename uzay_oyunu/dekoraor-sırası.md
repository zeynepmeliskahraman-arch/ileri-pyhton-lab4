# Fibonacci Çağrı Sayısı ve Dekoratör Sıralaması Analizi

fib(20) için farklı dekoratör kombinasyonlarıyla elde edilen çağrı sayıları ve nedenleri:

1. **Yalnızca @say : 21891**
   - *Neden:* Özyinelemeli (recursive) Fibonacci fonksiyonu her adımda alt dallara ayrıldığı için aynı değerleri tekrar tekrar hesaplar ve fonksiyon gövdesine binlerce kez girilir.

2. **@say üstte, @lru_cache altta: 39**
   - *Neden:* `@lru_cache` en altta çalıştığı için daha önce hesaplanan sonuçlar önbellekten çekilir ve fonksiyon gövdesine (dolayısıyla `@say`'e) çok daha az sayıda girilmesine izin verir. Ancak sayacımız en üstte olduğu için cache'e takılmadan önce dış katmanda bazı çağrılar sayılır.

3. **@lru_cache üstte, @say altta: 21**[cite: 3]
   - *Neden:* `@lru_cache` dışarıda olduğu için önbellekten dönen sonuçlar hiç içerideki fonksiyonu tetiklemez. Sadece ilk kez hesaplanan benzersiz 20-21 adım sayılır. *(Not: Bu durumda sayaca `fib._wrapped.cagri` veya sarmalama yapısına göre erişilir).*[cite: 3]
   