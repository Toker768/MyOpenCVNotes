# şimdi burada ben kanal verilerini birbirinden ayırma işlemi yapacağım.
import cv2 


img = cv2.imread("1images_opencv.png")  # bakın tekrar söylüyorum ben her zaman bir resmi işlemeden önce
# onu okuyup numpy haline soktuktan sonra bir değişkenin içine kaydetmem daha mantıklı.
print(f"Shape:{img.shape}")              # height, weight, ımage channel(BGR)      


(B, G, R) = cv2.split(img)          # ben bu B G R ile birlikte bir resmim renk kanallarını bu şekilde 
                                    # ayırabiliyorum.Bu harfler sırası ile blue green red değerlerini 
                                    # temsil ediyor.


merged = cv2.merge([B, G, R])       # ayırmış olduğum resim kanallarını burada tekrar birleştirdim.



cv2.imshow("Library", img)
cv2.imshow("Library-B", B)            # burada ben blue rengini alıp split(bölme) işlemi yapıyorum.
cv2.imshow("Library-G", G)            # tabiki burada önemli olan sıra sıra yazmam benim.  
cv2.imshow("Library-R", R)
cv2.imshow("Library-merge", merged)              # merge = birleştirmek. bütün o ayırdığım renkleri birleştir-
# memi sağlıyo burada.


cv2.waitKey(0)
cv2.destroyAllWindows()