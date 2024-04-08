import matplotlib.pyplot as plt

# 从文本文件中读取数据
file_path = "../source/hw1_result.txt"  # 请将文件路径替换为您的实际文件路径
with open(file_path, "r") as file:
    data = [tuple(map(float, line.strip().split())) for line in file]
file_path = "../source/hw1_result.txt"  # 请将文件路径替换为您的实际文件路径
with open(file_path, "r") as file:
    data_ = [tuple(map(float, line.strip().split())) for line in file]
# 提取 x 和 y 坐标
x = [point[0] for point in data]
y = [point[1] for point in data]

x_ = [point[0] for point in data_]
y_ = [point[1] for point in data_]
# 绘制直线连接点
plt.plot(x, y, marker='o', linestyle='-')
# plt.plot(x_, y_, marker='*', linestyle='-',color='r')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Plot of Points')
plt.grid(True)
# plt.show()
plt.savefig('../source/plot_origin.png')