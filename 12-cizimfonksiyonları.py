import cv2 
import numpy as np


canvas = np.zeros((200,200,3), dtype=np.uint8)
print(canvas)
# np.zeros fonksiyonunu kullanarak 512x512 boyutlarında, her bir pikseli 3 renk kanalına sahip (BGR) 
# bir siyah tuval oluşturur. bu veri tipi seçimide bir standdarttır.

'''
Yani, canvas adlı NumPy dizisi, her bir elemanı 8-bitlik üç renk kanalına sahip bir pikseli temsil 
eden bir görüntüyü tutar. Bu, çok yaygın bir kullanımdır çünkü genellikle renkli görüntülerde 8-bit 
derinliği kullanılır.
Zaten neredeyse her zaman ben bunu kullanırım aksi durumlar olmadığı sürece bu aksi durumlarda ya görüntü 
çok büyük olur yada çok küçük gibi.
'''


'''
cv2.imshow("Canvas", canvas)       # bana siyah rengini verecektir.çünkü matrisde sıfır değerlerin 
cv2.waitKey(0)                     # karşılığı siyah olacaktır.
cv2.destroyAllWindows()
'''




# şimdi ben bu oluşturmuş olduğum siyah tobloyu beyaza nasıl çeviricem matrislerde olan bütün sıfırları 
# 255 ekleyerek.

'''
canvas2 = np.zeros((512,512,3), dtype=np.uint8) + 255
# print(canvas2)
cv2.imshow("Canvas", canvas2)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

