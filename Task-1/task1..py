import random

kart_degerleri = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': [1, 11]
}


def deste_olustur():
    deste = []
    for kart in kart_degerleri :
        for _ in range(4):
            deste.append(kart)
    random.shuffle(deste)
    return deste


def kart_cek(deste):
    return deste


def el_degerini_hesapla(el):
    deger = 0
    aslar = 0
    for kart in el:
        if kart == 'A':
            aslar += 1
        else:
            deger += kart_degerleri[kart]

    for _ in range(aslar):
        if deger + 11 <= 21:
            deger += 11
        else:
            deger += 1

    return deger


def blackjack_oyna():
    bakiye = 500
    while bakiye > 0:
        print(f"Bakiyeniz: {bakiye}")
        while True:
                bahis = int(input("Bahis miktarını giriniz: "))
                if bahis > bakiye:
                    print("Bahis miktarı bakiyenizi geçemez!")
                else:
                    print("Geçerli bir bahis miktarı giriniz.")
                    break

        deste = deste_olustur()
        oyuncu_eli = [kart_cek(deste), kart_cek(deste)]
        dagitici_eli = [kart_cek(deste), kart_cek(deste)]

        print(f"Senin kartların: {oyuncu_eli} (değer: {el_degerini_hesapla(oyuncu_eli)})")
        print(f"Dağıtıcının kartları: [{dagitici_eli[0]}, ?]")

        while True:
            hamle = input("Kart çekmek ister misiniz? (e/h): ")
            if hamle == 'e':
                oyuncu_eli.append(kart_cek(deste))
                print(f"Yeni kartınız: {oyuncu_eli[-1]}")
                print(f"Senin kartların: {oyuncu_eli} (değer: {el_degerini_hesapla(oyuncu_eli)})")
                if el_degerini_hesapla(oyuncu_eli) > 21:
                    print("21'i geçtiniz, kaybettiniz!")
                    bakiye -= bahis
                    break
            else:
                break

        if el_degerini_hesapla(oyuncu_eli) <= 21:
            while el_degerini_hesapla(dagitici_eli) < 17:
                dagitici_eli.append(kart_cek(deste))

            print(f"Dağıtıcının kartları: {dagitici_eli} (değer: {el_degerini_hesapla(dagitici_eli)})")
            oyuncu_degeri = el_degerini_hesapla(oyuncu_eli)
            dagitici_degeri = el_degerini_hesapla(dagitici_eli)

            if dagitici_degeri > 21 or oyuncu_degeri > dagitici_degeri:
                print("Kazandınız!")
                bakiye += bahis
            elif oyuncu_degeri == dagitici_degeri:
                print("Berabere!")
            else:
                print("Kaybettiniz!")
                bakiye -= bahis

        if bakiye <= 0:
            print("Bakiyeniz bitti, oyun bitti.")
            break


blackjack_oyna()
