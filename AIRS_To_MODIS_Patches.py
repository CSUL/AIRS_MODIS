#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:56:30 2017

@author: sevakm
"""



import matplotlib.pyplot as plt
import numpy as np
from pyhdf.SD import SD, SDC
import pandas as pd
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/


# Open file.
FILE_NAME1 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD06_L2.A2013061.1500.006.2014260111924.hdf'
FILE_NAME2 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD06_L2.A2013061.1505.006.2014260105224.hdf'
FILE_NAME3 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD06_L2.A2013061.1510.006.2014260104633.hdf'
FILE_NAME4 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD06_L2.A2013061.1515.006.2014260104129.hdf'
FILE_NAME5 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD06_L2.A2013061.1520.006.2014260105602.hdf'
FILE_NAME6 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD06_L2.A2013061.1525.006.2014260111232.hdf'
FILE_NAME7 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD06_L2.A2013061.1530.006.2014260113113.hdf'
FILE_NAME8 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD06_L2.A2013061.1535.006.2014260095958.hdf'

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
DATAFIELD_NAME='cloud_top_temperature_1km'

data3D1 = hdf1.select(DATAFIELD_NAME)
data3D2 = hdf2.select(DATAFIELD_NAME)
data3D3 = hdf3.select(DATAFIELD_NAME)
data3D4 = hdf4.select(DATAFIELD_NAME)

data3D5 = hdf5.select(DATAFIELD_NAME)
data3D6 = hdf6.select(DATAFIELD_NAME)
data3D7 = hdf7.select(DATAFIELD_NAME)
data3D8 = hdf8.select(DATAFIELD_NAME)

scale_factor = getattr(data3D1, "scale_factor")
add_offset = getattr(data3D1, "add_offset")



valid_range = getattr(data3D1, "valid_range")

#print "valid_range: " + str(valid_range)

#print "scale_factor: " + str(scale_factor)

data1 = data3D1[:,:]
data2 = data3D2[:,:]
data3 = data3D3[:,:]
data4 = data3D4[:,:]
data5 = data3D5[:,:]
data6 = data3D6[:,:]
data7 = data3D7[:,:]
data8 = data3D8[:,:]

#print data1.shape

data=np.concatenate( [data1,data2,data3,data4,data5,data6,data7,data8], axis=0)

#print "data sample: " + str(data[100])
time = hdf1.select("Scan_Start_Time")[0,0]
#print time

def scale(x):
    return scale_factor * x

def offset(x):
    return x - add_offset



if add_offset != 0:
    #print "offest: " + str(add_offset)
    offset_func = np.vectorize(offset)
    data = offset_func(data)

#print "offest: " + str(add_offset)

if scale_factor != 1:

    scale_func = np.vectorize(scale)

#scale the value by scale factor
    data = scale_func(data)
     




#==============================================================================
# READ index file
#==============================================================================
nc_f = '/Users/sevakm/Documents/index-airs.aqua_modis.aqua-v1.0-2013.03.02.1500.nc4'  # Your filename
nc_fid = Dataset(nc_f, 'r') 

col_pt = nc_fid.variables['Column_Point'][:]
row_pt = nc_fid.variables['Row_Point'][:]



#print str(col_pt[0])
print "\n"

#print str(row_pt[0])

#print 'Col: ' + str(col_pt)
#print '\n\n'
#print 'Row: ' + str(row_pt)

#bad_arry = []
#count = 0
#for i in range(675):
#    for j in range(90):
#        if col_pt[i][j] <0:
#            count = count +1
#            bad_arry.append((i, j))
#
#print "bad values: " + str(count)
#print bad_arry
#print "column : " + str(row_pt[476])

#print row_pt


path = '/Users/sevakm/Documents/AIRS_To_Modis/' + DATAFIELD_NAME + '.npy'
index_path = '/Users/sevakm/Documents/AIRS_To_Modis/index_summary.npy'
index_arr =[]
scan_line = 0

#array containing all cluster chunks
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
      
        granule = ''
        
        if a <=134:
            granule =151
        elif a > 134 and a <=269:
            granule = 152
        elif a >269 and a <=404:
            granule =153
        elif a >404 and a <= 539:
            granule = 154
        elif a >539 and a <=674:
            granule = 155
        
        
        arr =[]
        arr.append(scan_line)
        arr.append(b)
        arr.append(granule)
        
        index_arr.append(arr)
        
    scan_line = scan_line +1
    if scan_line == 135:
        scan_line =0
        

np_arr = np.array(array)
np.save(path, np_arr)

#same index file
#np.save(index_path, np.array(index_arr))
    
#        print str(row_pt[a][b]) + " : "+ str(col_pt[a][b])



#print "read....."
##
#load= np.array(np.load(path))




