'''
Kontur Nedir?(What is the contour?)
Bir nesnenin kenar çizgisini hayal et. Kontur, bir nesnenin sınırlarını tanımlayan 'bir dizi noktadır'. 
Basitçe, bir nesnenin şeklini oluşturan noktalar zinciridir.

OpenCV'de nesneleri tanımak ve analiz etmek için kontur kullanilır.Bunu yapmak için, görüntüdeki 
piksellerin parlaklık ve renk değerlerindeki değişiklikleri analiz eder.

Bizim için oldukça önemli bi yapı bu aslında çünkü nesneleri tanımak ve algılamak için oldukça fazla
kullanılır.Aynı zamanda nesnelerin seklini ve boyutunu da bu şekilde kullanabilirsin.

Diyelim ki bir elma resminiz var. OpenCV, elmanın kenarlarını belirleyen bir dizi nokta bulacaktır. 
Bu noktalar, elmanın konturunu oluşturur.

OpenCV bir görüntüde nesneleri bulmak için konturları kullanır.
'''

# ben ayrıca contur bulurken binary yani siyah beyaz fotoğraflar kullanmalıyım.

# ben contour kullanarak bir tane üçgen fotoğrafının ;
# alanını,çevresini,geometri merkezini, çevreleyici geometrilerini bulabilirim.

'''
convex hull(diş bükey örtü) kavramı nedir ? 
Convex hull, bir dizi noktanın en dışbükey şeklini temsil eder. Bunu hayal etmek için bir kağıda bir dizi 
nokta çizin ve bir lastik bantla hepsini sarın. Lastik bandın sardığı alan, o noktaların convex hull'udur.

Bu görüntü işlemede çok fazla kullanilir.Convex hull'u hesaplamak için:
Graham Scan: En popüler algoritmalardan biridir.
Jarvis March: Basit bir algoritmadır, ancak Graham Scan'den daha yavaştır.


Evet, convex hull (dışbükey gövde), içbükey olan şekillere dişbükey bir örtü oluşturmak için kullanılan 
bir algoritmadır. Bu algoritma, bir şeklin tüm köşelerini birbirine bağlayan en küçük dışbükey şekli oluşturur.

Bilgisayar görüde nesneleri algılamak için oldukça fazla kullanılır.
'''


import cv2

img = cv2.imread("1images_opencv.png")     # I have to read it first if I want to take action.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     # Here I converted(dönüştürdü) my picture to black 
                                                 # and white format.because It makes my job easier.

_,thresh = cv2.threshold(gray,190,255,cv2.THRESH_BINARY)
'''
_ sembolü ile temsil edilen ilk çıktı değeri her zaman önemsiz değildir. Bazı durumlarda, işlemin başarısını 
veya başarısızlığını gösteren bir hata kodu veya geri dönüş değeri içerebilir.
Ancak, cv2.threshold fonksiyonu özelinde, ilk çıktı değeri her zaman 0'dır ve işlem her zaman başarıyla 
tamamlanır. Bu nedenle, bu özel durumda bu değer önemsizdir ve genellikle yok sayılır.
'''
 
contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours,-1,(0,0,255),3)

cv2.imshow("Contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


