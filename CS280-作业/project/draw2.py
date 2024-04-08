import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
root_dir="results_FSGNN"
files=os.listdir(root_dir)
SAM_results=[file for file in files if file.endswith(".csv")]
for file_path in SAM_results:
        df = pd.read_csv(file_path)
        savename=os.path.basename(file_path)[:-4]


        # df = pd.DataFrame(data)

        # 新的数据结构
        columns = ["perception complexity", "ignore priority", "non-caution predictor", "prediction error",
                "ignore decision", "follow decision", "yield decision", "overtake decision",
                "planning error", "execution error", "accident"]

        # 使用pivot_table将DataFrame转换为矩阵
        matrix = df.pivot_table(index='Cause', columns='Effect', values='Score', aggfunc='mean', fill_value=0)

        # 重新排列矩阵的行和列
        matrix = matrix.reindex(index=columns, columns=columns)
        np.save(root_dir+'//Matrix//'+savename+"_matrix.np")
        # 创建绘图
        plt.figure(figsize=(8, 6))
        plt.imshow(matrix.values, cmap='viridis', interpolation='nearest')
        plt.colorbar(label='Weight')
        plt.title('Causality Matrix')
        plt.xlabel('Effect')
        plt.ylabel('Cause')
        plt.xticks(np.arange(len(columns)), columns, rotation=45, ha="right")
        plt.yticks(np.arange(len(columns)), columns)
        plt.savefig(root_dir+'//Matrix//'+savename+".png")

        # 显示图像
        # plt.show()
