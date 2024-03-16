import cv2

# ben ilk önce bir video'yu kaydetmeden önce onu iyi bir şekilde almam karelerine bölmem ardından'da bölünen 
# karelerini okumam gerekir ondan sonra kayıt gelir zaten.

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)    # frame(kare)'lere ayırıp cap'in içine soktum burada
'''
Aslında benim video'mu daha kaliteli hale getiriyor diyebilirim.
Windows işletim sisteminde çalışıyorsanız ve temel video yakalama ve oynatma işlevlerine ihtiyacınız varsa, 
DirectShow iyi bir seçimdir.Linux işletim sisteminde çalışıyorsanız, V4L2 iyi bir seçimdir.
Daha fazla özellik veya daha iyi performans ihtiyacınız varsa, GStreamer veya FFmpeg'i kullanmayı düşünebilirsiniz.
'''

#------------------------------------------------------------------------------------------------------------------
filename = "D:\Anacondaam\envs\enimdosyam-5\BenimVideom.avi"   
codec = cv2.VideoWriter_fourcc('W','M','V','2')
framerate = 30
resolution = (640,480)
videoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)

                 # bunun içine dört tane parametre girersin burada;
# --> konumuyla birlikte dosya adı,codev değeri(hoca açıklamadı bunu), frame rate(oran), resolution value(çözünür
# lük değeri) 
# ayrıca buraya kadar yazılan kodları şöyle düşünebilirsin bir paket ayarladım ben aslında bu paketi
# kaydetmek için ben kullanıcam. 

'''
OpenCV'de video kaydederken bakabileceğin 4 temel parametre var:

1. Dosyanın Konumu ve Adı: Kaydedeceğin videonun nereye kaydedileceğini ve ne adla kaydedileceğini belirler.


2. Codec: Videonun nasıl sıkıştırılacağını ve kodlanacağını belirler. Farklı codec'ler farklı sıkıştırma
oranları ve görüntü kalitesi sunar.
Videonu nasıl sıkıştırmak istediğini hayal et. Sıkıştırmak, videoyu daha küçük hale getirir, böylece daha 
az yer kaplar ve daha kolay paylaşabilirsin. Farklı sıkıştırma türleri farklı görüntü kalitesi sunar.
Peki benim aklıma şöyle bir soru geldi en iyi codec türü gibi bir şey var mı ?
burada bizim ne yapmak istediğimizi bilmek oldukça önemli.en yaygın olanlar ise şöyle:
H.264/AVC, H.265/HEVC, VP9, AV1 bunlar yaygın olarak kullanılmakda özelikkle H.264/AVC 


3. Framerate: Videodaki saniyedeki kare sayısını (FPS) belirler. Daha yüksek bir framerate, daha akıcı
bir video anlamına gelir. .waitkey() ile neredeyse birbirinin zıttı olduğunu söyleyebilirim.


4. Çözünürlük: Videonun genişliğini ve yüksekliğini piksel cinsinden belirler. Daha yüksek bir çözünürlük,
daha ayrıntılı bir video anlamına gelir.
'''          
#Framerate ve çözünürlük, bir videonun iki önemli özelliğidir.
#Framerate: Videodaki saniyedeki kare sayısını (FPS) belirler. Daha yüksek bir framerate, daha "akıcı" bir video
#anlamına gelir.

#Çözünürlük: Videonun genişliğini ve yüksekliğini piksel cinsinden belirler. Daha yüksek bir çözünürlük, 
#daha "ayrıntılı" bir video anlamına gelir.
'''
İkisi arasındaki fark:

Framerate, videonun "zamansal" kalitesini etkiler. Daha yüksek bir framerate, videonun daha akıcı ve pürüzsüz 
görünmesini sağlar. Özellikle hızlı hareket içeren videolarda framerate önemlidir.
Çözünürlük, videonun "mekansal" kalitesini etkiler. Daha yüksek bir çözünürlük, videonun daha keskin ve ayrıntılı 
görünmesini sağlar. Özellikle büyük ekranlarda izlenecek videolarda çözünürlük önemlidir.
Örnek:

30 FPS'de 1080p bir video, 60 FPS'de 1080p bir videodan daha az akıcı olacaktır.
60 FPS'de 720p bir video, 30 FPS'de 1080p bir videodan daha az ayrıntılı olacaktır.
Hangi parametreyi daha çok önemsemeniz gerektiği, videonuzu nasıl kullanacağınıza bağlıdır.

Eğer videonuzu internette paylaşacaksanız, daha düşük bir framerate ve çözünürlük kullanmak isteyebilirsiniz. 
Bu, dosya boyutunu küçültecek ve videonuzun daha hızlı yüklenmesini sağlayacaktır.
Eğer videonuzu büyük bir ekranda izleyecekseniz, daha yüksek bir framerate ve çözünürlük kullanmak isteyebilirsiniz.
Bu, videonuzun daha akıcı ve ayrıntılı görünmesini sağlayacaktır.
Genel olarak, "30 FPS ve 1080p çözünürlük" çoğu video için iyi bir dengedir. Daha yüksek bir framerate veya 
çözünürlük, videonuzun daha iyi görünmesini sağlayabilir, ancak dosya boyutunu da artıracaktır.
'''

#-------------------------------------------------------------------------------------------------------------------
while True:
    reply, result = cap.read() # almış olduğum bu kareleri ben teker teker bir döngünü içinde numpy dizileri 
    # çıkartıyorum.

    # okuyamama durumunu düşünerekten;
    if reply==False:
        break
    
    # insan beyninin algılayabilmesi için ben bunu bi döndüriyim.1 yazdığım için y eksenine göre döndürecek.
    result = cv2.flip(result, 1)

#-------------------------------------------------------------------------------------------------------------


    # dödürmüş olduğum frameleri bir dosyanın içine kaydedicem. bir dosya dediğim şey burada nerede bulunacağımdan
    # nasıl kalitede olacağından özelliklerin bizzat benim belirlediğim yer.
    videoFileOutput.write(result)



#-------------------------------------------------------------------------------------------------------------

    cv2.imshow("Webcam", result)       # bir döngü içinde olduğu için ismi result olan frame'leri burada.
                                       # gösterilecek.
    
    if cv2.waitKey(50) & 0xFF == ord("q"):  # gösterilecekde nasıl hangi kalitede gösterilecek buda önemli.
        break

# eee tabi benim her video işinin sonunda release yapmaya mecburum yoksa almış olduğum video kodu kapatsam bile 
# durmaz.
    
videoFileOutput.release()
cap.release()                         # neredeyse her içinde video olan projeme ben bunu yazarım.
cv2.destroyAllWindows()               # nerdeyse her projemin altına ben bunu yazarım.

















