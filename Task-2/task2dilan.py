import random
import csv
def kullanici_girisi():
    ad = input("Lütfen takma adınızı giriniz: ")
    return ad
def puanlari_yukle():
    try:
        with open('leaderboard.csv') as file:
            reader = csv.reader(file)
            puanlar = {rows[0]: int(rows[1]) for rows in reader}
    except FileNotFoundError:
        puanlar = {}
    return puanlar
def puanlari_kaydet(puanlar):
    with open('leaderboard.csv') as file:
        writer = csv.writer(file)
        for ad, puan in puanlar():
            writer.writerow([ad, puan])

def liderlik_tablosu_goster(puanlar):
    sirali_puanlar = sorted(puanlar.items(), key=lambda x: x[1], reverse=True)[:5]
    print("Liderlik Tablosu:")
    for i, (ad, puan) in enumerate(sirali_puanlar, start=1):
        print(f"{i}. {ad} - {puan} puan")

def zorluk_seviyesi_sec():
    while True:
        print("Zorluk seviyesini seçin: ")
        print("1. Kolay (1-10)")
        print("2. Orta (1-50)")
        print("3. Zor (1-100)")
        secim = int(input("Seçiniz (1/2/3): "))
        if secim == 1:
            return ("Kolay", 10, 10)
        elif secim == 2:
            return ("Orta", 50, 25)
        elif secim == 3:
            return ("Zor", 100, 50)
        else:
            print("Geçersiz seçim.")
            devam = input("Oyuna devam etmek ister misiniz? (E/H): ")
            if devam != 'E':
                return None

def sayi_tahmin_oyunu():
    puanlar = puanlari_yukle()
    ad = kullanici_girisi()
    if ad in puanlar:
        toplam_puan = puanlar[ad]
        print(f"Hoş geldiniz {ad}! Şu anki toplam puanınız: {toplam_puan}")
    else:
        toplam_puan = 0
        puanlar[ad] = toplam_puan

    while True:
        zorluk_seviyesi = zorluk_seviyesi_sec()
        if zorluk_seviyesi is None:
            print("Oyun bitti!")
            break

        zorluk, aralik, puan = zorluk_seviyesi
        rastgele_sayi = random.randint(1, aralik)
        print(f"{zorluk} zorluk seviyesini seçtiniz. {aralik} arasında bir sayı tahmin edin.")

        tahmin_hakki = 5
        while tahmin_hakki > 0:
            tahmin = int(input("Tahmininiz: "))
            tahmin_hakki -= 1
            if tahmin == rastgele_sayi:
                print(f"Tebrikler! Doğru tahmin. {puan} puan kazandınız.")
                toplam_puan += puan
                break
            elif tahmin < rastgele_sayi:
                print("Daha yüksek bir sayı tahmin edin.")
            else:
                print("Daha düşük bir sayı tahmin edin.")

        if tahmin != rastgele_sayi:
            print(f"Maalesef, doğru sayı {rastgele_sayi} idi.")

        puanlar[ad] = toplam_puan
        puanlari_kaydet(puanlar)
        print(f"Oyununuz bitti. {ad}, toplam puanınız: {toplam_puan}")
        liderlik_tablosu_goster(puanlar)

        devam = input("Tekrar oynamak ister misiniz? (E/H): ")
        if devam != 'E':
            print(f"Oyunu bıraktınız. Toplam puanınız: {toplam_puan}")
            break
sayi_tahmin_oyunu()