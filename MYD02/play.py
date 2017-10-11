# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import pandas as pd

#
path = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/bright_summary.npy'
nc_f = '/Users/sevakm/Documents/AIRS_To_Modis/weather/2013.03.02.Ascending.nc' 
nc_fid = Dataset(nc_f, 'r')  
#                             
#
#
#

#print np.load('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/airs_to_modis_cluster_index.npy').shape
path = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/EV_1KM_Emissive.npy'
bright = np.load(path)

bright_arr = []

for x in bright:
    bright_arr.append(np.std(x))

plt.figure(figsize =(8, 6))
n, b ,p =plt.hist(bright_arr, normed=1, 
                  bins =1000,
                  histtype = 'step',
#                  range =[0,1],
                  cumulative=True)
plt.title("cumulative distribution of Brightness Temperature STD")
plt.xlabel("STD")


#clear = nc_fid.variables['tsur'][:]

#print clear[np.isnan(clear)].shape


#arr = clear[~np.isnan(clear)]
#
#print clear[0]
#
#x = clear[0]
#
#print x
#
#print np.arange(29, 30, 1)



#print clear[clear ==0].shape
#
#print clear[np.isnan(clear)].shape
#
#print np.isnan(clear)
#
#print clear[0]
#
#clear = np.ma.array(clear, mask= np.isnan(clear))  
#print np.mean(clear)
#print np.max(clear)
#
#
#tatm_ig = nc_fid.variables['tatm_ig'][:]
#
#print "tatm_ig: " + str(tatm_ig.shape)

#metric = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/metric3_without_clear.csv')


#print metric.loc[(metric['t10'] !=0) & (metric['t10'] !=-1)].shape
#print np.array(metric.loc[metric['t10'] ==0]).shape
#for metric_index, data_index in enumerate(range(1, 31, 3)):
#    print str(metric_index) + ":" + str(data_index)
#indices = np.load('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/airs_to_modis_cluster_index_temperature_10.npy')
#
#print indices.shape

#print np.std([277.8732468, 272.21865, 271.3697979, 284.4765625])
#data_frame =pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/index.csv')

#print data_frame.iloc[48]
#print np.array(metric['t10']).shape

#print metric.iloc[0]['t7']
#path = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/EV_1KM_Emissive.npy'
#bright = np.load(path)
#count = 0
#for index, x in enumerate(bright):
#    if np.average(x) ==-1:
#        count = count +1
#    print index
#
#print "count: " + str(count)