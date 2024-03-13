# Şimdi biz bu dersde histogram kullanıcağız.Peki ben bu histogramı neden kullanırım nerelerde benim işime
# yarar?
'''
Görüntü Özelliklerini Anlamak:
Görüntünün parlaklık ve kontrast dağılımını analiz etmek için kullanılabilir.
Görüntüdeki piksellerin renk ve ton dağılımını analiz etmek için kullanılabilir.

Görüntü eşitleme: Görüntünün kontrastını ve parlaklığını geliştirmek için kullanılabilir.
Görüntü segmentasyonu: Görüntüyü farklı bölgelere ayırmak için kullanılabilir.
Nesne tanıma: Görüntülerdeki nesneleri tanımlamak için kullanılabilir.
Doku analizi: Görüntünün dokusunu analiz etmek için kullanılabilir.

Görüntü Kalite Değerlendirmesi:
Görüntünün gürültü seviyesini ve bulanıklığını değerlendirmek için kullanılabilir.

Görüntünün keskinliğini ve netliğini değerlendirmek için kullanılabilir.

Görüntü Karşılaştırma:
İki görüntünün ne kadar benzer veya farkli olduğunu karşılaştırmak için kullanılabilir.
Görüntüdeki değişiklikleri takip etmek için kullanılabilir.

Histogram Kullanmanın Avantajları:
Hesaplaması basittir.
Görüntü hakkında birçok bilgi sağlayabilir.
Farklı görüntü işleme görevlerinde kullanılabilir.

Histogram Kullanmanın Dezavantajları:
Görüntünün uzamsal bilgilerini dikkate almaz.
Aydınlatma koşullarındaki değişikliklerden etkilenebilir.
Gürültüden etkilenebilir.
'''


import cv2
from matplotlib import pyplot as plt


# img = np.zeros((500,500), np.uint8)

# plt.hist(img.ravel(),256,[0,256])
# '''
# img.ravel(): Görüntüyü tek boyutlu bir diziye dönüştürür.Bu görüntünün tüm piksel değerleri tek boyutta
# lanacağı anlamına gelir.
# 256: Histogramdaki çubukların sayısını belirtir. Bu, görüntünün 256 farklı parlaklık seviyesine sahip 
# olabileceği anlamına gelir.
# [0,256]: Histogramın x ekseninin aralığını belirtir.
# '''
# plt.show() 

# cv2.imshow("Original", img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# bir örnek ile kafamızda daha iyi oturacaktır.
'''
Diyelim ki img görüntüsünde 10 piksel var ve bunların 5'i 100 parlaklık seviyesine, 
3'ü 150 parlaklık seviyesine ve 2'si 200 parlaklık seviyesine sahip.
img.ravel() fonksiyonu, bu pikselleri [100, 100, 100, 100, 100, 150, 150, 150, 200, 200] 
şeklinde bir diziye dönüştürür.
plt.hist fonksiyonu, bu dizideki her değer için bir çubuk oluşturur.
100 parlaklık seviyesine sahip çubuk 5 birim yüksekliğinde olacaktır.
150 parlaklık seviyesine sahip çubuk 3 birim yüksekliğinde olacaktır.
200 parlaklık seviyesine sahip çubuk 2 birim yüksekliğinde olacaktır.
'''


'''
img = np.zeros((500,500), np.uint8) + 100
cv2.rectangle(img,(0,60), (200,150), (255,255,255), -1)
# (0,60), (200,150) bu 2 nokta benim diktörgenimin sol üst ve sağ alt kısmını simgeliyor.
cv2.rectangle(img,(200,150), (350,400), (255,255,255),thickness=4)

plt.hist(img.ravel(),256,[0,256])
plt.show() 

cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''


'''
img = cv2.imread("1exraction2.jpg")
B,G,R = cv2.split(img)


plt.hist(img.ravel(), bins=1024, range=(0, 256)) # ben burada yatay eksenimde bulunan x değerlerinin
                                                 # sıklığını artırdım.
plt.hist(B.ravel(), bins=1024, range=(0, 256))
plt.hist(G.ravel(), bins=1024, range=(0, 256))
plt.hist(R.ravel(), bins=1024, range=(0, 256))


plt.show()
cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

