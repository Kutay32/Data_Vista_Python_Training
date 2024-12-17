import random
siralama = [("kuty", 20)]
oyuncu_ad = input("Kullanıcı adınızı girin: ")

def yeniden_oynama():
    yeniden_oyna = input("Yeniden oynamak ister misiniz? (E/H): ")
    if yeniden_oyna.lower() == "e":
        sayi_tahmin_oyunu()
    elif yeniden_oyna.lower() == "h":
        print("Oyun bitti, görüşmek üzere!")
def sayi_tahmin_oyunu():

    print("Zorluk seviyesini seçin:")
    print("1- Kolay (1-10 arası*)")
    print("2- Orta (1-50 arası*)")
    print("3- Zor (1-100 arası*)")
    seviye = int(input("Seçiminiz (1/2/3): "))

    if seviye == 1:
        max_sayi = 10
    elif seviye == 2:
        max_sayi = 50
    elif seviye == 3:
        max_sayi = 100
    else:
        print("Geçersiz seçim.")
        yeniden_oynama()
        return
    bilinmeyen_sayi = random.randint(1, max_sayi)
    tahmin_hakki = 5

    while tahmin_hakki > 0:
        tahmin = int(input(f"1 ile {max_sayi} arasında bir sayı tahmin edin: "))

        if tahmin == bilinmeyen_sayi:
            print(f"Tebrikler! Doğru tahmin ettiniz. {10} puan kazandınız.")
            puan = 10
            for i, (isim, eski_puan) in enumerate(siralama):
                if isim == oyuncu_ad:
                    siralama[i] = (isim, eski_puan + puan)
                    break
            else:
                siralama.append((oyuncu_ad, puan))
            break
        elif tahmin > bilinmeyen_sayi:
            print("Daha küçük bir sayı girin.")
        else:
            print("Daha büyük bir sayı girin.")
        
        tahmin_hakki -= 1
        print(f"Kalan tahmin hakkı: {tahmin_hakki}")

    if tahmin_hakki == 0:
        print(f"Üzgünüm, doğru sayı {bilinmeyen_sayi} idi.")


        print("\n-- En İyi 5 Oyuncu --")
    for i in range(len(siralama)):
        isim, puan = siralama[i]
        print(f"{i + 1}. {isim}: {puan} puan")
    yeniden_oynama()


sayi_tahmin_oyunu()
