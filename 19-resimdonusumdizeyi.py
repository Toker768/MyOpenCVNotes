import cv2
import numpy as np


img = cv2.imread("1ilkaskim.jpg",0)
resizeimg = cv2.resize(img, (680,460))

row, column = resizeimg.shape
# benim shape değerimin 3 parametresi olur bunlar index'e bağlıdır.index'e bağlı olduğu için sırasıyla
# yazarsan böyle her bir değişkene bir değer atanır. ama ben burada görüntümü siyah beyaz yaptım.ilk kod 
# satırımda.
M = np.float32([[1,0,10] , [0,1,30]])
'''
Bu kod, affine dönüşüm matrisini oluşturur. Affine dönüşüm matrisi, bir görüntüyü kaydırmak, 
döndürmek, ölçeklendirmek ve eğmek için kullanılır. Bu matris 2x3 boyutundadır ve aşağıdaki gibi gösterilir:

[
    [a, b, c], [d, e, f]  
]

a ve d: Görüntünün yatay ve dikey olarak ölçeklendirilmesini kontrol eder.
b ve e: Görüntünün eğilmesini kontrol eder.
c ve f: Görüntünün kaydırılmasını kontrol eder.

Matrisin Katsayıları:

a (1): Görüntünün yatay olarak ölçeklendirilme miktarını kontrol eder. a = 1 ise görüntü yatay olarak 
ölçeklendirilmez. a > 1 ise görüntü yatay olarak büyütülür ve a < 1 ise görüntü yatay olarak küçültülür.
b (0): Görüntünün yatay olarak eğilme miktarını kontrol eder. b = 0 ise görüntü yatay olarak eğilmez. 
b > 0 ise görüntü sağa doğru eğilir ve b < 0 ise görüntü sola doğru eğilir.
c (10): Görüntünün yatay olarak kaydırılma miktarını kontrol eder. c = 0 ise görüntü yatay olarak 
kaydırılmaz. c > 0 ise görüntü sağa doğru kaydırılır ve c < 0 ise görüntü sola doğru kaydırılır.
d (0): Görüntünün dikey olarak ölçeklendirilme miktarını kontrol eder. d = 1 ise görüntü dikey olarak 
ölçeklendirilmez. d > 1 ise görüntü dikey olarak büyütülür ve d < 1 ise görüntü dikey olarak küçültülür.
e (1): Görüntünün dikey olarak eğilme miktarını kontrol eder. e = 0 ise görüntü dikey olarak eğilmez. 
e > 0 ise görüntü yukarı doğru eğilir ve e < 0 ise görüntü aşağı doğru eğilir.
f (30): Görüntünün dikey olarak kaydırılma miktarını kontrol eder. f = 0 ise görüntü dikey olarak 
kaydırılmaz. f > 0 ise görüntü aşağı doğru kaydırılır ve f < 0 ise görüntü yukarı doğru kaydırılır.
'''
# M matrisi, görüntüyü yatay olarak 100 piksel ve dikey olarak 300 piksel kaydırır.
dst = cv2.warpAffine(resizeimg,M,(row,column))

cv2.imshow("DST", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

