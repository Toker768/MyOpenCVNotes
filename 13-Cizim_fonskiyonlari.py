import cv2
import numpy as np
# aslında numPy bize bir tuval oluşturuyor gibi düşünmek oldukça mantıklı.

'''
canvas = np.zeros((10,10,3), dtype=np.uint8) 


canvas[0,0] = (255,255,255)     
canvas[0,1] = (255,100,255)
canvas[0,2] = (255,255,255)
canvas[0,3] = (255,45,255)
canvas[0,4] = (100,100,144) 
canvas[0,5] = (10,10,10)

canvas = cv2.resize(canvas, (512,512), interpolation=cv2.INTER_AREA) #bunun amacı yapmış olduğum
# değişiklikleri net bir şekilde görebilmek.

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''



'''
canvas2 = np.zeros((10,10), dtype=np.uint8) 

canvas2[0,0] = 255   
canvas2[0,1] = 200
canvas2[0,2] = 150
canvas2[0,3] = 100
canvas2[0,4] = 50 
canvas2[0,5] = 10


canvas2 = cv2.resize(canvas2, (512,512), interpolation=cv2.INTER_AREA)
cv2.imshow("Canvas", canvas2)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''