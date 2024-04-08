from collections import defaultdict

import numpy as np
import matplotlib.image as mpimg    # 用于读取
import matplotlib.pyplot as plt     # 用于显示
import logging
import cv2 

logging.basicConfig(level=logging.INFO)

# 直方图均衡化
class Histogram(object):
    def __init__(self):
        pass
    # 显示直方图
    def showByHistogram(hist,*,title = ''):
        x_axis = range(0,256)
        y_axis = list(map(lambda x : hist[x] ,x_axis))

        fig = plt.figure(num = title)
        plot_1 = fig.add_subplot(111)
        plot_1.set_title(title)
        plot_1.plot(x_axis,y_axis)
        plt.show()
        del fig

    def show(img,*,title = ''):
        # 只取单通道
        img = img[:,:,0]
        size_h,size_w= img.shape
        logging.info(f' size_h :{size_h} size_w:{size_w} MN:{size_w*size_h}')

        hist = defaultdict(lambda: 0)

        for i in range(size_h):
            for j in range(size_w):
                hist[img[i,j]] += 1
        x_axis = range(0,256)
        y_axis = list(map(lambda x : hist[x] ,x_axis))

        fig = plt.figure(num = title)
        plot_1 = fig.add_subplot(111)
        plot_1.set_title(title)
        plot_1.plot(x_axis,y_axis)
        plt.show()
        del fig
    # 获取直方图，参数Normalized 决定是否归一化
    def get_histogram(img ,*,Normalized = False):
        # 只取 0 通道，若本身只有一个通道不会有影响
        img = img[:,:,0]
        size_h,size_w = img.shape
        logging.info(f' size_h :{size_h} size_w:{size_w} MN:{size_w*size_h}')

        hist = defaultdict(lambda: 0)
        
        for i in range(size_h):
            for j in range(size_w):
                hist[img[i,j]] += 1
                
        # 根据 Normalized 参数决定是否进行归一化
        if Normalized == True:
            sum = 0
            MN = size_h * size_w
            for pixel_value in hist: # Key 迭代
                hist[pixel_value] = hist[pixel_value]/MN
                sum += hist[pixel_value]
            logging.info(f'归一化后加和为：{sum}')
            del sum
        return hist
    # 直方图均衡化函数
    def equalization(img):
        size_h,size_w,size_c = img.shape
        hist = Histogram.get_histogram(img)
        MN = size_h * size_w
        new_hist = defaultdict(lambda: 0)
        # 公式 3.3-8 计算 S_k
        for i in range(0,256):
            for pixel in range(i+1):
                new_hist[i] += hist[pixel]
            new_hist[i] = new_hist[i] * 255/MN
        
        for key in new_hist:
            new_hist[key] = round(new_hist[key])
        new_img = img.copy()
        
        for i in range(new_img.shape[0]):
            for j in range(new_img.shape[1]):
                new_img[i,j] = new_hist[new_img[i,j,0]]

        return new_img
    pass


    def clip_histogram(self,hist, clip_limit, total_pixels):
        clip_value = clip_limit * total_pixels
        excess = np.maximum(0, hist - clip_value)
        excess_total = excess.sum()
        
        if excess_total > 0:
            redistribute_value = excess_total // 256
            hist = np.minimum(hist, clip_value) + redistribute_value
        
        return hist

    def apply_clahe_patch(self,img, patch_size=41, center_size=3, clip_limit=0.02):
        print(img.shape)
        H, W,_ = img.shape
        # new_img = np.zeros_like(img)
        new_img = img.copy()
        half_patch = patch_size // 2
        half_center = center_size // 2

        for y in range(half_patch, H - half_patch):
            for x in range(half_patch, W - half_patch):
                patch = img[max(y - half_patch, 0):min(y + half_patch + 1, H),
                            max(x - half_patch, 0):min(x + half_patch + 1, W)]
                
                hist, _ = np.histogram(patch, bins=256, range=(0, 256))
                hist = self.clip_histogram(hist, clip_limit, patch.size)
                cdf = hist.cumsum()
                cdf_normalized = 255 * cdf / cdf[-1]
                eq_patch = np.interp(patch, np.arange(256), cdf_normalized).reshape(patch.shape)
                
                # Update the center patch
                center = eq_patch[half_patch - half_center:half_patch + half_center + 1,
                                half_patch - half_center:half_patch + half_center + 1]
                new_img[y - half_center:y + half_center + 1, x - half_center:x + half_center + 1] = center
                
        return new_img
    
'''
    def clahe(img, clip_limit=2.0, grid_size=(41, 41)):
            img = img[:, :, 0]
            size_h, size_w = img.shape
            logging.info(f' size_h :{size_h} size_w:{size_w} MN:{size_w*size_h}')

            grid_h, grid_w = grid_size
            h_step = size_h // grid_h
            w_step = size_w // grid_w

            for i in range(h_step):
                for j in range(w_step):
                    y_start, y_end = i * grid_h, (i + 1) * grid_h
                    x_start, x_end = j * grid_w, (j + 1) * grid_w

                    grid_pixels = img[y_start:y_end, x_start:x_end]

                    hist, bins = np.histogram(grid_pixels.flatten(), bins=256, range=(0, 256))
                    cdf = hist.cumsum()
                    cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
                    clahe_mapping = np.round(cdf_normalized).astype(np.uint8)
                    grid_pixels_eq = clahe_mapping[grid_pixels]

                    hist, _ = np.histogram(grid_pixels_eq.flatten(), bins=256, range=(0, 256))
                    hist_cumsum = hist.cumsum()
                    hist_cumsum_clipped = np.clip(hist_cumsum, 0, clip_limit * h_step * w_step) / (clip_limit * h_step * w_step)
                    hist_cumsum_mapped = (hist_cumsum_clipped * 255).astype(np.uint8)
                    grid_pixels_eq = hist_cumsum_mapped[grid_pixels_eq]
                    # img[y_start:y_end, x_start:x_end] = grid_pixels_eq
                    img[y_start+19:y_end-19, x_start+19:x_end-19] = grid_pixels_eq[19:22,19:22]

            return img



'''
if __name__ == '__main__':

    # pic1 = mpimg.imread('../image/grain.tif')  # 读取图像
    pic1 = cv2.imread('../image/tire.tif')

    # 获取直方图
    # Histogram.show(pic1,title='pic1_Histogram')

    # Histogram.showByHistogram(Histogram.get_histogram(pic1,Normalized=True),title='pic1_Histogram')


    # Histogram.show(pic1,title='pic1_Histogram')

    # 直方图均衡化
    # new_pic = Histogram.equalization(pic1)

    #自适应直方图均衡化
    t = Histogram()
    new_pic = t.apply_clahe_patch(pic1)
    # plt.imshow(pic1)
    # plt.axis('off')
    plt.imshow(new_pic)
    # plt.axis('off')
    # plt.show()

    cv2.imwrite('CLAHE.jpg',new_pic)
    # Histogram.show(pic1,title='pic1_Histogram')
    # Histogram.show(new_pic,title='pic1_Histogram after equalization')
    # mpimg.imsave('../image/output_HistogramEqualization.jpg',new_pic)


