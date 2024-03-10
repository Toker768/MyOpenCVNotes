import cv2
import numpy as np

'''
canvas2 = np.ones((512,512,3), dtype=np.uint8) * 255 

# ben bir çizim yaptım bunun kaç parametresi olabilir öncelikle ben bunu hangi tuvale hangi pencereye yapıcam
# ardından (başlangıç noktası) nere (bitiş noktası) nere (rengi) ne (kalınılığı) ne olsun.

cv2.line(canvas2, (50,50), (199,199), (255,0,0), thickness=2)
cv2.line(canvas2, (400,400), (199,199), (0,0,255), thickness=4)

# eğer ben bir diktörgen yapıcaksam bir sol üst ile sağ alt'ın kordinatlarını bilmem benim için yeterli temel
# olarak
cv2.rectangle(canvas2, (20,20), (100,100), (0,255,0), thickness=2)


# ben bir çember çiziceksem öncelikle onun bir merkesi ardından bir de yarıçapı vardır.
cv2.circle(canvas2, (300,300), 80, (0,0,255), thickness=5)


# open cv fonksiyonlarını kullanarak çizim yapmak bu kadar basit aslında her türlü çizimi ben rahatlıkla 
# yapabilirim zaten bunları ezberlemene gerek yok lazım olduğunda internetten bakacaksın.

# ben herhangi bir kapalı yamuk oluşturacaksam ne yapmam gerekecek.veya çokgen oluşturacaksam ne yapcam 
# o zaman ben polylines kullanmam gerek.

# son  olarak şunu söyleyebilirim ben sen çizmek istediğin şeklin özelliklerini bilmen benim için yeterli.


# ben openCV kullanarak yazı da yazdırabiliyorum.benim sadece bunu bilmem aslında yeterli.çünkü internette 
# zaten bunlar yazıyo.oradan bakarsın.



cv2.imshow("Canvas", canvas2)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''