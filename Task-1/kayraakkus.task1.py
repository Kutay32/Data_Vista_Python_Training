import random

# Kart değerleri
kart_degerleri = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "A": 10, "K": 10, "Q": 10,
                  "J": 11}


# deste
def tum_deste():
    kartlar = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "K", "Q", "J", "2", "3", "4", "5", "6", "7", "8", "9",
               "10", "A", "K", "Q", "J", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "K", "Q", "J", "2", "3",
               "4", "5", "6", "7", "8", "9", "10", "A", "K", "Q", "J"]
    random.choice(kartlar)
    return kartlar


# A 1 ya da 11(yardim alindi)
def skor_hesaplama(el):
    skor = sum(kart_degerleri[kart] for kart in el)
    if "A" in el and skor > 21:
        skor -= 10
    return skor


# oyunu başlatma
def blackjack_baslatma():
    bakiye = 1000
    deste = tum_deste()

    while True:
        print("\nSeytaniniz bol olsun. (^-^) ")
        print("1- Oyunu Başlat*")
        print("2- Bakiye Sorgula*")
        print("3- Masadan Kalk*")

        menü_secimi = input("Menüden isteğinizi seçin. (1/2/3): ")

        if menü_secimi == "1":
            bahis = int(input("Bahsinizi yapin: $"))
            if bahis > bakiye:
                print("Bakiyeniz Yeterli Degil.")
                continue

            oyuncu_eli = [deste.pop(), deste.pop()]
            krupiye_eli = [deste.pop(), deste.pop()]

            print(f"Kartin: {oyuncu_eli}, Kartlarinin Puani: {skor_hesaplama(oyuncu_eli)}")
            print(f"Krupiyerin ilk karti: {krupiye_eli[0]}")

            while skor_hesaplama(oyuncu_eli) < 21:
                kart_cek_dur = input("Başka bir kart almak için 'y' veya pas geçmek için 'n' yazin: ")
                if kart_cek_dur == "y":
                    oyuncu_eli.append(deste.pop())
                    print(f"Kartin: {oyuncu_eli}, Karlarinin Puani: {skor_hesaplama(oyuncu_eli)}")
                elif kart_cek_dur == "n":
                    break
                else:
                    print("Geçersiz giriş! lütfen 'y' ya da 'n' giriniz.")

            while skor_hesaplama(krupiye_eli) < 17:
                krupiye_eli.append(deste.pop())

            print(f"Elinin son hali: {oyuncu_eli}, Elinin son skoru: {skor_hesaplama(oyuncu_eli)}")
            print(f"Krupiye'nin son eli: {krupiye_eli}, Krupiye'nin son skoru: {skor_hesaplama(krupiye_eli)}")

            oyuncu_skor = skor_hesaplama(oyuncu_eli)
            krupiye_skor = skor_hesaplama(krupiye_eli)

            if oyuncu_skor > 21:
                print("Kaybettin 21'i gectin!")
                bakiye -= bahis

            elif krupiye_skor > 21 or oyuncu_skor > krupiye_skor:
                print("Kazandin.")
                bakiye += bahis

            elif oyuncu_skor < krupiye_skor:
                print("Kaybettin!")
                bakiye -= bahis

            else:
                print("Berabere.")




        elif menü_secimi == "2":
            print(f"Toplam Bakiye: ${bakiye}")




        elif menü_secimi == "3":
            print("Seytaniniz bol olsun (^-^) ")
            break




        else:
            print("Yanlis secim, menüden secim yapin.")

        print("---------")


blackjack_baslatma()
