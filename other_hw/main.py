import cv2 



img = cv2.imread(r'E:\homework\desktop\hw\other_hw\1.png')

img = cv2.resize(img,(170,100))

cv2.imwrite('res.jpg',img)