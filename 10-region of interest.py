# region of interest --> ilgi alanları
'''
olay şu ben bir fotoğrafdaki insanların duygu hallerine bakıcaksam benim ilgi alanım(region of interest)
yüzleri olur.

Mesela ben bir basketbol topunun boyunu hesaplamak istiyorum o halde benim region of interest'im basketbol 
topu olur.
'''

import cv2 


img = cv2.imread("1basketboll.jpg") # ben okumadan bir görsele işlem yapamam bunu aklından çıkarma lütfen 
# illa onu okuyup numpy dizisi haline sokmam gerek.

print(f"Shape:{img.shape}")        # shape = şekil

regionOfinterest =img[100:160, 200:350] 
# burada benim yakalamış olduğum yüzü böyle manuel bir şekilde yakalamıyoruz tabikide çeşitli derin öğrenme 
# ve makine öğrenmesi yöntemleriyle bu iş yapılır.


# img[200:300, 250:400] = regionOfinterest
# burada benim img'min seçmiş olduğum bir kısmı regionofinterest'e eşitlediğimi görebiliyorum.


cv2.imshow("Basketçiler", img)
cv2.imshow("Yüz",regionOfinterest)

cv2.waitKey(0)
cv2.destroyAllWindows()
