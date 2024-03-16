# video bir çok karenin bir araya gelmesi ile oluşur.Tıpkı fotoğrafların birçok pikselin bir araya gelmesi ile
# oluştuğu gibi.

import cv2


# ben ister foto olsun ister video farketmez ben onu en başta bi okuyup değişken içine almam gerekli.benim
# fotoraflardaki imread() fonsiyonum videoda ise şu:

cap = cv2.VideoCapture(0)
# bildiğin videonun içindeki kareleri(frame) leri alıyor ve teker teker içine kaydediyor.oldumu sana video bu 
# satten sonra kare kare fotoğraflar.

'''
eğer ben videoyu webcam'den yani kameradan okuyacaksam bunun içine sifir 
değerini girmem gerekir. eğer yok kamera değilde bilgisayardaki bir videoda iş yapacaksam o videnun adresini
girmeliyim.
peki lan bu sıfır nerden geldi dediğinizi duyar gibiyim onun da açıklaması şöyle;

0: Varsayılan kamerayı kullanır. Bu genellikle dahili webcamdır.
1: Harici bir web kamerası veya ikinci bir dahili kamera gibi ikinci kamerayı kullanır.
2: Üçüncü kamerayı kullanır.
'''


while True:                     # ben karaleri tek tek yakalayıp cap değişkenine hapsettikten sonra onları işliyorum.
    reply, result = cap.read()  # ne yazıkki öyle tek fonksiyonla olmuyor şu aşamada.ben o kareleri(frame)
                                # tek tek okumam gerekli.
    # burada ayrıca cap.read() iki tane cevap döndürür bunlardan ilki True,False yani okuyup okuyamadığı
    # ikincisi ise : okunan karenin Numpy dizisidir. Bu dizi, görüntünün piksellerini ve diğer bilgilerini 
    # içerir.

    if not reply:           # reply'in False olması demek aslında şu anlama geliyor ben eğer dışardan bir 
        break               # video açmışşam onun bitmesi anlamına geliyor.eğer ki webcam'den sen video açmışsan
    # zaten buna gerek kalmaz.

    result = cv2.flip(result, 1)  # flip = çevir burada ben yazmış olduğum 1'den dolayı y eksenine göre  
    # çeviriyorum webcamden aldığım görüntüyü.
#     1: Görüntüyü yatay olarak çevirir.
#     0: Görüntüyü dikey olarak çevirir.
#    -1: Görüntüyü hem yatay hem de dikey olarak çevirir.      

    cv2.imshow("Webcam", result)           # burada her kareyi bana gösterecek bir döngünü içinde.bide ben bunları
    # göriyim bağlım.

    if cv2.waitKey(20) & 0xFF == ord("q"):    # ben burada hem waitkey'i hemde 'q' ye bastığımda çıkan bir 
        break                                 # kod yazdım.
    
    
    # bu daha basit hali 
    # cv2.waitKey(30)              # her bir kareyi 30 milisaniye beklet demek bu.eğer ben kameradan bunu gösteri-
    # yorsam ben 10 yapsam yani her 10 milisaniyede bir görüntü al desem. benim bilgisayarım zorlanabilir
    # çünkü ben daha fazla çalıştırmış olacağım.



cap.release()            # release = serbest bırakmak,tahliye etmek



'''
sana Opencv'de cap.release() fonksiyonunun ne işe yaradığını mantığını ve bir çocuğa anlatır gibi anlatacağım.

Hayal et ki bir video oyunu oynuyorsun. Oyunda bir karakteri kontrol ediyorsun ve bu karakter bir sürü farklı
 şey yapabiliyor. Örneğin, koşabilir, zıplayabilir ve ateş edebilir.

Peki, karakterin bir şey yapmayı bitirdiğinde ne yaparsın? Örneğin, karakterin koşmayı bitirdiğinde,
 koşma komutunu durdurursun. Aynı şekilde, karakterin ateş etmeyi bitirdiğinde, ateş etme komutunu da durdurursun.

Cap.release() fonksiyonu da buna benzer bir şey yapar. Bu fonksiyon, video yakalama cihazını
 (web kamerası veya video dosyası) kontrol etmeyi bırakır.

Haydi bunu bir örnekle açıklayalım. Diyelim ki web kameranızla video kaydediyorsunuz. Kayıt işlemi bittiğinde, 
web kamerasını kullanmayı bırakmak istersiniz. Bunu yapmak için cap.release() fonksiyonunu çağırırsınız.

Cap.release() fonksiyonunu çağırmadığınızda ne olur? Web kamerası hala açık kalır ve bilgisayarınızın 
kaynaklarını (işlemci gücü ve bellek) kullanmaya devam eder. Bu da bilgisayarınızın yavaşlamasına neden 
olabilir.

Cap.release() fonksiyonunu HER ZAMAN kullanmayı UNUTMAYIN. Bu fonksiyon, bilgisayarınızın kaynaklarını 
korumanıza ve bilgisayarınızın daha hızlı çalışmasını sağlamanıza yardımcı olur.fotoğraflarda'da bu 'del' dir 
ben  en son atıyorum fotografımı okuttum ve numpy dizime dönüştürdüm işim bittikten sonra 'del' yaparak işlemi
sonlandırmam çok daha iyi olacaktır.
'''
# cv2.destroyAllWindows()     # buda benim opencv ile açtığım tüm dosyalarımı kapatmamı sağlar.




'''

cap = cv2.VideoCapture(0)        # ben ilk başta video mu karelere bölücem.

# sonra bölmüş olduğum bu kareleri ben teker teker işleme sokmam gerek.bunu'da while döngüsü ile yapıyorum.
while True:                     
    reply, result = cap.read()  

    if not reply:           
        break               

    result = cv2.flip(result, 1)           

    cv2.imshow("Webcam", result)           

    if cv2.waitKey(30) & 0xFF == ord("q"):     
        break   


cap.release()                      # ben eğer bir video açmıssam zaten bunun ikisini kullanmak zorundayım.       
cv2.destroyAllWindows()   
  '''

















