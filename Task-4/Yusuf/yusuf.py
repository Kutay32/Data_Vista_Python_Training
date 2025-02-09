import cv2
import numpy as np

# Park yeri dikdörtgen boyutları
PARK_GENİŞLİK = 109
PARK_YÜKSEKLİK = 49
YOĞUNLUK_EŞİĞİ = 650
VIDEO_DOSYA_YOLU = "carPark.mp4"

# Özel olarak belirlenen park yeri koordinatları
PARK_POZİSYONLARI = [
    (50, 90), (55, 140), (60, 190), (65, 240), (70, 290),
    (75, 340), (80, 390), (85, 440), (90, 490), (95, 540),
    (200, 95), (205, 145), (210, 195), (215, 245), (220, 295),
    (225, 345), (230, 395), (235, 445), (240, 495), (245, 545),
    (400, 100), (405, 150), (410, 200), (415, 250), (420, 300),
    (425, 350), (430, 400), (435, 450), (440, 500), (445, 550),
    (600, 110), (605, 160), (610, 210), (615, 260), (620, 310),
    (625, 360), (630, 410), (635, 460), (640, 510), (645, 560)
]


def kareyi_işle(kare, pozisyonlar, park_genişlik, park_yükseklik):
    """Gelen videonun her karesini işler ve boş/dolu park yerlerini belirler"""
    gri_kare = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
    bulanık_kare = cv2.GaussianBlur(gri_kare, (3, 3), 1)

    # Adaptif eşikleme ile görüntü işleme
    eşiklenmiş = cv2.adaptiveThreshold(
        bulanık_kare, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16
    )
    temiz_eşik = cv2.medianBlur(eşiklenmiş, 5)

    boş_alan_sayısı = 0

    for x, y in pozisyonlar:
        park_bölgesi = temiz_eşik[y: y + park_yükseklik, x: x + park_genişlik]
        doluluk_sayısı = cv2.countNonZero(park_bölgesi)

        if doluluk_sayısı < YOĞUNLUK_EŞİĞİ:
            renk = (0, 255, 0)  # Yeşil (Boş)
            boş_alan_sayısı += 1
        else:
            renk = (0, 0, 255)  # Kırmızı (Dolu)

        # Park alanlarını işaretleme
        cv2.rectangle(kare, (x, y), (x + park_genişlik, y + park_yükseklik), renk, 2)
        print(f"Park Alanı ({x}, {y}): Yoğunluk = {doluluk_sayısı}, Durum = {'Boş' if renk == (0, 255, 0) else 'Dolu'}")

    # Bilgi ekranı için üst köşeye siyah kutu
    cv2.rectangle(kare, (30, 15), (500, 55), (0, 0, 0), -1)

    return kare, boş_alan_sayısı


def ana_fonksiyon():
    """Ana fonksiyon: Videoyu işler ve boş park alanlarını gösterir"""
    video = cv2.VideoCapture(VIDEO_DOSYA_YOLU)
    if not video.isOpened():
        print("Hata: Video dosyası açılamadı!")
        return

    print("Park alanı tespiti başladı. Çıkmak için 'q', ekran görüntüsü almak için 's' tuşuna basın.")

    while True:
        ret, kare = video.read()
        if not ret:
            print("Video sonlandı veya okuma hatası oluştu.")
            break

        işlenmiş_kare, boş_yerler = kareyi_işle(kare, PARK_POZİSYONLARI, PARK_GENİŞLİK, PARK_YÜKSEKLİK)

        # Boş park yerleri bilgisi ekrana yazdırılıyor
        cv2.putText(işlenmiş_kare, f"Bos Alanlar: {boş_yerler}/{len(PARK_POZİSYONLARI)}",
                    (10, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Otopark Tespiti", işlenmiş_kare)

        tuş = cv2.waitKey(1) & 0xFF
        if tuş == ord('q'):
            break
        elif tuş == ord('s'):
            cv2.imwrite("kaydedilen_kare.jpg", işlenmiş_kare)
            print("Görüntü kaydedildi: kaydedilen_kare.jpg")

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    ana_fonksiyon()
