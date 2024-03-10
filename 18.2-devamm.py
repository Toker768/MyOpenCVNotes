import cv2

img1 = cv2.imread("1bitwase.png")
img2 = cv2.imread("1bitwase1.png")


diff = cv2.absdiff(img1, img2)  # different'dan geliyor.iki fotograf arasında matrislerin farklarını alıyor.     
# farklı çıkan yerler beyaz aynı çıkan yer varsa siyah oluyor.


cv2.imshow("Farklar", diff)
cv2.imshow("Myimg1", img1)
cv2.imshow("Myimg2", img2)


cv2.waitKey(0)
cv2.destroyAllWindows()

# bence bitwise işlemleri renkli fotoğraflardan daha ziyade siyah beyaz olan fotoğraflarda daha fazla
# kullanılır.bunun açıklamasını gemini şöyle yapıyor:
'''
1. Renkli Fotoğrafların Karmaşıklığı:
Renkli fotoğraflar, kırmızı, yeşil ve mavi kanallardan oluşan üç boyutlu bir veri kümesidir. 
Her kanal, 0'dan 255'e kadar değerlere sahip 8 bitlik bir tamsayı dizisidir. Bu, renkli fotoğrafları 
işlemenin siyah beyaz fotoğraflara göre daha karmaşık ve zorlayıcı hale getirir.

2. Bitwise İşlemlerin Basitliği:
Bitwise işlemler, tek bitlik değerler üzerinde çalışır. Bu, siyah beyaz fotoğraflar için idealdir, 
çünkü her piksel tek bir bit ile temsil edilir. Renkli fotoğraflar için ise her piksel üç bit ile temsil 
edilir ve bu da bitwise işlemleri daha karmaşık hale getirir.

3. Renkli Fotoğraflarda Bitwise İşlemlerin Kullanım Alanları:
Renkli fotoğraflarda bitwise işlemler kullanılabilir, ancak kullanım alanları siyah beyaz fotoğraflara 
göre daha sınırlıdır. Bazı yaygın kullanım alanları şunlardır:

Renk Kanallarını Ayırma: Kırmızı, yeşil ve mavi kanalları ayrı ayrı işlemek için bitwise işlemler 
kullanılabilir.
Renk Maskeleri Oluşturma: Belirli renkleri veya renk aralıklarını seçmek için bitwise işlemler kullanılabilir.
Görüntü Birleştirme: Farklı renk kanallarından gelen görüntüleri birleştirmek için bitwise 
işlemler kullanılabilir.

Sonuç:
Bitwise işlemler, siyah beyaz fotoğraflar için çok kullanışlı bir araçtır. 
Renkli fotoğraflar için de kullanılabilir, ancak kullanım alanları daha sınırlıdır. Renkli fotoğraflarda 
bitwise işlemler kullanırken dikkat edilmesi gereken bazı önemli noktalar vardır.
'''
