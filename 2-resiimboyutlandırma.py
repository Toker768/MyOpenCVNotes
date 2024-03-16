import cv2

# cv2.namedWindow("Myimage", cv2.WINDOW_NORMAL)  # ben burada imshow ile göstermiş olduğum görüntümün
# dışına bir pencere koydum.peki benim penceremi nereden tanıdın diye sorarsanız isimlerini aynı yapıyorum dikkat et.
# ben bu ikinci parametreye ya cv2.WINDOW_NORMAL yada cv2.WINDOW_AUTOSIZE yazabilirim.başka yazacağım bir şey yok.
# aotusıze yapınca benim pencerem görüntümün boyutunda oluyor.

'''
Peki ben neden bir görüntümün pencereye sahip olamasini isterim ?


Geliştirme ve Hata Ayıklama: Görüntü işleme uygulamalarını geliştirirken, her adımda görüntüyü gözlemlemek 
ve algoritmanın doğru çalışıp çalışmadığını kontrol etmek önemlidir.
Pencere ekleyerek, her aşamada görüntüyü görsel olarak izleyebilir ve geliştirdiğiniz algoritmanın beklediğiniz sonuçları
üretip üretmediğini kontrol edebilirsiniz.

İnteraktif Kullanım: Pencere eklemek, kullanıcının bir uygulama ile etkileşimde bulunmasına olanak tanır. 
Örneğin, görüntü üzerinde bir nesneyi seçmek, konumlandırmak veya bir işlemi başlatmak gibi interaktif özellikler 
ekleyebilirsiniz.

Parametre Ayarı: Pencere ekleyerek, bir algoritmanın veya işlemin parametrelerini gerçek zamanlı olarak ayarlamak 
ve sonuçları gözlemlemek mümkün olabilir. Bu, algoritmanın performansını optimize etmek için kullanışlıdır.

Ön İnceleme ve Sunum: Görüntüyü bir pencerede göstermek, son kullanıcıya veya başka bir geliştiriciye sonuçları 
ön izleme ve sunma imkanı sağlar. Bu, projenizi paylaşmak, tartışmak veya belirli bir aşamada sonuçları 
değerlendirmek için kullanışlıdır.
'''

# cv2.namedWindow("Myimage")

img = cv2.imread("1cakma_asker.jpg")            # ben bir resmi önce numpy dizilerini dönüştürmem gerek.numpy'a
# dönüştürdükten sonra işlemler yapabilirim anca.

img = cv2.resize(img, (400,400), interpolation=cv2.INTER_LINEAR)

cv2.imshow("Myimage", img)               # görüntümün başılğını ve hangi görüntümü göstereceğimi belli ettim.
cv2.waitKey(0)
cv2.destroyAllWindows()


