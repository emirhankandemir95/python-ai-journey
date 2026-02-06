# Reception Asset Tracking System (RATS)
# Developed by Emirhan Kandemir

verilen_kartlar = {} 

print("--- RESEPSİYON KART SİSTEMİ BAŞLATILDI (RATS) ---")

while True:
    print("\n-------------------------")
    print("1: Kart Ver (Check-out)")
    print("2: Kart Teslim Al (Check-in)")
    print("3: Çıkış")
    print("4: Hakkında") # Yeni seçeneğimiz
    
    islem = input("İşlem Seçiniz: ")

    # SENARYO 1: Kart Verme
    if islem == "1":
        try:
            kart_no = int(input("Vereceğiniz Kart Numarası: "))
            if kart_no in verilen_kartlar:
                print(f"HATA: {kart_no} numaralı kart zaten {verilen_kartlar[kart_no]} isimli kişide!")
            else:
                firma = input("Kimin/Firmanın Adı: ")
                verilen_kartlar[kart_no] = firma
                print(f"BAŞARILI: {kart_no} numaralı kart {firma}'ya teslim edildi.")
        except ValueError:
            print("HATA: Lütfen kart numarası için sadece RAKAM giriniz.")

    # SENARYO 2: Kart Alma
    elif islem == "2":
        try:
            kart_no = int(input("Teslim Alınan Kart Numarası: "))
            if kart_no in verilen_kartlar:
                silinen_kisi = verilen_kartlar[kart_no] 
                del verilen_kartlar[kart_no] 
                print(f"BAŞARILI: {kart_no} numaralı kart {silinen_kisi}'den geri alındı.")
            else:
                print("HATA: Bu kart numarası sistemde 'verilmiş' olarak görünmüyor.")
        except ValueError:
            print("HATA: Lütfen kart numarası için sadece RAKAM giriniz.")

    # SENARYO 3: Çıkış
    elif islem == "3":
        print("Sistem kapatılıyor. İyi nöbetler!")
        break 

    # SENARYO 4: Hakkında
    elif islem == "4":
        print("\n***********************************")
        print("* Developed by Emirhan Kandemir *")
        print("* v1.0 - 2025                  *")
        print("***********************************")
        
        input("Ana menüye dönmek için Enter'a basınız...")
        
        continue

    else:
        print("Geçersiz seçim, lütfen listedeki numaralardan birine basınız.")

    print(f"\n[GÜNCEL DURUM] Dışarıdaki Kartlar: {verilen_kartlar}")