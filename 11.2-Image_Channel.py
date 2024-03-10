import cv2 
import numpy as np

img = cv2.imread("1images_opencv.png")  
print(f"Shape:{img.shape}")                 

(B, G, R) = cv2.split(img)        


# şimide ben bir tane siyah ekran oluşturuyim ardından bunu oluştururken şöyle bir şey yapıcam.
black = np.zeros(img.shape[:2], dtype="uint8") 
                 # bu parametreye ben böyle yükseklik ve enini giriyorum 
                 # burada ondan sonra opsiyonel olarak matrisin
                 # veri tipinide tanımlayabiliyorum.
# cv2.imshow("Black window", black)

cv2.imshow("Red", cv2.merge([black, black, R]))
                            # değişken vermem gereken noktada ben cv2.merge'vermemin sebebi renkeli uygun
                            # şekilde yakalama istediği.
cv2.imshow("Green", cv2.merge([black, G, black]))               
cv2.imshow("Blur", cv2.merge([B, black, black]))



cv2.waitKey(0)
cv2.destroyAllWindows()