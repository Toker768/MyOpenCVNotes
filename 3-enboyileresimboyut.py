'''
import cv2

def resizeWithRatio(img, width=None, height=None, inter=cv2.INTER_AREA):

    dimension = None
    (h, w) = img.shape[:2]

    if width is None and height is None:
        return img

    if width is not None:
        r = width / float(w)
        dimension = (width, int(h*r))
    
    elif height is not None:
        r = height / float(h)
        dimension = (int(w*r), height)

    return cv2.resize(img, dimension, interpolation=inter)

img = cv2.imread("cakma_asker.jpg")
img1 = resizeWithRatio(img, width=None, height=400, inter=cv2.INTER_AREA)

cv2.imshow("Original", img)
cv2.imshow("Resized", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# ------------------------------------------------------------------------------------------------------------------


import cv2

def resizeWithRatio(img, width=None, height=None, inter=cv2.INTER_AREA):

    '''
    burada bizim soru sormamız gereken yer "inter=cv2.INTER_AREA" kısmı bu ne işe yarar ?
    
    inter=cv2.INTER_AREA, görüntünün yeniden boyutlandırılması sırasında kullanılan interpolasyon yöntemini
    belirtir. Interpolasyon, bir pikselin değerinin bilinen piksel değerleri arasında nasıl hesaplandığını 
    ifade eder.

    Bu özellikle, görüntü boyutları değiştiğinde piksellerin nasıl hesaplanacağını belirlemek için önemlidir.
    OpenCV'de yaygın olarak kullanılan interpolasyon yöntemlerinden biri cv2.INTER_AREA'dir. Bu özellikle
    görüntüyü küçültürken kullanılır ve piksel değerlerini alan pikseller arasında bir alanın ortalaması
    olarak hesaplar.

    Yani, inter=cv2.INTER_AREA ifadesi, görüntüyü küçültme işleminde daha iyi sonuçlar veren bir interpolasyon
    yöntemi seçtiğini belirtir. Başka bir durumda, görüntüyü büyütürken farklı bir interpolasyon yöntemi seçilebilir.

    Diğer yaygın interpolasyon yöntemleri arasında şunlar bulunur:

    cv2.INTER_LINEAR: Piksel değerlerini doğrusal bir şekilde hesaplar, bu da genellikle görüntüleri büyütürken
    kullanılır.

    cv2.INTER_CUBIC: Piksel değerlerini kübik bir polinom kullanarak hesaplar, bu da genellikle daha yüksek
    kaliteli büyütme işlemleri için kullanılır.

    cv2.INTER_NEAREST: En yakın komşu interpolasyonunu kullanır, bu da genellikle daha basit ve daha hızlı
    bir interpolasyon yöntemidir.

    Bu yöntemler, görüntü işleme işlemlerinde kullanılan farklı interpolasyon stratejilerini temsil eder
    ve uygulamanıza göre hangi yöntemin en uygun olduğunu seçebilirsiniz. 
    ben eğer görüntüde değişiklikler yaptığımda bir interpolosyon kullanabilirim.

    peki ben bu interpolosyon türlerimi neye göre belirliyorum burada?
    eğer ben küçültme ve basit işlemler yapıyorsam cv2.INTER_LINEAR
    karmaşık işlemeler var ise: cv2.INTER_CUBIC
    Hesaplama maliyeti önemliyse ve daha basit bir interpolasyon yeterliyse,
    en yakın komşu interpolasyonu (örneğin cv2.INTER_NEAREST
    '''


    dimension = None
    (h, w) = img.shape[:2]   # buradaki shape de genelde 3 parametre alabilir. yükseklik, genişlik, renkkanalları
    # [:2] de ilk 2 tanesi için değerleri alsın bunları da h ve w 'ye sabitlesin.

    if width is None and height is None:
        return img

    if width is not None:
        r = width / float(w)
        dimension = (width, int(h*r))
    
    elif height is not None:
        r = height / float(h)
        dimension = (int(w*r), height)

    return cv2.resize(img, dimension, interpolation=inter)

img = cv2.imread("cakma_asker.jpg")
img1 = resizeWithRatio(img, width=200, height=400, inter=cv2.INTER_AREA)

cv2.imshow("Original", img)
cv2.imshow("Resized", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

# aslında bana bu kod bana yüksekliği veya genişliği verilen bir görselin nasıl orantılı bir şekilde ayarlanacağını
# gösterdi bana.

