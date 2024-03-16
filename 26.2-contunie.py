# First of all, I want to understand the concept(kavram) called 'thresholding'. While looking at this concept, 
# I saw that automatic thresholding is done with the help of histogram.

# how the make histogram 
 

import cv2
import matplotlib.pyplot as plt

# Görüntüyü okuyun
img = cv2.imread("1ilkaskim.jpg")


# Histogramı hesaplayın
hist = cv2.calcHist([img], [0], None, [256], [0, 256])  # bu sadece 0. yani blue renk kanalinı ölçtü.
# green ve red'e sıra gelmedi burada.
# for example my converted from color to the gray this same, eğer renkli yapıcaksam bunun her parametresi
# 3 katına çıkarıcan.

# Histogramı gösterin
plt.plot(hist)
plt.xlabel("Gri Tonlama Değeri")
plt.ylabel("Piksel Sayısı")
plt.show()