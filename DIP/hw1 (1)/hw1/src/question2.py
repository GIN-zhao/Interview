import numpy as np
import cv2
from numpy import *
# 读取图像
image = cv2.imread('../image/moon.jpg', cv2.IMREAD_GRAYSCALE)

#(1)
# 定义 Laplacian 核的分离版本
laplacian_x = np.array([[0, 1, 0],
                        [0, -2, 0],
                        [0, 1, 0]])

laplacian_y = np.array([[0, 0, 0],
                        [1, -2, 1],
                        [0, 0, 0]])

# 应用 x 方向的 Laplacian 核
image_laplacian_x = cv2.filter2D(image, -1, laplacian_x)

# 应用 y 方向的 Laplacian 核
image_laplacian_y = cv2.filter2D(image, -1, laplacian_y)

# 显示处理后的图像
# cv2.imshow('Laplacian X', image_laplacian_x)
g_x = image - image_laplacian_x
g_y = image - image_laplacian_y
g_y[g_y<0] = 0 
g_x[g_x<0]  = 0 
g_x[g_x>255]  = 255 
g_y[g_y>255]  = 255

# cv2.imwrite('Laplacian_X.jpg', g_x)

# cv2.imwrite('Laplacian_Y.jpg', g_y)
                    

#（2）
# 未分离的 3 × 3 Laplacian 核
laplacian = np.array([[0, 1, 0],
                      [1, -4, 1],
                      [0, 1, 0]])

# 应用 Laplacian 核进行 2-D 卷积
image_sharpened = cv2.filter2D(image, -1, laplacian)

g  = image - image_sharpened 
g [g<0] = 0
g [g>255] = 255
# 显示处理后的图像
# cv2.imwrite('laplacian2D.jpg', g)


#(3)
# 使用 unsharp mask 进行图像锐化

image = cv2.imread('../image/moon.jpg') # 根据路径读取一张图片
 
 
reflect_img = cv2.copyMakeBorder(image,1,1,1,1,cv2.BORDER_REPLICATE)#填充边界像素
x,y=reflect_img.shape[:2]
for depth in range(0,3):
    for rows in range(1,x-1):
        for colums in range(1,y-1):
            HighPass = (reflect_img.item(rows,colums,depth)<<2)-reflect_img.item(rows-1,colums,depth)\
                        -reflect_img.item(rows+1,colums,depth)- reflect_img.item(rows,colums-1,depth)\
                        -reflect_img.item(rows,colums+1,depth)
 
            Value = image.item(rows-1,colums-1,depth)+100*HighPass//100
            if(Value > 255):
                Value = 255
            elif(Value < 0):
                Value = 0
 
            image.itemset((rows-1,colums-1,depth),Value)

 
cv2.imwrite("Unsharp_mask.jpg",image)

