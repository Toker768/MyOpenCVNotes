# ı will find edge and corner of the image in the here
import cv2
import numpy as np

textimg = cv2.imread("1contour.png")

gray = cv2.cvtColor(textimg,cv2.COLOR_BGR2GRAY)
'''
öncelikle ben bir görüntünün köşelerini bulurken onu siyah beyaz formatına sokarım bunun temel nedenleri vardır:
renkli bir görüntüde 3 kanal vardır buda köşe dedöktörünün işini zorlaştırır.bende dedöktörlerinin işini
kolaylaştırmak adına bu kanalları teke indiriyorum.

Renkli görüntülerde, aydınlatma köşelerin görünümünü etkileyebilir. Örneğin, parlak bir alandaki bir köşe, 
karanlık bir alandaki bir köşeden daha belirgin olabilir. Siyah beyaz bir görüntüde ise aydınlatma tüm 
pikseller için eşittir. Bu da köşeleri daha net ve daha tutarlı hale getirir.

Aslında temel prensib burada benim işimi kolaylaştırmaktır başka bir şey değildir.
'''

gray = np.float32(gray)   
'''
Benim bu işlemi yapmamında temel 2 nedeni vardır:
1. Hassasiyet:
Float32 veri tipi, gri tonlama değerlerini daha hassas bir şekilde temsil edebilir. Bu da köşe 
dedektörlerinin daha doğru çalışmasını sağlar.

2. Hesaplama Verimliliği:
Float32 veri tipi, bazı matematiksel işlemler için daha verimlidir. Bu da köşe dedektörlerinin 
daha hızlı çalışmasını sağlayabilir.
'''
corners = cv2.goodFeaturesToTrack(gray, 3, 0.01, 10)
# bu fonksiyonun 4 parametresi vardır: -->  img, maxkaçköşebulsun, kalite, köşelerarasıminumummesafe
# ve sadece köşe bulmak için kullanılır.çalışma prensibinin temel mantığı ise şu şekilde olur 
# bir tane köşe dedöktörü görüntüdeki parlaklık değişimlerini analiz eder ve buradan köşeleri bulduğunu 
# söyleyebilirim.
# Fonksiyon, bulunan köşelerin koordinatlarını içeren bir dizi döndürür.
'''Ayrıca gray adında görüntümün içinde bulduğun her köşeyi 'corners' değişkenime atadım.'''
corners = np.int0(corners)
# corners değişkenini np.int0'a dönüştürmek, cv2.circle fonksiyonunun parametresi olarak 
# kullanılabilmesini sağlar.

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(textimg,(x,y),3,(0,0,255),-1)
    # textimg: Dairenin çizileceği görüntü.
    # (x,y): Dairenin merkezi.
    # 3 piksel : Dairenin yarıçapı.
    # (0,0,255): Dairenin rengi (kırmızı).
    # -1: Dairenin doluluk kalınlığı (-1, daireyi doldurur).
cv2.imshow("Corner", textimg)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
    buradaki .ravel() fonksiyonunu anlamak çok önemli bir nokta eğer onu anlamassak kafamızda tam manasıyla
   oturmayacaktır.
   ravel() fonksiyonu, bir dizideki tüm elemanları tek boyutlu bir diziye dönüştürmek için 
   kullanılır. Bunu, bir diziyi "düzleştirmek" olarak düşünebilirsiniz.

   Bunu yaparken elemanları satır satır eklemek yerine sutun sutun ekler.ve orijinal diziyi değiştirmez
   yeni bir dizi oluşturur.
   
   '''

