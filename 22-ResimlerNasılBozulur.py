import cv2
import numpy as np 

'''
img = cv2.imread("1ilkaskim.jpg")
newimg = cv2.resize(img, (680,450))

kernel = np.ones((3,3), np.uint8)
erosion = cv2.erode(newimg,kernel,iterations=1) # burada iterations erozyonun kaç defa gerçekleşmesini
# istiyorsan onu yazıyorsun.

cv2.imshow("Orijinal",newimg)
cv2.imshow("erosionPhoto", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# bizim burada anlamadığımız 1 nokta var bir kernel olayı ? bunu çok basit bir dille size anlatacağım
'''
Diyelim ki bir resim üzerinde çalışıyorsun ve bazı değişiklikler yapmak istiyorsun.
Kernel, bir fırça gibi bir araç. Fırçayla resmin belirli bölgelerini boyayabilir, yumuşatabilir 
veya keskinleştirebilirsin.

Kernel'in boyutu, fırçanın büyüklüğüne benzetilebilir. Küçük bir fırça, resimdeki küçük detayları 
değiştirmek için idealdir. Büyük bir fırça ise daha geniş alanları kaplamak ve daha genel değişiklikler 
yapmak için kullanılır.

Kernel'in elemanları, fırçadaki kılların rengine benzetilebilir. Fırçadaki kıllar farklı renklerde olabilir 
ve bu da resme farklı tonlar eklemenizi sağlar.

Kernel'i kullanarak:
Resmi yumuşatabilirsin. Bunu, tüm elemanları 1 olan bir kernel kullanarak yapabilirsin. Bu, fırçayla 
resimdeki tüm renkleri karıştırmaya benzer.
Resmi keskinleştirebilirsin. Bunu, bazı elemanları diğerlerinden daha büyük olan bir kernel kullanarak 
yapabilirsin. Bu, fırçayla resimdeki bazı kenarları belirginleştirmeye benzer.
Kenarları algılayabilirsin. Bunu, kenarları vurgulayan bir kernel kullanarak yapabilirsin. Bu, fırçayla 
resimdeki çizgileri ve kontrastları belirginleştirmeye benzer.
Gürültüyü azaltabilirsin. Bunu, ortalama filtreleme gibi bir kernel kullanarak yapabilirsin. Bu, fırçayla 
resimdeki küçük kusurları ve lekeleri düzeltmeye benzer.
Kernel'i kullanmak, resim üzerinde birçok farklı değişiklik yapmanı sağlar. Farklı kernel boyutlarını ve 
elemanlarını deneyerek resimlerini istediğin gibi değiştirebilirsin.
'''

# ----------------------------------------------------------------------------------------------------------

'''
# bu dilate aynı şekilde fotoğrafı erezyona uğratıyor ama normalde erozyona uğrayan fotoğraf siyahlar fakat 
# bu beyazlamaya başlıyor.
img = cv2.imread("1ilkaskim.jpg")
newimg = cv2.resize(img, (680,450))

kernel = np.ones((4,4), np.uint8)
mydilate = cv2.dilate(newimg,kernel,iterations=1) 

cv2.imshow("Orijinal",newimg)
cv2.imshow("DilatePhoto", mydilate)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
# ----------------------------------------------------------------------------------------------------------


# https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
# bu sitede hocanın göstermiş olduğu görüntü oynama işlemleri mevcut aslında.

