import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):  # ben eğer TrackBar oluşturacaksam bir fonksiyona ihtiyacım var.elimde bir fonksiyon yok
    pass         # ise işte böyle boş bir fonksiyon oluştururum.

cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 500, 500)

cv2.createTrackbar("Lower - H", "TrackBar", 0, 180, nothing)  # ilk parametre TrackBar'ın ismi sonra TrackBar'
cv2.createTrackbar("Lower - S", "TrackBar", 0, 255, nothing)  # ı koyacağım pencere sonra TrackBar'ın alacağı
cv2.createTrackbar("Lower - V", "TrackBar", 0, 255, nothing)  # değer aralığı ardından bir fonksiyon.
# renk tonu değeri max 180 olur o yüzden 0-180 aralığında.
cv2.createTrackbar("Upper - H", "TrackBar", 0, 180, nothing)
cv2.createTrackbar("Upper - S", "TrackBar", 0, 255, nothing)
cv2.createTrackbar("Upper - V", "TrackBar", 0, 255, nothing)

cv2.setTrackbarPos("Upper - H", "TrackBar", 180) # bir trackbar'ın (izleme çubuğu) mevcut pozisyonunu 
cv2.setTrackbarPos("Upper - S", "TrackBar", 255) # ayarlamak için kullanılır.bu değerlerde varsayılan değerleri
cv2.setTrackbarPos("Upper - V", "TrackBar", 255)

# buradaki H S V nin açılımı da şu şekilde olacak.
# H --> renk tonu(Hue)
# S --> doygunluk(Saturation)
# V --> değer(Value)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("Lower - H", "TrackBar")
    lower_s = cv2.getTrackbarPos("Lower - S", "TrackBar")
    lower_v = cv2.getTrackbarPos("Lower - V", "TrackBar")

    upper_h = cv2.getTrackbarPos("Upper - H", "TrackBar")
    upper_s = cv2.getTrackbarPos("Upper - S", "TrackBar")
    upper_v = cv2.getTrackbarPos("Upper - V", "TrackBar")

    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(frame_HSV, lower_color, upper_color)
    

    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


