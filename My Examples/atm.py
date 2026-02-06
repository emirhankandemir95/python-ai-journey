bakiye = 1000
while True:
    print("\n----------------")
    print("1: Bakiye Sorgula")
    print("2: Para Yatır")
    print("3: Para Çek")
    print("4: Çıkış")

    islem = input('Bir İşlem Seçiniz: ')
    if islem == '1':
        print(f"Mevcut Bakiyeniz: {bakiye} TL")
    elif islem == '2':
        try:
            yatirilan = int(input('Yatırılacak Miktar: '))
            bakiye = bakiye + yatirilan # Bakiyeyi burada güncelliyoruz
            print(f"Yeni Bakiyeniz: {bakiye} TL")
        except ValueError:
            print("HATA: Lütfen sayı giriniz.")
    elif islem == '3':
        try:
            cekilecek = int(input('Çekilecek Miktar: '))
            if cekilecek > bakiye:
                print(">>> HATA: Yetersiz Bakiye! Bu kadar paranız yok.")
            else:
                bakiye = bakiye - cekilecek # Bakiyeyi burada güncelliyoruz
                print(f"Paranız veriliyor... Kalan Bakiye: {bakiye} TL")
        except ValueError:
            print("HATA: Lütfen sayı giriniz.")
    elif islem == '4':
        print("Kartınız iade ediliyor. İyi günler!")
        break
    else:
        print("Geçersiz işlem! Lütfen 1-4 arası bir sayı girin.")