import os 
import PIL
from PIL import Image,ImageEnhance
folder_path = os.path.abspath('./img1')

file_names = os.listdir(folder_path)

# 图片列表
images = []

for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        img = Image.open(file_path)
        img = img.resize((300, 300))  # 调整图片大小为 228x228
        enhanced_img = ImageEnhance.Sharpness(img).enhance(2.0)  # 调整清晰度（这里使用2.0作为例子，你可以调整这个值）
        images.append(enhanced_img)
        # images.append(img)

# 计算排列方式
cols = 4  # 每行显示的图片数量
rows = 6

# 计算合并后的图像尺寸
width = cols * 228
height = rows * 228

# 创建新的图像对象，用于合并图片
merged_image = Image.new('RGB', (width, height), color='white')

# 合并图片
for i, img in enumerate(images):
    x = i % cols * 228
    y = i // cols * 228
    merged_image.paste(img, (x, y))

# 显示合并后的图片
# merged_image.show()
merged_image.save('merged_image_arranged2.jpg')