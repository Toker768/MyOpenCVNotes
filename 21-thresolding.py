import cv2 


# öncelikle eşiklemelerin hepsini ben siyah beyaz fotoğraflarda kullandığımı söyleyebilirim.
img = cv2.imread("1Fahrettin_pasa.jpg",0)

ret,th1 = cv2.threshold(img, 150,255, cv2.THRESH_BINARY)
# otsu eşikleme bundan daha iyi sonuçlar verdiğini söyleyebilirim.

'''
ret: Eşikleme işleminin başarı durumunu gösteren bir değişken.
th1: Eşiklenmiş görüntü.
127: Eşik değeri. Bu değerden daha parlak pikseller 255 (beyaz) olarak, daha koyu pikseller 
ise 0 (siyah) olarak atanır.
255: Beyaz piksellerin değeri.
cv2.THRESH_BINARY: Eşikleme yöntemi. Bu yöntem, pikselleri siyah veya beyaz olarak ikiye ayırır.
'''

#cv2.imshow("Ustad", img)
cv2.imshow("Ustad-TH1", th1)


cv2.waitKey(0)
cv2.destroyAllWindows()

# peki eşikleme neden yapılır ve nerelerde kullanılır ? 
'''
Görüntüyü basitleştirmek: Eşikleme, bir görüntüyü siyah ve beyaz piksellerden oluşan bir 
görüntüye dönüştürerek basitleştirebilir. Bu, görüntü işleme ve analizini kolaylaştırabilir.
Gürültüyü azaltmak: Eşikleme, görüntünün gürültülü bölgelerini ortadan kaldırarak görüntüyü iyileştirebilir.
Nesneleri segmentlemek: Eşikleme, bir görüntüdeki nesneleri arka plandan ayırmak için kullanılabilir.
Kenarları algılamak: Eşikleme, bir görüntüdeki kenarları algılamak için kullanılabilir.
'''
