import os
import pickle as pkl
import sys
import networkx as nx
import numpy as np
import scipy.sparse as sp
import torch
from visualization import visualize

feat = np.load('/media/ncclab/database2/ziyuan/dataset/MAXP/features.npy')
print(feat.shape)