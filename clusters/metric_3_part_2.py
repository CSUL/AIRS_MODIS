# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import pandas as pd

path = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/EV_1KM_Emissive.npy'
bright = np.load(path)

print bright.shape
data_frame =pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/index.csv')

#path = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/bright_summary.npy'
nc_f = '/Users/sevakm/Documents/AIRS_To_Modis/weather/2013.03.02.Ascending.nc' 
nc_fid = Dataset(nc_f, 'r')  

metric3_with_clear = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/metric3_with_clear.csv')
metric3_without_clear  = metric3_with_clear.copy(deep=True)                        


# Extract data from NetCDF file
pressure = nc_fid.variables['tatm_layerPressures'][:]  # extract/copy the data


def log(x):
        return np.log(1000/x) * 7
    
log_func = np.vectorize(log)

pressure = log_func(pressure)


bottom2 = []
for index, x in enumerate(pressure):
    if x >=1 and x <=2.1:
        bottom2.append(index)

print "\n\n"

tatm_ig = nc_fid.variables['tatm_ig'][:]
tatm = nc_fid.variables['tatm'][:]
clear_sky_temp = nc_fid.variables['tsur'][:]

bottom_first = bottom2[0]
bottom_last = bottom2[len(bottom2)-1]

tatm_2km = tatm[:, bottom_first: bottom_last +1]
tatm_ig_2km = tatm_ig[:, bottom_first: bottom_last +1]

clean_tatm_2km = np.ma.array(tatm_2km, mask= np.isnan(tatm_2km))   
clean_tatm_ig_2km =np.ma.array(tatm_ig_2km, mask= np.isnan(tatm_ig_2km)) 

#==============================================================================
# plot
#==============================================================================



tatm_delete_indices =[]
for index, x in enumerate(clean_tatm_2km):
    if x.all() is np.ma.masked:
        tatm_delete_indices.append(index)

#print "shape: " + str(len(tatm_indices) *6) + "/" + str(clean_tatm_2km.size)

#tatm_ig_indices =[]
for index, x in enumerate(clean_tatm_ig_2km):
    if x.all() is np.ma.masked:
        if index not in tatm_delete_indices:
            tatm_delete_indices.append(index)

#print one_cluster.iloc[2]

#print "ones: " + str(one_cluster.shape)






#==============================================================================
# all cluster graphs
#==============================================================================

granule = nc_fid.variables['granule'][:]
scanline = nc_fid.variables['track'][:]
footprint = nc_fid.variables['xTrack'][:]


#s               0
#f              48
#g             151


#for cluster_count in np.arange(2, 8):
clusters = np.array(data_frame.loc[
        
                                (data_frame['f'] >= 26)
                                &(data_frame['f'] <= 69)
                            ])

clusters = clusters[:, 1:clusters.shape[1]-1]

current_tatm_delete_indices = tatm_delete_indices[:]

#index = np.nonzero(clusters == [134, 67, 155])
#print index

#print clusters[41]


#print clusters

#    current_good_tatm =[]

cluster_list = clusters.tolist()

#print "current_tatm_delete_indices:" + str(current_tatm_delete_indices)

#print "------"
#print cluster_list.index([134, 67, 155])

#print len(cluster_list)

#metric = np.array(metric3_with_clear)

airs_to_modis_cluster_index = []
airs_to_modis_cluster_index_temperature_10 = []

for x in range(tatm_2km.shape[0]):
    if x not in current_tatm_delete_indices:
        tatm_pos_arr= []
        
        tatm_s = scanline[x]
        tatm_f = footprint[x]
        tatm_g =granule[x]
        
        tatm_pos_arr.append(tatm_s)
        tatm_pos_arr.append(tatm_f)
        tatm_pos_arr.append(tatm_g)
        
        if tatm_pos_arr in cluster_list:
            index = cluster_list.index(tatm_pos_arr)
            if index ==48:
                print "!!!!!!!!!!!!!!!!!!!!!!"
            
            airs_to_modis_cluster_index.append(index)
      
            if metric3_with_clear.iloc[index]['t10'] ==-1:
#                print "index: " + str(clear_sky_temp[x])
                metric3_without_clear.set_value(index, 't10',  clear_sky_temp[x])
                airs_to_modis_cluster_index_temperature_10.append(index)
#                if np.isnan(clear_sky_temp[x]):
#                    print "index: " + str(index)
#                    print "sky x: " + clear_sky_temp[x]
        
    print str(x) + '/' + str(tatm_2km.shape[0])
            
#
metric3_without_clear.to_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/metric3_without_clear.csv')
np.save('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/airs_to_modis_cluster_index_temperature_10.npy', np.array(airs_to_modis_cluster_index_temperature_10))
np.save('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/airs_to_modis_cluster_index.npy', np.array(airs_to_modis_cluster_index))
#cluster_path = '/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/cluster'
#cluster_path = cluster_path + str(7) + ".npy"