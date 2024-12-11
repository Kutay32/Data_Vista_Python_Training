import random
import csv


def oyun_baslat():
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    kullanici_adi = input("Lütfen kullanıcı adınızı girin: ")

    while True:
        zorluk = input("Zorluk seviyesi seçin (kolay, orta, zor veya çıkış): ").lower()
        if zorluk == "kolay":
            return oyna(1, 10, kullanici_adi)
        elif zorluk == "orta":
            return oyna(1, 50, kullanici_adi)
        elif zorluk == "zor":
            return oyna(1, 100, kullanici_adi)
        elif zorluk == "çıkış":
            print("Oyunu bıraktınız.")
            return
        else:
            print("Geçersiz zorluk seviyesi.")


def oyna(alt_sinir, ust_sinir, kullanici_adi):
    sayi = random.randint(alt_sinir, ust_sinir)
    tahmin_sayisi = 0

    while tahmin_sayisi < 5:
        tahmin = int(input(f"{alt_sinir}-{ust_sinir} arasında bir sayı tahmin edin: "))
        tahmin_sayisi += 1
        if tahmin < sayi:
            print("Daha yüksek bir sayı tahmin et.")
        elif tahmin > sayi:
            print("Daha düşük bir sayı tahmin et.")
        else:
            print(f"Tebrikler {kullanici_adi}, doğru tahmin! {5 - tahmin_sayisi} hakkın kaldı.")
            skor = (5 - tahmin_sayisi) * (ust_sinir - alt_sinir + 1)
            skor_kaydet(kullanici_adi, skor)
            return

    print(f"Üzgünüm {kullanici_adi}, doğru sayı: {sayi}")


def skor_kaydet(kullanici_adi, skor):
    with open('lider_tablosu.csv', 'a', newline='') as dosya:
        writer = csv.writer(dosya)
        writer.writerow([kullanici_adi, skor])
    print("Skorunuz kaydedildi.")


if __name__ == "__main__":
    oyun_baslat()