# büyük veri kümesiyle çalışırken
# karmaşık matamatiksel işlemlerde
# ve veri analizi yaparken ben numPy çok fazla kullanıyorum.
import cv2 
import numpy as np

img = np.zeros((10,10,3), np.uint8)
# ben bunun boyutunu bir değiştiriyim bakalım.
img = cv2.resize(img, (300,300), interpolation=cv2.INTER_AREA)
      # neyin boyutunu değiştirmek istediğini gösteriyorsun ardından istediğin boyutu yaz ve sonra
      # interpolasyon değerini ver varsayılan olarak veriliyor gelin bunun neden verildiğini anlayalım şimdi.

cv2.imshow("Örnek Tablom", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
en başta söylemek gerekirki interpolasyon'nun kelime anlamı:
bilinen değerlerden bilinmeyeni tahmin etme yöntemi'dir kendisi.
Resim Boyutlandırma ve Interpolasyon
Kodunuz, 10x10 piksel boyutunda ve her piksel için 3 renk kanalına (kırmızı, yeşil, mavi) sahip siyah 
bir resim oluşturuyor ve ardından resmi 100x100 piksele yeniden boyutlandırıyor.bir yeniden boyutlandırma
söz konusu aslında.


Interpolasyon Nedir?
Resim boyutlandırma işleminde, piksellerin sayısı artırılır veya azaltılır. 
işte bu değişiklik sırasında bir adaptasyonu sağlıyo aslında.


Interpolasyon Türleri:
Yakınsak (Nearest Neighbor): Her piksel için en yakın pikselin renk değeri kullanılır. Bu yöntem hızlıdır, 
ancak bulanık bir görüntü oluşturabilir.
Doğrusal (Bilinear): Her piksel için komşu 4 pikselin renk değerleri ortalaması kullanılır. 
Bu yöntem, Yakınsak yöntemden daha yumuşak bir görüntü oluşturur, ancak daha yavaştır.
Kübik (Cubic): Her piksel için komşu 16 pikselin renk değerleri karmaşık bir fonksiyon ile hesaplanır. 
Bu yöntem, en yumuşak görüntüyü oluşturur, ancak en yavaştır.
Neden Interpolasyon Kullanılır?

Resim boyutlandırma işleminde piksellerin kaybolmasını veya çoğalmasını engeller.
Görüntünün netliğini ve pürüzsüzlüğünü korumaya yardımcı olur.
Kodunuzda:

interpolation=cv2.INTER_AREA parametresi, Doğrusal interpolasyon yöntemini seçer. Bu yöntem, Yakınsak 
yöntemden daha yumuşak bir görüntü oluşturur, ancak daha yavaştır.

Interpolasyon Değerini Neden Belirtmeniz Gerekir?

OpenCV, varsayılan olarak Doğrusal interpolasyon yöntemini kullanır. Ancak, farklı bir yöntem kullanmak 
isterseniz, bunu interpolation parametresi ile belirtebilirsiniz.

Hangi Interpolasyon Yöntemini Seçmelisiniz?

Bu, resminizin boyutlandırma amacına ve istenen görüntü kalitesine bağlıdır.

Hız önemliyse: Yakınsak yöntem
Görüntü kalitesi önemliyse: Doğrusal veya Kübik yöntem
'''


'''
dtype=np.uint8 parametresi, her renk kanalı için veri türünü belirtiyor.

Neden np.uint8 Seçilir?

Veri Aralığı: np.uint8 veri türü, 0 ile 255 arasındaki değerleri saklayabilir. Bu aralık, bir pikselin 
renk değeri için idealdir.
Bellek Kullanımı: np.uint8 veri türü, diğer veri türlerine (örneğin float32) göre daha az bellek kullanır.
Hız: np.uint8 veri türü, diğer veri türlerine göre daha hızlı işlem görür.

Alternatif Veri Türleri:
np.float32: Daha geniş bir veri aralığı sağlar, ancak daha fazla bellek kullanır ve daha yavaş işlem görür.
np.uint16: Daha yüksek hassasiyet sağlar, ancak daha fazla bellek kullanır ve daha yavaş işlem görür.
Genellikle, np.uint8 veri türü, resimler ve videolar için en iyi seçimdir.

Her renk kanalı için veri tipi belirtmezseniz:
NumPy, tüm kanallar için varsayılan veri türünü kullanır. Bu veri türü, tüm renk kanalları için 
uygun olmayabilir.
Resim veya videonuzda renk bozulması veya hatalı görüntüleme meydana gelebilir.
'''







