import cv2


'''
img1 = cv2.imread("1bitwase.png")
img2 = cv2.imread("1bitwase1.png")

bit_and = cv2.bitwise_and(img1,img2)    # ben öncelikle zaten 'bitwise_and' siyah beyaz ekranlarda kullanırım
# mantıkda şu şekilde işliyor iki resimde eğer siyah siyah olursa siyah oluyor siyah beyaz olursa siyah oluyor
# aslında mantık konusundaki 've' 'veya' mantığı ile aynıdır.Neredeyse bir farkı yok desek yalan olmaz.


cv2.imshow("bitAnd", bit_and)
cv2.imshow("Original1", img1)
cv2.imshow("Original2", img2)
'''


'''
img1 = cv2.imread("1bitwase.png")
img2 = cv2.imread("1bitwase1.png")

bit_or = cv2.bitwise_or(img1,img2)  # buda yukardakinden tek farkı ve değil veya kullanması diyebilirim.  


cv2.imshow("bitOr", bit_or)
cv2.imshow("Original1", img1)
cv2.imshow("Original2", img2)
'''

'''
img1 = cv2.imread("1bitwase.png")
img2 = cv2.imread("1bitwase1.png")

bit_Xor = cv2.bitwise_xor(img1,img2)    


cv2.imshow("bitNot", bit_Xor)          # bu xor da 've' nin tam tersi değer veriyor burada.
cv2.imshow("Original1", img1)
cv2.imshow("Original2", img2)
'''



'''
img1 = cv2.imread("1bitwase.png")


bit_not = cv2.bitwise_not(img1)        # siyah beyaz olan fotağrafımı ters çevirdi renklerini aslında mantık    
# bu

cv2.imshow("bitNot", bit_not)
cv2.imshow("Original1", img1)

'''


cv2.waitKey(0)
cv2.destroyAllWindows()

