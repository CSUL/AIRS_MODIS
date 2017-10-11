#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:56:30 2017

@author: sevakm
"""



from haversine import haversine
import numpy as np
from pyhdf.SD import SD, SDC
import pandas as pd
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/


# Open file.
FILE_NAME1 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD03/MYD03.A2013061.1500.005.2013062152057.hdf'
FILE_NAME2 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD03/MYD03.A2013061.1505.005.2013062151919.hdf'
FILE_NAME3 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD03/MYD03.A2013061.1510.005.2013062151708.hdf'
FILE_NAME4 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD03/MYD03.A2013061.1515.005.2013062151754.hdf'
FILE_NAME5 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD03/MYD03.A2013061.1520.005.2013062152049.hdf'
FILE_NAME6 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD03/MYD03.A2013061.1525.005.2013062151908.hdf'
FILE_NAME7 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD03/MYD03.A2013061.1530.005.2013062151646.hdf'
FILE_NAME8 = '/Users/sevakm/Documents/AIRS_To_Modis/MYD03/MYD03.A2013061.1535.005.2013062151709.hdf'

hdf1 = SD(FILE_NAME1, SDC.READ)
hdf2 = SD(FILE_NAME2, SDC.READ)
hdf3 = SD(FILE_NAME3, SDC.READ)
hdf4 = SD(FILE_NAME4, SDC.READ)

hdf5 = SD(FILE_NAME5, SDC.READ)
hdf6 = SD(FILE_NAME6, SDC.READ)
hdf7 = SD(FILE_NAME7, SDC.READ)
hdf8 = SD(FILE_NAME8, SDC.READ)


#print hdf1.attributes()



#print hdf.attributes()

print "\n\n"
#==============================================================================
# CLOUD TOP PRESSURE
#==============================================================================

## # Read dataset.
DATAFIELD_NAME='Longitude'
#
data1 = hdf1.select(DATAFIELD_NAME)[:,:]
data2 = hdf2.select(DATAFIELD_NAME)[:,:]
data3 = hdf3.select(DATAFIELD_NAME)[:,:]
data4 = hdf4.select(DATAFIELD_NAME)[:,:]

data5 = hdf5.select(DATAFIELD_NAME)[:,:]
data6 = hdf6.select(DATAFIELD_NAME)[:,:]
data7 = hdf7.select(DATAFIELD_NAME)[:,:]
data8 = hdf8.select(DATAFIELD_NAME)[:,:]
#scale_factor = getattr(data3D1, "scale_factor")

#print "SCALE: " + str(scale_factor)
#


#print data1.shape

lon_data=np.concatenate( [data1,data2,data3,data4,data5,data6,data7,data8], axis=0)

DATAFIELD_NAME='Latitude'
#
data1 = hdf1.select(DATAFIELD_NAME)[:,:]
data2 = hdf2.select(DATAFIELD_NAME)[:,:]
data3 = hdf3.select(DATAFIELD_NAME)[:,:]
data4 = hdf4.select(DATAFIELD_NAME)[:,:]

data5 = hdf5.select(DATAFIELD_NAME)[:,:]
data6 = hdf6.select(DATAFIELD_NAME)[:,:]
data7 = hdf7.select(DATAFIELD_NAME)[:,:]
data8 = hdf8.select(DATAFIELD_NAME)[:,:]

#scale_factor = getattr(data3D1, "scale_factor")

#print "SCALE: " + str(scale_factor)
#


#print data1.shape

lat_data=np.concatenate( [data1,data2,data3,data4,data5,data6,data7,data8], axis=0)

#print hdf1.attributes()
#time = hdf1.select("scan_start_time")[:,:]
#print time

print lat_data.shape
print lon_data.shape

#print hdf1.datasets()
#print da
#print "Shape of Data: " + str(data.shape) + "\n"
#
#def scale(x):
#    return scale_factor * x
#
#if scale_factor != 1:
#
#    scale_func = np.vectorize(scale)
#
##scale the value by scale factor
#    data = scale_func(data)
#
##==============================================================================
## READ index file
##==============================================================================
nc_f = '/Users/sevakm/Documents/index-airs.aqua_modis.aqua-v1.0-2013.03.02.1500.nc4'  # Your filename
nc_fid = Dataset(nc_f, 'r') 

col_pt = nc_fid.variables['Column_Point'][:]
row_pt = nc_fid.variables['Row_Point'][:]



#print "point: " + str(data[row][col])


#path = '/Users/sevakm/Documents/AIRS_To_Modis/MYD03/' + DATAFIELD_NAME + '.npy'
#
arrau = []
string =""

#print lon_data[0][677]
#print lat_data[0][677]
#
#print lon_data[16239][677]
#print lat_data[16239][677]



for a in range(16230):

#    col = col_pt[a][677]
#    row = row_pt[a][677]
        
#    if(col == -9999 or row == -9999):
        ""
#        array.append(np.zeros((19, 39))) 
#            print "len of zeros: " + str(np.zeros((19, 39)).shape)
#    else:
#        i0 = col -20
#        i1 = col + 19
#            
#        j0 = row -10
#        j1 = row + 9
#        patch = data[j0:j1, i0:i1]
#            print "patch shape: " + str(np.array(patch).shape)
#            print patch
        string = string + str(lon_data[a][676]) + "," + str(lat_data[a][676]) + "\n"

#print string
text_file = open("/Users/sevakm/Documents/AIRS_To_Modis/MYD03/MODIS_MID_COL.txt", "w") 
text_file.write(string)
#np_arr = np.array(array)
#print "Shape of patches: " + str(array)
#np.savetxt("/Users/sevakm/Documents/AIRS_To_Modis/MYD03/MODIS_MID_COL.out", np_arr, delimiter='\n')
#    
##        print str(row_pt[a][b]) + " : "+ str(col_pt[a][b])
#
#
#
##print "read....."
###
##load= np.array(np.load(path))
#
#
#
#
#
#
#
#
##x1= np.zeros([1354,2030])
##x2= np.zeros([1354,2030])
##x3= np.zeros([1354,2030])
##x4= np.zeros([1354,2030])
##x5= np.zeros([1354,2040])
##x6= np.zeros([1354,2030])
##x7= np.zeros([1354,2030])
##x8= np.zeros([1354,2030])
##
##x=np.concatenate( [x1,x2,x3,x4,x5,x6,x7,x8], axis=1)
##print  x1.shape
##print  x2.shape
##print  x3.shape
##print  x4.shape
##print  x5.shape
##print  x6.shape
##print  x7.shape
##print  x8.shape
##print  x.shape
#
#
#
#
##scale_factor = getattr(data3D, "scale_factor")
###print "scale factor : " + str(scale_factor)
##
##data = data3D[:,:]
##
##i0 = 1280 -20
##i1 = 1280 +19
##
##j0 = 2192 -2030 -10
##j1 = 2192 -2030 + 9
##
##res = data3D[i0:i1, j0:j1]
##
##print res.shape