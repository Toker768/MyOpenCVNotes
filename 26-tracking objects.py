import cv2 
import numpy as np 

cap = cv2.VideoCapture("1dog.mp4")

while True:
    ret,orijinal = cap.read()

    hsv = cv2.cvtColor(orijinal, cv2.COLOR_BGR2HSV) # I explained this HSV concept(kavram) in the notebook

    # there is dog in the video, so I find the HSV value of the white.
    sensitivity = 15
    lower_white = np.array([0,0,168])
    upper_white = np.array([172,111,255])

    mask = cv2.inRange(hsv,lower_white,upper_white)            # or white or black
    #                  image,min color value, max color value
    '''
     Bu fonksiyon, bir görüntüdeki piksellerin renk değerlerini belirli bir aralığa göre kontrol 
     eder ve aralıkta olan pikselleri 1 (beyaz) olarak, aralıkta olmayan pikselleri ise 0 (siyah) 
     olarak işaretler.
    '''

    final_State = cv2.bitwise_and(orijinal,orijinal,mask=mask)
    '''
    cv2.bitwise_and() fonksiyonunu kullanarak orijinal çerçeve (frame) ve maskesi (mask) ile bitwise AND 
    işlemini uygular. Bu işlem, hem çerçevede hem de maskede beyaz olan pikselleri korur ve beyaz alanları 
    etkin bir şekilde izole ederek diğer tüm pikselleri siyah yapar. Bu yaklaşım, cv2.bitwise_or() 
    kullanmaktan genelde daha verimlidir.

    ın fact my purpose in using this is to filter
    '''

    cv2.imshow("Frames", orijinal)
    cv2.imshow("With Mask", mask)
    cv2.imshow("Result", final_State)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()











