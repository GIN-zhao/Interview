import subprocess
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
root_dir="npy_files//"
accident=os.listdir(root_dir)
print(accident)
SAM_results=[file for file in accident if file.endswith(".json")]
for file_path in SAM_results:
        json_path=root_dir+file_path
        subprocess.run(["E:/AnaConda/envs/python-3.8/python.exe","e:/homework/desktop/hw/CS280-作业/project/run_FSGNN.py",json_path])
        
        