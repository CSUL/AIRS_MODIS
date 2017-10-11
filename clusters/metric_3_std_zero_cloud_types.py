# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

path = '/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/metric_3_ZERO_std_cloud_types.npy'

#arr = np.load(path)
#
#print arr.shape


df = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/metric_3_ZERO_std_cloud_types.csv')

print df.shape


print df[df['cloud_10'] ==1].shape

#
df1 = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/metric_3_std_cloud_types_ALL.csv')

print df1.shape
print df1[df1['cloud_8'] ==1].shape

