import cv2 



# farklı türde olan eşikleme yöntemleri bunlar en sık kullanılan türleri bı bakmakta fayda olacağını düşündüm

img = cv2.imread("1Fahrettin_pasa.jpg",0)
'''
# Otsu eşikleme
ret,th1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
'''
'''
# Adaptif eşikleme
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
cv2.THRESH_BINARY,7,2)
'''

'''
Adaptif eşiklemeyi kullanabileceğiniz bazı durumlar:

Düşük aydınlatmalı görüntüler: Düşük aydınlatmalı görüntülerde, görüntünün bazı bölgeleri diğerlerinden 
daha karanlık olabilir. Adaptif eşikleme, her bölgeye uygun bir eşik değeri seçerek görüntünün daha net 
görünmesini sağlayabilir.
Yüksek aydınlatmalı görüntüler: Yüksek aydınlatmalı görüntülerde, görüntünün bazı bölgeleri patlamış olabilir. 
Adaptif eşikleme, bu bölgeleri daha koyu hale getirerek görüntünün daha dengeli görünmesini sağlayabilir.
Parlaklık değişimi olan görüntüler: Görüntünün farklı bölgelerinde parlaklık değişimi varsa, adaptif eşikleme 
bu bölgeleri ayrı ayrı işleyerek daha iyi sonuçlar elde edebilir.
Dokulu görüntüler: Dokulu görüntülerde, adaptif eşikleme dokuyu korumaya yardımcı olabilir.
Adaptif eşiklemenin faydaları:

Homojen olmayan aydınlatma koşullarında daha iyi sonuçlar verir.
Nesneleri arka plandan daha iyi ayırabilir.
Görüntüdeki gürültüyü azaltabilir.
Adaptif eşiklemenin dezavantajları:

Sabit eşiklemeye göre daha karmaşıktır.
Hesaplama açısından daha maliyetlidir.
Eşik değerinin seçimi, görüntünün özelliklerine ve istenen sonuca bağlıdır.
'''
'''
# Sabit eşikleme
th3 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)[1]
'''

'''
# Yarı tonlama
th4 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_TOZERO)[1]
'''

#cv2.imshow("Otsu Eşikleme", th1)
#cv2.imshow("Adaptif Eşikleme", th2)
#cv2.imshow("Sabit Eşikleme", th3)
#cv2.imshow("Yari Tonlama", th4)

cv2.waitKey(0)
cv2.destroyAllWindows()