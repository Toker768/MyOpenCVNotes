import cv2



img = cv2.imread("1ilkaskim.jpg",0)
resizeimg = cv2.resize(img, (680,460))

row, column = resizeimg.shape

M = cv2.getRotationMatrix2D((column/2,row/2),90,1)
'''
Bu kod, görüntüyü döndürmek için bir dönüşüm matrisi oluşturur. cv2.getRotationMatrix2D() fonksiyonu, 
görüntüyü döndürmek için kullanılan bir matris oluşturur. Bu fonksiyon üç parametre alır:

(column/2,row/2): Dönüş merkezinin koordinatları. Bu kodda, dönüş merkezi görüntünün merkezine ayarlanır.
90: Dönüş açısı. Bu kodda, görüntü 90 derece saat yönünde döndürülür.
1: Ölçeklendirme faktörü. Bu kodda, görüntü döndürülürken ölçeklendirilmez.aslında yakınlaştırmak ile aynı
şeydir.
'''

dst = cv2.warpAffine(resizeimg,M,(column,row))
# cv2.warpAffine() fonksiyonu, görüntünüzde yaptığınız değişiklikleri uygulama fonksiyonudur. 
# Bu fonksiyon, görüntüyü bir affine dönüşüm matrisi kullanarak dönüştürür. Affine dönüşüm matrisi, 
# görüntüyü kaydırmak, döndürmek, ölçeklendirmek ve eğmek için kullanılabilir.
'''
Bu kod, resizeimg görüntüsünü M matrisi kullanarak döndürür ve dst değişkenine atar. 
row ve column değişkenleri, yeniden boyutlandırılmış görüntünün boyutunu saklar.
'''

cv2.imshow("DST", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()