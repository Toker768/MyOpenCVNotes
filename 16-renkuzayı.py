import cv2

img = cv2.imread("1Fahrettin_pasa.jpg")

newRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
newHVS = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
newGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
newHLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)


cv2.imshow("Klon BGR", img)                       
#cv2.imshow("Klon RGB", newRGB)                   # ben görüntü üzerinde neye ihtiyacım var ise ona göre 
#cv2.imshow("Klon RGB", newHVS)                   # uygun renk uzayını ben seçerim.
#cv2.imshow("Klon RGB", newGray)
cv2.imshow("Klon HLS", newHLS)

cv2.waitKey(0)
cv2.destroyAllWindows()




# peki ben neden renk uzayları değiştirme ihtiyacı hissederim diye sorarsan bunun ana sebebi "uyumsuzluk"
# daha detaylı bir bilgi istersen aşağıya bak:
'''
OpenCV ve Matplotlib Uyumusuzluğu:
OpenCV kütüphanesi, BGR renk düzenini kullanır. Ancak, Matplotlib gibi bazı diğer kütüphaneler ve araçlar, 
RGB renk düzenini kullanır. Eğer OpenCV ile işlediğiniz bir görüntüyü Matplotlib ile göstermek istiyorsanız, 
renk düzenini uyumlu hale getirmek amacıyla BGR'den RGB'ye dönüştürme işlemi yapmanız gerekebilir.

Veri Setleri ve Modeller:
Bazı veri setleri veya önceden eğitilmiş modeller, farklı renk düzenlerini kullanabilir. Eğer bir veri 
seti veya model, BGR renk düzenini kullanıyorsa, ancak siz RGB düzenini tercih ediyorsanız, dönüşüm işlemi 
yapmanız gerekebilir.

Görüntü İşleme Algoritmaları:
Görüntü işleme algoritmaları veya belirli işlemler, BGR renk düzenini kullanarak tasarlanmış olabilir. 
Bu durumda, işlemleri gerçekleştirmek için uygun renk düzenine dönüştürme yapmanız gerekebilir.

Renk Modeli Tercihleri:
Bazı uygulamalarda veya alanlarda (örneğin, medikal görüntüleme), belirli renk düzenleri tercih edilebilir. 
Eğer tercih ettiğiniz renk düzeni farklıysa, dönüşüm işlemi yaparak istediğiniz renk düzenine uyum 
sağlayabilirsiniz.
'''


# meraktan baktım bunlarada;
'''
Farklı renk uzayları, çeşitli görüntü işleme görevlerinde ve uygulamalarda kullanılır. 
İşte bazı örnekler:

RGB ve BGR:
RGB ve BGR renk uzayları genellikle renkli görüntü temsilinde kullanılır. Kameralar tarafından sağlanan 
renkli görüntüler genellikle bu uzaylarda ifade edilir. Grafik tasarım, video oyunları ve genel renkli 
görüntü işleme uygulamalarında yaygındır.

GRAY:
Gri tonlama renk uzayı, renk bilgisine ihtiyaç duyulmadığı durumlarda ve işlemlerin hızlı bir şekilde 
gerçekleştirilmesi gerektiğinde kullanılır. Özellikle kenar tespiti, görüntü segmentasyonu ve bazı temel 
işlemler için uygundur.

HSV:
HSV renk uzayı, renk bilgisini daha doğru bir şekilde temsil ettiği için renk tabanlı işlemler ve 
analizler için idealdir. Renk filtreleme, renk tanıma ve renk tabanlı nesne izleme gibi uygulamalarda 
kullanılır.

YCrCb:
YCrCb, genellikle video sıkıştırma algoritmalarında ve renk kanalı bazlı işlemlerde kullanılır. 
Özellikle renk bilgisinin daha az önemli olduğu durumlarda sıkça kullanılır.

Lab:
Lab renk uzayı, renk hassasiyetine dayalı olarak tasarlanmıştır ve insan gözünün renk algısını daha iyi 
yansıtır. Renk düzeltme ve renk tabanlı analizlerde kullanılır.

XYZ:
XYZ renk uzayı, renk bilgisini matematiksel olarak ifade eder ve renk dönüşümlerinde kullanılır. 
Özellikle renk uzayı dönüşümleri ve renk uzayı tabanlı hesaplamalarda kullanılır.

Luv:
Luv renk uzayı, renk bilgisini insan gözünün renk algısına dayalı olarak temsil eder. Renk düzeltme 
ve renk tabanlı analizlerde kullanılır.

HLS veya HSL:
Hue-Lightness-Saturation renk uzayı, renk tonu, parlaklık ve doygunluğu içerir. Renk tabanlı işlemler, 
renk filtreleme ve renk analizi uygulamalarında kullanılır.
'''