# Smart Elevator Simulation
# Developed by Emirhan Kandemir
# Concept: While Loops, Input Validation, State Management

import time

# 1. HAFIZA (State): Asansör başlangıçta zemin katta
floor = 0 

print("--- SMART ELEVATOR SYSTEM ---")
print("Type 'exit' to turn off the system.\n")

while True:
    print(f"-----------------------------------")
    print(f"[SYSTEM INFO] Current Floor: {floor}")
    print(f"-----------------------------------")
    
    # 2. GİRDİ (Input)
    giris = input('Enter destination floor (0-10) or "exit": ').strip().lower()

    # 3. ÇIKIŞ KONTROLÜ
    if giris == "çıkış" or giris == "exit":
        print("System shutting down... Goodbye!")
        break 

    # 4. SAYIYA ÇEVİRME VE HATA YÖNETİMİ
    try:
        hedef_kat = int(giris) 
    except ValueError:
        print(">>> ERROR: Please enter a valid number!")
        continue 

    # 5. MANTIK KONTROLLERİ (Logic)
    
    # A) Zaten aynı kattaysak
    if hedef_kat == floor:
        print(">>> ALERT: You are already on this floor.")
        continue
    
    # B) Geçersiz kat (0-10 dışı)
    elif hedef_kat < 0 or hedef_kat > 10:
        print(">>> ERROR: Invalid floor! Please select between 0-10.")
        continue 

    # 6. EYLEM (Action)
    else:
        # Görsellik için yön belirleme
        yon = "Going UP ▲" if hedef_kat > floor else "Going DOWN ▼"
        print(f"{yon} - Moving from {floor} to {hedef_kat}...")
        
        # Simülasyon hissi için minik bir bekleme (Opsiyonel)
        time.sleep(1) 
        
        print(f"Ding Dong! You have arrived at floor {hedef_kat}.")
        
        # ! HAFIZA GÜNCELLEME !
        floor = hedef_kat