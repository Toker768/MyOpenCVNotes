# gelin bugün beraber piksellere yakından bakalım

import cv2 

path = "1turgut_ozal.jpg"    # aynı yerde olduğu için konumu böyle belirtmem yeterli olucaktır benim için
img = cv2.imread(path)
# print(img)


# benim normalde bildiğim kordinat sistemleri ortadan başlar ama resimlerde böyle değil.sol üsten başlıyor.
# sağa doğru gidildikçe x değerim artarken aşağı yöne gittiğim zaman y değerim artmakda.böyle bir farkı var.
'''
ben atıyorum 10'a 10 değerini bulurken bana vermiş olduğu değerin anlami o noktadaki renklerin karişimi.
'''

'''
px = img[10,10]
print(px)        # [78 78 78] değeri bu pikselin BGR değerlerini temsil ediyor.çünkü open cv bu şekilde çalışır.  
# The reason I use square brackets(köşeli parantez) is because of the Numpy array.
# numpy array uses like this
'''
'''
# let's we learn what is the size
print(img.shape)   # will give row,column,channel colors
'''




'''
img = cv2.imread("1turgut_ozal.jpg")                        # burada toplam piksel sayısını ben hesaplayabiliyorum
                                                        
# Piksel sayısını hesapla                                
piksel_sayisi = img.shape[0] * img.shape[1]
# shape fonksiyonun 3 tane parametresi vardır.Yükseklik, genişlik, renk kanalları.

# Piksel sayısını yazdır                                  # demekki her bir yükseklik veya genişlik bir piksel
print(piksel_sayisi)                                      # olarak sayilmakda.
'''

'''
img = cv2.imread("1turgut_ozal.jpg")
print(img[100,100])  # [119 124 127] bu çıktının anlamı ise şöyle: 
# 119: Mavi (B) bileşeni
# 124: Yeşil (G) bileşeni
# 127: Kırmızı (R) bileşeni

# their average give me Brightness(parlaklık) of pixel

# give me saturation(doygunluk):  If the difference between color components(bileşenler) is low, the saturation of the 
# pixel is also low.If saturation is high, colors appear vibrant(canlı) and bright(parlak); 
# if saturation is low,colors appear pale(soluk) and dull(mat).

# and fınally gives pixel tone(colors). 
 

# ben şöyle yaparsamda 100'e 100 noktasında olan bunun 0.indexde olanı yani Blue(mavi) yi bana gösterecektir.
blue =(img[100,100,0])
print(blue)                               # böyle erişmek istemesseniz .item() fonksiyonunu kullanabilirsin.
 
green = (img[100,100,1])
print(green)

red =(img[100,100,2])
print(red)


# ben peki piksel değerlerini değiştirebilirmiyim.tabikii
img[100,100] = [10,20,30]          # gayet basit bir mantığı var burada.
print(img[100,100])

# böyle yapmak yerine bir tane fonksiyon var onu kullanmak daha mantıklı:
img.itemset((10,10,2), 199)             # ben burada 10,10 noktasında olan pikselin kırmızı rengini(BGK'den dolayı)
# 199 olarak değiştirdim burada.
# peki neden openCV bir pikselin içinde bulunan rengini "BGR" şeklinde yapmış acaba?
'''



'''
OpenCV'nin bir pikselin rengini BGR şeklinde yapmasının birkaç sebebi var:

Tarihi:
OpenCV, Sovyetler Birliği'nde geliştirildi ve o dönemdeki bilgisayarlar BGR renk uzayını kullanıyordu.

Verimlilik:
BGR, bazı işlemciler üzerinde RGB'den daha verimli olabilir.

Uyumluluk:
OpenCV, BGR'yi kullanan birçok üçüncü taraf kütüphanesiyle uyumludur.
Bununla birlikte, RGB renk uzayı daha yaygın olarak kullanılır.
'''





































