import random

class Gladyator():
    def __init__(self, isim, can, vurus_gucu):
        self.isim = isim
        self.__can = can      # 🔒 GİZLİ
        self.vurus_gucu = vurus_gucu
    
    def kalan_cani_soyle(self):
        return self.__can     # 🔑 OKUMA İZNİ

    def hasar_al(self, miktar):
        self.__can -= miktar  # 🛠️ DEĞİŞTİRME İZNİ
        if self.__can < 0:
            self.__can = 0

    def saldır(self, rakip):
        hasar = random.randint(5, 25)
        
        # Rakibin fonksiyonunu kullanıyoruz (Doğrusu bu)
        rakip.hasar_al(hasar)
        
        # Güncel canı öğreniyoruz
        yeni_can = rakip.kalan_cani_soyle()
        
        if hasar == 25:
            print(f"{self.isim}, {rakip.isim}'e {hasar} KRİTİK vurdu! (Kalan: {yeni_can})")
        else:
            print(f" {self.isim}, {rakip.isim}'ye {hasar} vurdu. (Kalan: {yeni_can})")

    def __str__(self):
        # DÜZELTME: self.can yerine self.__can yazdık
        return f"{self.isim} | Can: {self.__can} | Güç: {self.vurus_gucu}"        

class Buyucu(Gladyator):
    def saldır(self, rakip):
        sans_zari = random.randint(1, 100)
        
        if sans_zari <= 30:
             at_damage = random.randint(40, 60)
             
             # DÜZELTME: Değişken değil, FONKSİYON kullandık
             rakip.hasar_al(at_damage)
             yeni_can = rakip.kalan_cani_soyle()
             
             print(f"{self.isim} ALEV TOPU ATTI! {at_damage} hasar! (Kalan: {yeni_can})")
        else:
            av_damage = random.randint(5, 10)
            
            # DÜZELTME: Burada da fonksiyon kullandık
            rakip.hasar_al(av_damage)
            yeni_can = rakip.kalan_cani_soyle()
            
            print(f"{self.isim} asasıyla dürttü. {av_damage} vurdu. (Kalan: {yeni_can})")

# --- OYUN ALANI ---
spartacus = Gladyator("Spartacus", 100, 15)
crixus = Buyucu("Merlin", 80, 0)

print(spartacus) # __str__ testi
print(crixus)    # __str__ testi

while True:
    # 1. Spartacus Saldırıyor
    spartacus.saldır(crixus)
    
    # Getter ile kontrol ediyoruz
    if crixus.kalan_cani_soyle() <= 0:
        print(f"{crixus.isim} öldü. {spartacus.isim} kazandı!")
        break
    
    # 2. Büyücü Saldırıyor
    crixus.saldır(spartacus)
    
    if spartacus.kalan_cani_soyle() <= 0:
        print(f" {spartacus.isim} öldü. {crixus.isim} Kazandı!")
        break