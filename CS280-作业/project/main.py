import dowhy
from dowhy.causal_model import CausalModel

import numpy as np
import pandas as pd
import graphviz
import networkx as nx

from IPython.display import Image, display

# np.set_printoptions(precision=3, suppress=True)
# np.random.seed(0)

data = np.load(r'C:\Users\HuanyinSSD\Desktop\hw\CS280-作业\project\npy_files\recording_09-21_08_ignore_by_default\recording_09-21_08_ignore_by_default21-09-2023-07-51-58.record.npy')
data = data.T
print(data[1])

factors = ["perception complexity", "ignore priority", "non-caution predictor", "prediction error",
    "ignore decision", "follow decision", "yield decision", "overtake decision", "planning error",
    "execution error", "accident"]

# Create a pandas DataFrame
data_df = pd.DataFrame(data, columns=factors)

# Specify the causal model
model = CausalModel(
     data=data_df,
     treatment=['ignore priority', 'non-caution predictor', 'ignore decision', 'follow decision', 'yield decision', 'overtake decision'],
    outcome=['accident'],
    common_causes=['perception complexity']
)

# Identify the causal effect
# identified_estimand = model.identify_effect()
# estimate = model.estimate_effect(identified_estimand, method_name="backdoor.linear_regression")
# print(estimate)
# print(identified_estimand)

# causal_graph = model.identify_effect().get_backdoor_graph()


# 保存因果图为PNG图像文件
# causal_graph.render(filename='causal_graph', format='png', cleanup=True)

# 显示因果图
model.view_model()


# print(type(img))
# import matplotlib.pyplot as plt 
# plt.imsave('test.jpg',img)