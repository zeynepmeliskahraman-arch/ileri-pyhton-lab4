import time
from functools import wraps

def sure_olc(func):
    """Fonksiyonun çalışma süresini ölçen dekoratör."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = func(*args, **kwargs)
        bitis = time.perf_counter()
        sure = bitis - baslangic
        print(f"{func.__name__}: {sure:.4f} sn")
        return sonuc
    return wrapper

def say(func):
    """Fonksiyonun kaç kez çağrıldığını bir nitelikte sayan dekoratör."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.cagri += 1
        return func(*args, **kwargs)
    wrapper.cagri = 0
    return wrapper

def log_cagri(func):
    """Fonksiyon adını, argümanlarını ve dönüş değerini loglayan dekoratör."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Konumsal ve adlı argümanları formatlama
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        imza = ", ".join(args_repr + kwargs_repr)
        
        # Çağrı öncesi log
        print(f"-> {func.__name__}({imza})")
        
        # Fonksiyonu çalıştır ve sonucu al
        sonuc = func(*args, **kwargs)
        
        # Çağrı sonrası (dönüş değeri) log
        print(f"<<- {func.__name__} {sonuc!r}")
        return sonuc
    return wrapper

def sinirla(min_deger=0, max_deger=100):
    """Fonksiyona gelen sayısal argümanları belirtilen min ve max değerler arasında sınırlandıran dekoratör."""
    def dekorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Konumsal argümanları sınırla (sayısal ise)
            yeni_args = [
                max(min_deger, min(max_deger, arg)) if isinstance(arg, (int, float)) else arg 
                for arg in args
            ]
            # Adlı argümanları sınırla (sayısal ise)
            yeni_kwargs = {
                k: max(min_deger, min(max_deger, v)) if isinstance(v, (int, float)) else v 
                for k, v in kwargs.items()
            }
            return func(*yeni_args, **yeni_kwargs)
        return wrapper
    return dekorator