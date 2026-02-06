class SanalBebek():
    def __init__(self,isim):
        self.isim = isim
        self.aclik = 0
        self.enerji = 100

    def oyun_oyna(self):
        print(f"{self.isim} oyun oynuyor... Çok eğlendi!")
        self.enerji -= 20
        self.aclik += 10

    def yemek_ye(self,gelen_yemek):
        print(f"{self.isim} mama yiyor... Ham hum!")
        self.aclik -= gelen_yemek.kalori
        print(f"{self.isim},{gelen_yemek.ad} yedi. Açlık {gelen_yemek.kalori}")


class Mama():
    def __init__(self,ad,kalori):
        self.ad = ad
        self.kalori = kalori
        
boncuk = SanalBebek("Boncuk")
elma = Mama("Elma", 5)
kebap = Mama("Adana Kebap", 50)
boncuk.oyun_oyna()
boncuk.oyun_oyna()
boncuk.yemek_ye(elma)
boncuk.yemek_ye(kebap)
print(f"Boncuk doydu. {boncuk.enerji} {boncuk.aclik}")
