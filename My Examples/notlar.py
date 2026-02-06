### Çift mi Tek mi Kontrolü
sayi = 1
if sayi % 2 == 0:
    print("Çift Sayı (Even)")
else:
    print("Tek Sayı (Odd)")

#Döngüler ve Aralıklar(range)
# 1'den 5'e kadar (5 dahil) saymak istiyorsan:
for i in range(1, 6):
    print(i) # 1, 2, 3, 4, 5 yazar.

#Sayaç mantığı (Counter)
#Bir şeyin kaç kere olduğunu saymak için.
sayac = 0
sayac += 1  # 1 artırır (sayac = sayac + 1 ile aynı)
can -= 15   # 15 azaltır

#Random yani Rastgelelik
#Şans faktörü eklemek istersen unutma!
import random

zar = random.randint(1, 6)   # 1 ile 6 dahil sayı tutar
hasar = random.randint(10, 20) # 10 ile 20 arası hasar

#OOP(Nesne Tabanlı Programlama)
#Sınıf Oluşturma
class Gladyator():
    # __init__: Fabrika Ayarları (Doğduğu an çalışan kısım)
    def __init__(self, isim, can):
        self.isim = isim       # Dışarıdan gelen ismi kaydet
        self.can = can         # Dışarıdan gelen canı kaydet
        self.stamina = 100     # Sabit özellik (Herkes 100 başlar)

    # Metot: Nesnenin Yeteneği
    def saldir(self, rakip):
        # self = Ben, rakip = Diğer Oyuncu
        rakip.can -= 15

#Miras Alma (Inheritance)
class Buyucu(Gladyator): # Parantez içine başka bir class alabilir
    pass #kodun çalışmasını istemiyorsan bunu şimdilik pas geç demek için kullan

#Polymorphism(Metot Ezme/Override)
#mesela saldir metotunu değiştirmek için aynı metot ismiyle yazarsam oynama yapabilirim yeni class için
class Buyucu(Gladyator):
    # Gladyatör'deki saldir'i iptal edip bunu kullanır
    def saldir(self, rakip):
        print("Alev Topu Attı!")
        rakip.can -= 50