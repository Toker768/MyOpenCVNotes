import cv2
'''
img = cv2.imread("1Fahrettin_pasa.jpg")    # bu benim görüntümü okumamı yani piksellere ayırmamı sağladı.
# print(img)

# şimdi ben burada bir pikselin değil bir bölgenin renk değerini değiştiricem.seyrett.

corner = img[0:600,0:375]         # y ekseninde 0'dan 300'e kadar olan ile x ekseninde 0'dan 400'ye kadar olan alanı
# ben taradım burada.Hiçbirseyi ezberlemene gerek yoktur deneyerek bunları yapabiliriz burada biz.
# burada ben ilk başta satır sonra sütün mantığı ile hareket ediyoruz.

cv2.imshow("Üstad", img)
cv2.imshow("Corner", corner)


cv2.waitKey(0)             # demekki benim bunları bir tane koymam gayet yeterli olacakmış.
cv2.destroyAllWindows()
'''


'''
img = cv2.imread("1images_opencv.png")    
corner = img[0:200,0:200]       


img[0:100, 0:250] = (255,0,0) # bu şu demek ben y ekseninde 0'dan 100'e kadar olan kısım ile x ekseninden 
                                     # 0'dan 250'ye kadar olan tarafı maviye boyadım.
# maviye boyamamın mantığı ise şuradan geliyor "BGR" den dolayı aslında.


cv2.imshow("OpenCV", img)
cv2.imshow("Corner", corner)



cv2.waitKey(0)            
cv2.destroyAllWindows()
'''















