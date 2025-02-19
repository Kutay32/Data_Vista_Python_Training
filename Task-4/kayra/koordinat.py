import cv2
import numpy as np

# park alanı boy
car_spot_width = 106
car_spot_height = 46
video_yolu = 'C:/Users/TAS KAFA/Downloads/carPark.mp4'

# global 
selected_carSpot = []
is_video_playing = False

def mouse_click_events(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        selected_carSpot.append((x, y))
        print(f"Seçilen Park Yeri İşaretlendi: ({x}, {y})")

def main():
    global is_video_playing
    
    cap = cv2.VideoCapture(video_yolu)
    if not cap.isOpened():
        print("ERROR! Video Dosyası Açılmadı.")
        return
    
    ret, frame = cap.read()
    if not ret:
        print("ERROR! İstenilen Kare Alınmadı.")
        return
    
    window_name = "Park Alanları İşaretleme"
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, mouse_click_events)
    
    print("Kontroller:")
    print("- Park alanı işaretlemek için fare sol tuş")
    print("- Video oynatmak/durdurmak için SPACE tuşu")
    print("- Çıkmak için 'q' tuşu")
    
    current_frame = frame.copy()
    
    while True:
        frame_to_show = current_frame.copy()
        
        # işaretlenmiş
        for (x, y) in selected_carSpot:
            cv2.rectangle(frame_to_show, (x, y),(x + car_spot_width, y + car_spot_height), (0, 255, 0), 2)
        
        # güncel
        cv2.imshow(window_name, frame_to_show)
        
        # tuş
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord(' '):  # Space tuşu
            is_video_playing = not is_video_playing
            print("Video: " + ("Oynatılıyor" if is_video_playing else "Duraklatıldı"))
            
        # durdur başlat
        if is_video_playing:
            ret, frame = cap.read()
            if ret:
                current_frame = frame.copy()
            else:
                # Video bittiğinde başa sar
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                ret, frame = cap.read()
                if ret:
                    current_frame = frame.copy()
                    is_video_playing = False
                    print("Video başa sarıldı ve duraklatıldı")
    
    
    print("\nİşaretlenen park yerleri koordinatları:")
    print(selected_carSpot)
    
    # kapatma
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
