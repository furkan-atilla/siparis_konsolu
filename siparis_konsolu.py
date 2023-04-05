#sıparıs_sozlugu_olusturuluyor
siparisler = {}

def siparis_ekle():
    siparis_adi = input("Sipariş Adı: ")
    siparis_fiyati = float(input("Siparişin Fiyatı: "))
    siparis_miktari = int(input("Siparişin Miktarı: "))
    siparisler[siparis_adi] = {"fiyat": siparis_fiyati,
                               "miktar": siparis_miktari}
    print("Sipariş Eklendi!\n")
    
def siparis_listele():
    if not siparisler:
        print("Kaydedilmiş bir sipariş yoktur.\n")
    else:
        print("Siparişler: ")
        toplam_fiyat = 0
        for ad, ozellikler in siparisler.items():
            fiyat = ozellikler["fiyat"]
            miktar = ozellikler["miktar"]
            toplam = fiyat*miktar
            toplam_fiyat= toplam_fiyat+toplam
            print(ad+": "+str(fiyat)+" x "+str(miktar)+" = "+str(toplam))
        print("Toplam Fiyat: "+str(toplam_fiyat)+"\n")

def siparis_sil():
    siparis_adi = input("Silinecek Siparişin Adı: ")
    if siparis_adi in siparisler:
        del siparisler[siparis_adi]
        print(siparis_adi+" Siparişi Silindi.\n")
    else:
        print("Bu isimde bir sipariş yoktur.\n")

def siparis_duzenle():
    siparis_adi = input("Düzenlenecek Sipariş Adı: ")
    if siparis_adi in siparisler:
        print("Şu anki sipariş detayları: "+str(siparisler[siparis_adi]))
        fiyat = float(input("yeni fiyat: "))
        miktar = int(input("yeni miktar: "))
        siparisler[siparis_adi] = {"fiyat": fiyat, "miktar": miktar}
        print(siparis_adi+" siparişi düzenlendi.\n")
    else:
        print("Bu isimde bir sipariş yoktur.\n")

while True:
    print("Yapabileceğiniz İşlemler: ")
    print("1. Sipariş Ekle")
    print("2. Siparişleri Listele")
    print("3. Sipariş Sil")
    print("4. Sipariş Düzenle")
    print("5. Çıkış")
    secim = input("Seçiminiz (1-5): ")
    
    if secim == "1":
        siparis_ekle()
    elif secim == "2":
        siparis_listele()
    elif secim == "3":
        siparis_sil()
    elif secim == "4":
        siparis_duzenle()
    elif secim == "5":
        print("Hoşçakalınız..")
        break
    else:
        print("Geçersiz seçim!\n")

    
    
        
        
 
        
        
    
    
    
    


    



