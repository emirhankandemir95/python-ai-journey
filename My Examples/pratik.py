def bio_olustur(isim,yas,meslek):
    return f"Ben {isim}, {yas} yaşındayım ve {meslek} olarak çalışıyorum."

emir = bio_olustur("Emir",30,"Yazılımcı")
print(emir)


def kargo_hesapla(sepet_tutari):
    if sepet_tutari >= 500:
        return sepet_tutari
    else:
        return sepet_tutari + 50
    
kargo = kargo_hesapla(100)
print(kargo)

def sifre_kontrol(sifre):
    if len(sifre) >= 8:
        return True
    else:
        return False

strong_password = sifre_kontrol("qqqq1234")
if strong_password:
    print("Şifre oluşturuldu.")
else:
    print("Şifre çok kısa")
