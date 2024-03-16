import cv2 
import numpy as np

'''
matris = np.arange(24).reshape(4, 6)
#image = cv2.imread(matris)          Bu kod hata vericektir.Çünkü cv2.imread bir matrisi değil görüntü
# okur.
'''

'''
# Belirli bir sayıyla doldurulmuş 4x6 boyutunda bir matris oluşturun.
matris = np.full((2, 3), 120)
# print(matris)


# Matrisi bir görüntü dosyası olarak kaydedin.
cv2.imwrite("resim.jpg", matris)


image = cv2.imread("resim.jpg")
print(image)
'''

# cv2.imshow("Resim", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


cv2.namedWindow("Myimage", cv2.WINDOW_AUTOSIZE )

img = cv2.imread("1cakma_asker.jpg")            

img = cv2.resize(img, (600,600), interpolation=cv2.INTER_LINEAR)

cv2.imshow("Myimage", img)               
cv2.waitKey(0)
cv2.destroyAllWindows()


