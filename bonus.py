import time
from uzay_oyunu.akis import aralik

def zamanlayici_calistir():
    print("Zamanlayıcı başladı (10 saniye)...")
    son_tik = 0
    son_tak = 0
    
    for an in aralik(10):
        # Her 2 saniyede bir "tik"
        if int(an) >= son_tik + 2:
            print("tik")
            son_tik += 2
            
        # Her 5 saniyede bir "tak"
        if int(an) >= son_tak + 5:
            print("tak")
            son_tak += 5

if __name__ == "__main__":
    zamanlayici_calistir()