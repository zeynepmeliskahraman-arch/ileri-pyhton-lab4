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