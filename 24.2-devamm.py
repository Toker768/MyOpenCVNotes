import cv2
import numpy as np

'''
textimg = cv2.imread("1contour.png")
gray = cv2.cvtColor(textimg,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Köşe bulma parametrelerini ayarlama
maxCorners = 3
qualityLevel = 0.01
minDistance = 10
corners = cv2.goodFeaturesToTrack(gray, maxCorners, qualityLevel, minDistance)

# Köşeleri np.int0 veri tipine dönüştürme
corners = np.int0(corners)

# Köşeleri çizme
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(textimg, (x, y), 3, (0, 0, 255), -1)

# Görüntüyü gösterme
cv2.imshow("Köşeler", textimg)

# Bekleme ve pencereleri kapatma
cv2.waitKey(0)
cv2.destroyAllWindows()
'''



# şimdi de kenar bulabilen bir tane yazalım.bakalım

cap = cv2.VideoCapture(0)   # Bu fonksiyon, videodaki kareleri (frame'leri) bir diziye atar ve 
                            # bu diziyi cap adında bir değişkene atar.
while 1:
    reply, frame = cap.read()

    if reply == False:
        break

    frame = cv2.flip(frame,1)

    edges = cv2.Canny(frame,100,180)
    '''
    threshold1: Kenar olarak kabul edilecek piksellerin minimum gradyan büyüklüğünü belirler.Bu değeri 
    yüksek tutarsan, sadece çok belirgin kenarlar seçilir.

    threshold2: Yüksek eşik değerini karşilamayan, ancak kenar olarak kabul edilebilecek 
    piksellerin minimum gradyan büyüklüğünü belirler.Bu değeri düşük tutarsan, daha zayıf kenarlar da seçilir.
    Bir pikselin kenar olarak kabul edilebilmesi için gradyan değerinin belirli bir eşik 
    değerini aşmasi gerekir.
    '''
# ben eğerki x1>x2 yaparsam cızıltılar olucaktır yani kenar olmayan yerleri bile sana kenar diye gösterecektir
# eşit tuttuğun taktirde ne olur bakalım hala istediğim performansda olmadığı aşıkar
# fazla abartmamak şarti ile x2>x1 den olması daha iyidir.

    cv2.imshow("Frame", frame)
    cv2.imshow("Edges", edges)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release
cv2.destroyAllWindows()




