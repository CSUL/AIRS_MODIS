#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:22:30 2017

@author: sevakm
"""



import matplotlib.pyplot as plt
import numpy as np
from pyhdf.SD import SD, SDC
import pandas as pd
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/
import scipy
import mod_br as mod_br
#import ModisData as MD


# Open file.
FILE_NAME1 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/MYD021KM.A2013061.1500.006.2013062154358.hdf'
FILE_NAME2 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/MYD021KM.A2013061.1505.006.2013062154129.hdf'
FILE_NAME3 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/MYD021KM.A2013061.1510.006.2013062154211.hdf'
FILE_NAME4 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/MYD021KM.A2013061.1515.006.2013062154238.hdf'
FILE_NAME5 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/MYD021KM.A2013061.1520.006.2013062153907.hdf'
FILE_NAME6 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/MYD021KM.A2013061.1525.006.2013062154158.hdf'
FILE_NAME7 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/MYD021KM.A2013061.1530.006.2013062153847.hdf'
FILE_NAME8 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/MYD021KM.A2013061.1535.006.2013062161543.hdf'

hdf1 = SD(FILE_NAME1, SDC.READ)
hdf2 = SD(FILE_NAME2, SDC.READ)
hdf3 = SD(FILE_NAME3, SDC.READ)
hdf4 = SD(FILE_NAME4, SDC.READ)

hdf5 = SD(FILE_NAME5, SDC.READ)
hdf6 = SD(FILE_NAME6, SDC.READ)
hdf7 = SD(FILE_NAME7, SDC.READ)
hdf8 = SD(FILE_NAME8, SDC.READ)



#print hdf.attributes()

print "\n\n"
#==============================================================================
# CLOUD TOP PRESSURE
#==============================================================================

## # Read dataset.
DATAFIELD_NAME='EV_1KM_Emissive'

data3D1 = hdf1.select(DATAFIELD_NAME)
data3D2 = hdf2.select(DATAFIELD_NAME)
data3D3 = hdf3.select(DATAFIELD_NAME)
data3D4 = hdf4.select(DATAFIELD_NAME)

data3D5 = hdf5.select(DATAFIELD_NAME)
data3D6 = hdf6.select(DATAFIELD_NAME)
data3D7 = hdf7.select(DATAFIELD_NAME)
data3D8 = hdf8.select(DATAFIELD_NAME)

#scale_factor = getattr(data3D1, "scale_factor")

data1 = data3D1[:,:]
data2 = data3D2[:,:]
data3 = data3D3[:,:]
data4 = data3D4[:,:]
data5 = data3D5[:,:]
data6 = data3D6[:,:]
data7 = data3D7[:,:]
data8 = data3D8[:,:]

#print data1.shape

band_index = 11
band  =32
data=np.concatenate( [data1[band_index],data2[band_index],data3[band_index]
                    ,data4[band_index],       
                      data5[band_index],data6[band_index],
                      data7[band_index],data8[band_index]], axis=0)
#data = data1

#print "bad vals: " + str(len(data[data >32767]))
#print "min: " + str(np.mean(data))
#print "max: " + str(np.max(data))


radiance_scale = getattr(data3D1, 'radiance_scales')[band_index]
radiance_offset = getattr(data3D1, 'radiance_offsets')[band_index]
print data[0][0]
def scale(x):
    return radiance_scale *(x-radiance_offset)

scale_func = np.vectorize(scale)

data = scale_func(data)
print data[0][0]


modBT = scipy.vectorize(mod_br.modis_bright)
data = modBT(data,1,int(band),1)

print data[0][0]


#==============================================================================
# READ index file
#==============================================================================
nc_f = '/Users/sevakm/Documents/index-airs.aqua_modis.aqua-v1.0-2013.03.02.1500.nc4'  # Your filename
nc_fid = Dataset(nc_f, 'r') 

col_pt = nc_fid.variables['Column_Point'][:]
row_pt = nc_fid.variables['Row_Point'][:]

path = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/' + DATAFIELD_NAME + '.npy'

##array containing all cluster chunks
array = []

for a in range(675):
    for b in range(90):
        col = col_pt[a][b]
        row = row_pt[a][b]
        
        if(col <0 or row <0):
            array.append(np.negative(np.ones((19, 39)))) 
#            print "len of zeros: " + str(np.zeros((19, 39)).shape)
        else:
            i0 = col -20
            i1 = col + 19
            
            j0 = row -10
            j1 = row + 9
            patch = data[j0:j1, i0:i1]
#            print "patch shape: " + str(np.array(patch).shape)
    #        print patch
            array.append(patch)
    
    print str(a) + "/675"
  
    
np_arr = np.array(array)
np.save(path, np_arr)






