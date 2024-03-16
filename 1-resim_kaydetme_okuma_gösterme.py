import cv2
import matplotlib



img = cv2.imread("1cakma_asker.jpg")     # cv2.imread() fonksiyonu, "cakma_asker.jpg" adlı bir görüntü
                                        # dosyasını okur ve bu görüntüyü bir NumPy dizisine dönüştürür.
print(img)



'''
Neden Fotoğraflar matris formatındadır başka bir şey olamazmıydı ? 

Nedeni çok basit çünkü bilgisayarlar bu şekilde çok rahat işlem yapıyorlar.her türlü işlemlerini burada 
gerçekleştirebiliyorlar.
'''

# ben neden bir fotografı numpy gibi bir diziye dönüştürmek istiyorum diyosan bunun sebebi üzerinde 
# oynamalar çok kolay yaparımda o yüzden.
# bu numpy dizisinin içinde piksel değerleri vardır onunlar oynama yapılabilir.matplotlip ile ben matrisleri
# görselleştirebiliyorum.

# Derin öğrenme ve makine öğrenme uygulamalarında, görüntü verileri genellikle NumPy dizileri olarak kullanılır.
# Model eğitimi ve tahmin süreçlerinde NumPy dizileri üzerinde operasyonlar gerçekleştirilir.

# yani şunu şöyleyebiliriz burada bir jpg'nin numpy matrislerine dönüşmesi onunla geniş bir yelpazede işlem 
# yapabileceğimi gösterir.




'''
img = cv2.imread("1cakma_asker.jpg", cv2.IMREAD_COLOR)     
print(img) 
'''

'''
cv2.IMREAD_COLOR: Renkli görüntü olarak okuma (Varsayilan). eğer ben bir şey belirtmessem otomatik olarak 
bunu alacaktir.
cv2.IMREAD_GRAYSCALE: Siyah-beyaz (grayscale) olarak okuma.
cv2.IMREAD_UNCHANGED: Alfa kanali dahil, orijinal formatta okuma.

benim bunlari böyle farklı renkde belirtmemin bir sebebi var aslında o da şu:

eğer ben siyah-beyaz bir fotoğraf kullanacaksam "cv2.IMREAD_GRAYSCALE" yaparım daha az bellek'de yer kaplar 
benim de verimliliğim artmış olur.Çünkü ben eğer belirtmessem otomatik olarak renkli gibi müdale edicektir.
buda benim için bir problem olarak karşıma çıkacaktır.

Özel Görüntü İşleme Senaryoları:
Belirli görüntü işleme senaryolarında, özellikle belirli renk kanalları üzerinde çalışmak istiyorsanız,
farklı renk modlarını belirtmek daha spesifik işlemlere olanak tanır. Örneğin, sadece mavi kanalı üzerinde
işlem yapmak.Özetle, ikinci parametreyi belirlemenin faydası, görüntüyü farklı renk modlarında veya 
formatta okuma esnekliği sağlamaktır. Ancak, çoğu durumda bu parametre belirtilmez ve varsayılan renk modu 
(renkli) kullanılır.
'''



'''
img = cv2.imread("1cakma_asker.jpg", cv2.IMREAD_COLOR)    # benim burada "cv2.IMREAD_COLOR" yazmamın bir 
# nedeni yok aslında zaten varsayılan ayar olarak böyle anlayacaktı.ama ben siyah beyaz bir görüntü kullan
# mış olsaydım bu sefer belirtmem gerekirdi. "cv2.IMREAD_GRAYSCALE" diye bellek'de tasarruf etmek için.


cv2.namedWindow("Myimage",cv2.WINDOW_NORMAL)        # benim resmim eğer boyutunu artırmada veya azaltmada bir
# problem var ise bunu yaparım.Zaten isminden tanıyor boyutunu ayarlayacağım görüntünün.

cv2.imshow("Myimage", img)      # bu görüntüyü göstermek için kullanıldı.
cv2.waitKey(0)                  # buda benim bir tuşa basılana kadar beklememi sağlıyor burada.
# ben içeriye milisaniye cinsinden değer yada bir tuşa basıldığında kapatmasını sağlayan yazılım yazabilirim.


key = cv2.waitKey(0)
if key == ord('q'):  # Eğer 'q' tuşuna basılırsa
    cv2.destroyAllWindows()



cv2.destroyAllWindows()         # Ancak, bir programda birden fazla pencere açılmışsa ve bu pencerelerin 
                                # düzgün bir şekilde kapatılmasını sağlamak istiyorsanız, cv2.destroyAllWindows()
                                # kullanmanız iyi bir uygulama olabilir.
'''








 
