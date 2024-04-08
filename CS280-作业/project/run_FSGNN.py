#Import libraries
import cdt
from cdt import SETTINGS
SETTINGS.verbose=True
# SETTINGS.GPU = 1
# SETTINGS.njobs = 1 
SETTINGS.GPU = 0 
import networkx as nx
import time
# A warning on R libraries might occur. It is for the use of the r libraries that could be imported into the framework
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from cdt.independence.graph import FSGNN
import sys
import os
import pickle 
from cdt.causality.pairwise import GNN
from cdt.utils.graph import dagify_min_edge

file_path=sys.argv[1]
name=os.path.basename(file_path)[:-5]
json_file_path =file_path
data = pd.read_json(json_file_path)
data = data.sample(n=50000, random_state=42)



print('start')
Fsgnn = FSGNN(train_epochs=1, test_epochs=1, l1=0.1, batch_size=1000,njobs=1)
print('train')
start_time = time.time()
ugraph = Fsgnn.predict(data, threshold=1e-7)
print("--- Execution time : %4.4s seconds ---" % (time.time() - start_time))

start_time = time.time()

gnn = GNN(nruns=32, train_epochs=1, test_epochs=1, batch_size=1000)
mode_path='model_FSGNN_'+name+'.pkl'

ograph = dagify_min_edge(gnn.orient_graph(data, ugraph))
with open(mode_path, 'wb') as file:
    pickle.dump(gnn, file)
print("--- Execution time : %4.4s seconds ---" % (time.time() - start_time))

# List results
df2=pd.DataFrame(list(ograph.edges(data='weight')), columns=['Cause', 'Effect', 'Score'])
df2.to_csv('E:\homework\desktop\hw\CS280-作业\project\\results_FSGNN\\'+'FSGNN_'+name+'.csv')
print("finished  "+name)


