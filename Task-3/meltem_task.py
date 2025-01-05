import cv2
import matplotlib.pyplot as plt


monkey_image = cv2.imread('C:/Users/Meltem/Downloads/shocked_monkey.jpg')
monkey_rgb = cv2.cvtColor(monkey_image, cv2.COLOR_BGR2RGB)
plt.title('RGB')
plt.imshow(monkey_rgb)
plt.axis('off')
plt.show()


mavi_kanal_monkey = monkey_image.copy()
mavi_kanal_monkey[:, :, 0] = 0
mavi_kanal_monkey[:, :, 1] = 0
plt.imshow(mavi_kanal_monkey)
plt.title('Mavi Kanal')
plt.axis('off')
plt.show()


shocked_guy = cv2.imread('C:/Users/Meltem/Downloads/shocked_guy.png')
shocked_guy_rgb = cv2.cvtColor(shocked_guy, cv2.COLOR_BGR2RGB)
plt.imshow(shocked_guy_rgb)
plt.title('RGB')
plt.axis('off')
plt.show()


shocked_guy_ters = cv2.flip(shocked_guy_rgb, 0)
plt.imshow(shocked_guy_ters)
plt.title('Ters')
plt.axis('off')
plt.show()


shocked_guy_2 = shocked_guy_ters.copy()
cv2.rectangle(shocked_guy_2, pt1=(500, 880), pt2=(700, 1050), color=(255, 0, 0), thickness=6)
plt.imshow(shocked_guy_2)
plt.title('Gözü Saptanmış')
plt.axis('off')
plt.show()


shocked_cat = cv2.imread('C:/Users/Meltem/Downloads/shocked_cat.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(shocked_cat, cmap='gray')
plt.title('Siyah Beyaz')
plt.axis('off')
plt.show()


ret, thresh1 = cv2.threshold(shocked_cat, 127, 255, cv2.THRESH_BINARY)
plt.imshow(thresh1, cmap='gray')
plt.title('Binary')
plt.axis('off')
plt.show()


sobel_x = cv2.Sobel(thresh1, cv2.CV_64F, 1, 0, ksize=5)
plt.imshow(sobel_x, cmap='gray')
plt.title('Binary Sobel')
plt.axis('off')
plt.show()

