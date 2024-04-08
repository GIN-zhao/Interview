import cv2 
import numpy as np

def GaussianFilter(img):
    
    h,w,c = img.shape
    # 高斯滤波 
    K_size = 3
    sigma = 1.3
    
    # 零填充
    pad = K_size//2
    out = np.zeros((h + 2*pad,w + 2*pad,c),dtype=np.float32)
    out[pad:pad+h,pad:pad+w] = img.copy().astype(np.float32)
    
    # 定义滤波核
    K = np.zeros((K_size,K_size),dtype=np.float32)
    
    for x in range(-pad,-pad+K_size):
        for y in range(-pad,-pad+K_size):
            K[y+pad,x+pad] = np.exp(-(x**2+y**2)/(2*(sigma**2)))
    K /= (sigma*np.sqrt(2*np.pi))
    K /=  K.sum()
    
    # 卷积的过程
    tmp = out.copy()
    for y in range(h):
        for x in range(w):
            for ci in range(c):
                out[pad+y,pad+x,ci] = np.sum(K*tmp[y:y+K_size,x:x+K_size,ci])
    
    out = out[pad:pad+h,pad:pad+w].astype(np.uint8)
    
    return out

def median_filter(image, kernel_size):
    # 获取图像的高度和宽度
    height, width = image.shape[:2]
    # 计算中值滤波器的半径
    radius = kernel_size // 2
    # 创建一个空白的图像来存储滤波后的结果
    filtered_image = np.zeros_like(image)
    
    for y in range(height):
        for x in range(width):
            # 提取当前像素周围的像素值
            neighbors = []
            for j in range(-radius, radius + 1):
                for i in range(-radius, radius + 1):
                    # 边界检查
                    if (y + j >= 0 and y + j < height and x + i >= 0 and x + i < width):
                        neighbors.append(image[y + j, x + i])
            # 计算邻域的中值并将其分配给当前像素
            filtered_image[y, x] = np.median(neighbors)
    
    return filtered_image
if __name__ == "__main__":
    
    # 读取图像
    # img = imageio.imread("../image/lena_noisy.tif")
    img = cv2.imread("../image/lena_noisy.tif")

    # 高斯滤波
    cv2.imwrite("median_blur.jpg",median_filter(img,3))
