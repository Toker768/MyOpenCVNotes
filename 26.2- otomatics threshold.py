# First of all, I want to understand the concept(kavram) called 'thresholding'. While looking at this concept, 
# I saw that automatic thresholding is done with the help of histogram.

# how the make histogram ? 

import cv2
import matplotlib.pyplot as plt

# Görüntüyü okuyun
img = cv2.imread("1ilkaskim.jpg")

# Histogramı hesaplayın
# hist = cv2.calcHist([img], [0], None, [256], [0, 256])  --> bu siyah beyaz lar için geçerli bir kod.



hist = cv2.calcHist([img], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])

# Histogramı gösterin
plt.plot(hist[:, :, 0], label="Mavi")
plt.plot(hist[:, :, 1], label="Yeşil")
plt.plot(hist[:, :, 2], label="Kırmızı")
plt.legend()
plt.show()
