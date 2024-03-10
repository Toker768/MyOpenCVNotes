# Öncelikle ben 2 resimi toplamasını yapabilmem için bunların aynı boyda olması lazım.çünkü resimlerde aslında 
# birer matrislerdir.ve matrisler toplanabilmesi için aynı boyda olması gerekir.

# ben görüntü işleme yaparken neden 2 resimi toplamaya ihtiyaç duyarım ? 

'''
Renkli Görüntü Üzerinde Efektler Oluşturma:
Farklı efektler elde etmek için iki renkli görüntüyü toplayabilirsiniz. Örneğin, bir görüntüyü diğerine 
ekleyerek renk tonlarını değiştirebilir veya parlaklık ve kontrast gibi özellikleri ayarlayabilirsiniz.

Görüntü Birleştirme veya Üzerine Koyma:
İki görüntüyü birleştirerek veya üzerine koyarak, farklı katmanları birleştirebilirsiniz. 
Örneğin, iki manzara görüntüsünü birleştirerek geniş bir manzara görüntüsü elde edebilirsiniz.

İki Görüntü Arasındaki Farkı Bulma:
İki görüntü arasındaki farkı bulmak için, piksel değerlerini çıkarabilir veya mutlak değerini alabilirsiniz. 
Bu, örneğin iki kamera görüntüsü arasındaki değişiklikleri belirlemek veya bir referans görüntü ile mevcut 
görüntü arasındaki farkları ortaya çıkarmak için kullanılabilir.

Gürültü Azaltma:
İki benzer görüntüyü toplayarak, gürültüyü azaltabilirsiniz. Benzer piksel değerlerine sahip iki 
görüntüyü toplamak, ortak özellikleri güçlendirecek ve gürültüyü azaltacaktır.

İki Görüntüdeki Nesneleri Birleştirme:
İki farklı pozisyondan alınan görüntülerdeki nesneleri birleştirerek geniş bir perspektif elde 
edebilirsiniz. Bu, genellikle 3D modelleme ve haritalama uygulamalarında kullanılır.
'''

import cv2
import numpy as np 


'''
canvasCircle = np.zeros((512,512,3), np.uint8) + 255              # beyaz renkde bir tuval oluşturdum.
cv2.circle(canvasCircle, (256,256), 60, (255,0,0), thickness=-1)   # 'thickness=kalınlık' ben -1 yağtığımda 
# içersi dolu olan bir daire çizmiş olucam.

canvasRectangle = np.zeros((512,512,3), np.uint8) + 255 
cv2.rectangle(canvasRectangle, (150,150),(350,350), (0,255,0), -1)


add = cv2.add(canvasRectangle,canvasCircle)


cv2.imshow("Circle",canvasCircle)
cv2.imshow("Rectagnle",canvasRectangle)
cv2.imshow("Mix", add)
'''

canvasCircle = np.zeros((512,512,3), np.uint8) + 255             
cv2.circle(canvasCircle, (256,256), 60, (255,0,0), thickness=-1)

canvasRectangle = np.zeros((512,512,3), np.uint8) + 255 
cv2.rectangle(canvasRectangle, (150,150),(350,350), (0,255,0), -1)

dst = cv2.addWeighted(canvasCircle, 0.7, canvasRectangle, 0.3, 0)



cv2.imshow("Circle",canvasCircle)
cv2.imshow("Rectagnle",canvasRectangle)
cv2.imshow("Mix",dst)




cv2.waitKey(0)
cv2.destroyAllWindows()
