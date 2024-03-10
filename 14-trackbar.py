import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((512,512,3), np.uint8)        # bir tane matris oluşturdum ben burada.
cv2.namedWindow("image")


swicth = "0:OFF,1:ON"
cv2.createTrackbar("R", "image", 0, 255, nothing)   # ben burada TrackBar larımı oluşturdum.İlk başta ismini
cv2.createTrackbar("G", "image", 0, 255, nothing)   # ardından hangi pencereye ait olacağını ardından bu 
cv2.createTrackbar("B", "image", 0, 255, nothing)   # oluşturmuş olduğumuz TrackBar'ın sayı değer aralığı 
cv2.createTrackbar(swicth, "image", 0, 1, nothing)  # ve en son bu değiştiği anda çalışacak bir fonksiyonun
# varsa onu yazıyorsun.

'''
Boş bir Fonksiyon Tanımlama (nothing): cv2.createTrackbar fonksiyonu, bir trackbar'ın değeri 
değiştirildiğinde çağrılacak bir fonksiyona ihtiyaç duyar. Ancak, bu örnekte bu fonksiyonu kullanmıyorsunuz, 
bu nedenle boş bir fonksiyon tanımlanmış (nothing fonksiyonu).
'''


while True:
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    r = cv2.getTrackbarPos("R", "image")          
    g = cv2.getTrackbarPos("G", "image")        
    b = cv2.getTrackbarPos("B", "image")           
    s = cv2.getTrackbarPos(swicth, "image")

# 'getTrackbarPos' --> bunun sonucu herzaman bir sayıyı döndürür.ben TrackBar oluştururken bu sayı aralığını
# zaten belirliyorum.
 
    if s == 1:
        img[:] = [b,g,r]
    if s == 0:
        img[:] = [0,0,0]


cv2.destroyAllWindows()
