import cv2
import numpy as np

# Sabitler
PARK_SPOT_WIDTH = 109
PARK_SPOT_HEIGHT = 49
VIDEO_FILE = "carPark.mp4"

# Global değişkenler
selected_park_spots = []
marked_empty_spots = []


def on_mouse_click(event, x, y, flags, params):
    global selected_park_spots, marked_empty_spots
    if event == cv2.EVENT_LBUTTONDOWN:
        marked_empty_spots.append((x, y))
        print(f"Boş park yeri işaretlendi: ({x}, {y})")

        # İşaretlenen yeri yeşil bir dikdörtgenle göster
        cv2.rectangle(frame, (x, y), (x + PARK_SPOT_WIDTH, y + PARK_SPOT_HEIGHT), (0, 255, 0), 2)
        cv2.imshow("Boş Park Yeri Seçimi", frame)


def main():
    # Video dosyasını aç
    cap = cv2.VideoCapture(VIDEO_FILE)
    if not cap.isOpened():
        print("Hata: Video dosyası açılamadı.")
        return

    # İlk kareyi oku
    ret, frame = cap.read()
    if not ret:
        print("Video karesi alınamadı.")
        return

    # İlk kareyi göster ve fare tıklamalarını dinle
    cv2.imshow("Boş Park Yeri Seçimi", frame)
    cv2.setMouseCallback("Boş Park Yeri Seçimi", on_mouse_click)

    print("Boş park yerlerini işaretlemek için tıklayın. Çıkmak için 'q' tuşuna basın.")

    while True:
        # Video karesini oku
        ret, frame = cap.read()
        if not ret:
            print("Video sona erdi veya okuma hatası oluştu.")
            break

        # İşaretlenen boş park yerlerini yeşil dikdörtgenlerle göster
        for (x, y) in marked_empty_spots:
            cv2.rectangle(frame, (x, y), (x + PARK_SPOT_WIDTH, y + PARK_SPOT_HEIGHT), (0, 255, 0), 2)

        # Kareyi göster
        cv2.imshow("Boş Park Yeri Seçimi", frame)

        # 'q' tuşuna basıldığında döngüden çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kaynakları serbest bırak ve pencereleri kapat
    cap.release()
    cv2.destroyAllWindows()

    # İşaretlenen boş park yerlerini ekrana yazdır
    print(f"İşaretlenen boş park yerleri: {marked_empty_spots}")


if __name__ == "__main__":
    main()