import cv2

img = cv2.imread("1Fahrettin_pasa.jpg")    # benim burada bir değişkene yazma zorunluluğum yok.

cv2.imshow("Üstadım", img)  # ama ben bunu çalıştıracaksam eğer önceden okumuş olduğum bir fotoğrafı ben bir
# değişkene bağlamak zorundayım.çünkü benim gösterme fonksiyonum fotografın okunmuş halini istiyor.


'''
Temelde bir görüntü 3 farklı değere sahiptir.Yüksekliği, genişliği ve resmin kanal veri değeridir.önemli 
bir nokta olduğunu düşünüyorum.
'''
# print(img.shape)        # (859, 750, 3)  The first parameter refers(ifade eder) to the height. 
# If the 2nd width, is the 3rd the channel data value If you noticed, the logic(mantık) of rows and columns prevails(hakim)here.



# bu kanal veri değeri dediğimiz nedir ?
'''
bu verinin renkli mi yoksa siyah beyaz mı olduğunu söylüyor.
eğer ki 3 ise --> renkli 
1 ise --> siyah beyaz olduğu anlamına geliyor.
4 ise --> Bu durumda, kırmızı (R), yeşil (G), mavi (B) ve bir alpha (A) kanalı bulunur. 
Alpha kanalı, pikselin şeffaflığını belirtir.
''' 

print(f"Height:{img.shape[0]} pixel")       # sonuçta benim shape değerim bir liste şeklinde dönüyor.
print(f"Weight:{img.shape[1]} pixel")           
print(f"Channel:{img.shape[2]} pixel")

# boyutun kapladığı alan gibi düşünmeliyiz burayı aslında burada dönen olay aslında şu:
# benim yükseklik ve genişlik değerini çarptıktan sonra bunu 3 ile çarpmam gerek bunun sebebi renkli bir 
# görüntü olmasından kaynaklanıyor olması.bu openCV de şu şekilde olur en yukarıda red ortada green altta ise 
# blue vardır.bu yüzden ben size(yani) boyutumu hesaplarken 3 ile çarpıyorum.
print(f"Image Size:{img.size}")
               
cv2.waitKey(0)
cv2.destroyAllWindows()
