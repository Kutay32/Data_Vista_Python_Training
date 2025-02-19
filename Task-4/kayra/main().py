import cv2
import numpy as np

# park alan boyu ve yogunluk
car_spot_width = 106
car_spot_height = 46
th_limit = 150
video_yolu = 'C:/Users/TAS KAFA/Downloads/carPark.mp4'

park_spots = [
    (48, 97), (162, 98), (51, 148), (169, 156), (55, 207), (170, 202), (49, 244), 
    (163, 248), (44, 288), (155, 292), (42, 336), (159, 341), (41, 384), 
    (156, 388), (41, 432), (157, 439), (48, 484), (160, 484), (47, 532), 
    (161, 531), (46, 579), (159, 579), (46, 628), (158, 626), (392, 92), 
    (506, 93), (392, 142), (507, 142), (389, 191), (504, 191), (392, 239), 
    (505, 239), (394, 288), (506, 288), (394, 334), (503, 334), (394, 382), 
    (503, 385), (395, 432), (509, 435), (399, 479), (511, 487), (397, 526), 
    (510, 532), (400, 576), (509, 580), (400, 622), (513, 628), (741, 85), 
    (748, 135), (900, 147), (743, 187), (899, 197), (745, 233), (900, 240), 
    (742, 282), (903, 286), (742, 327), (900, 335), (746, 377), (901, 385), 
    (751, 426), (902, 433), (750, 478), (898, 480), (750, 524), (898, 530), 
    (750, 575), (901, 576), (757, 620), (902, 625)
]

def check_spots(frame, spots, car_spot_height, car_spot_width):
    empty_spots = 0
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 1)
    
    binary = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16
    )
    
    threshold = cv2.medianBlur(binary, 5)
    
    for x, y in spots:
        roi = threshold[y:y + car_spot_height, x:x + car_spot_width]
        full_or_empty = cv2.countNonZero(roi)
        
        # yesil(bos)
        if full_or_empty < th_limit:
            color = (0, 255, 0)
            empty_spots += 1
        # kirmizi(dolu)
        else:
            color = (0, 0, 255)
            
        cv2.rectangle(frame, (x, y), (x + car_spot_width, y + car_spot_height), color, 2)
        print(f"Park alanı: ({x}, {y}) Yoğunluk: {full_or_empty} Durum: {'Boş' if color == (0, 255, 0) else 'Dolu'}")
    
    cv2.rectangle(frame, (20, 20), (480, 80), (0, 0, 0), -1)
    
    return frame, empty_spots

def main():
    cap = cv2.VideoCapture(video_yolu)
    if not cap.isOpened():
        print("ERROR! Video dosyası bulunamadı.")
        return
    
    print("Park alanları inceleniyor. Çıkmak isterseniz 'q', ekran görüntüsü için 's' tuşuna basın.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Video okuma hatası!")
            break
            
        checked_frame, empty_spaces = check_spots(frame, park_spots, car_spot_height, car_spot_width)
        
        # bos dolu yazma
        cv2.putText(frame, f"Bos Alanlar: {empty_spaces}/{len(park_spots)}", 
                    (20, 60), cv2.FONT_HERSHEY_COMPLEX, 1.2, (255, 255, 255), 3)
        
        cv2.imshow("Park", frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            cv2.imwrite("C:/Users/TAS KAFA/Downloads/carPark_img.png", frame)
            print("Ekran Görüntüsü Alındı.")
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
