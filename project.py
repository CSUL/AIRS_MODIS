# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import matplotlib.pyplot as plt
import numpy as np
from pyhdf.SD import SD, SDC
import decimal

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


DATAFIELD_NAME="cloud_top_pressure_1km"

"Cloud_Optical_Thickness"
"Cloud_Effective_Radius"
"cloud_top_pressure_1km"


data3D1 = hdf1.select(DATAFIELD_NAME)
data3D2 = hdf2.select(DATAFIELD_NAME)
data3D3 = hdf3.select(DATAFIELD_NAME)
data3D4 = hdf4.select(DATAFIELD_NAME)

data3D5 = hdf5.select(DATAFIELD_NAME)
data3D6 = hdf6.select(DATAFIELD_NAME)
data3D7 = hdf7.select(DATAFIELD_NAME)
data3D8 = hdf8.select(DATAFIELD_NAME)

scale_factor = getattr(data3D1, "scale_factor")
print "Scale factor: " + str(scale_factor)

#print "HI: " + str(data3D1[:,].shape)
#
data1 = data3D1[:,316:1038]
data2 = data3D2[:,316:1038]
data3 = data3D3[:,316:1038]
data4 = data3D4[:,316:1038]
data5 = data3D5[:,316:1038]
data6 = data3D6[:,316:1038]
data7 = data3D7[:,316:1038]
data8 = data3D8[:,316:1038]


data = np.concatenate( [data1,data2,data3,data4,data5,data6,data7,data8], axis=0)

print "shape of data: " + str(data.shape)

#print hdf.info()

#print hdf.attributes()

print "\n\n"
#==============================================================================
# CLOUD TOP PRESSURE
#==============================================================================

## # Read dataset.
#DATAFIELD_NAME='Cloud_Optical_Thickness'


def scale(x):
    return scale_factor * x

def log(x):
    return np.log(1000/x) * 7
#
#scale_func = np.vectorize(scale)
#
##scale the value by scale factor
#data = scale_func(data)
#mask = (data >=0) & (data <= 1000)
#data = data[mask]
#
#print data
#
#
#log_func = np.vectorize(log)
##convert pressure to height
#data = log_func(data)
#
##for x in data:
##    print x
#
#
#
#fig0 = plt.figure()
#ax0 = fig0.add_subplot(1, 1, 1)
#n, bins, patches = ax0.hist(data, 40, normed=1, facecolor='green')
#plt.xlabel("Cloud height in KM")
# 
##plt.axis([30, 50, 0, 0.7])
#plt.grid(True)
#
#
##==============================================================================
## CLOUD OPTICAL THICKNESS
##==============================================================================
#
#DATAFIELD_NAME='Cloud_Optical_Thickness'
#data3D = hdf.select(DATAFIELD_NAME)

#print data3D.attributes()

#data = data3D[:,:]
#scale_factor = getattr(data3D, "scale_factor")
if scale_factor != 1:
    scale_func = np.vectorize(scale)
    #scale the value by scale factor
#    data1 = scale_func(data1)
#    data2 = scale_func(data2)
#    data3 = scale_func(data3)
#    data4 = scale_func(data4)
#    
#    data5 = scale_func(data5)
#    data6 = scale_func(data6)
#    data7 = scale_func(data7)
#    data8 = scale_func(data8)
    data = scale_func(data)


################PRESSURE
#log_func = np.vectorize(log)
mask = (data >=0) & (data <= 1000)
data = data[mask]
#data = log_func(data)
#########################

################THICKNESS
#mask = (data >=0) & (data <= 100)
#data = data[mask]
#########################

################Cloud_Effective_Radius
#mask = (data >=0) & (data <= 90)
#data = data[mask]
#########################






mean = np.mean(data)
std = np.std(data)

print "shape of data: " + str(data.shape)


print "Mean: " + str(mean) + " |  Std: " + str(std) 

#mask = (data1 >=0) & (data1 <= 1000)
#data1 = data1[mask]
#data1 = log_func(data1)
#
#mask = (data2 >=0) & (data2 <= 1000)
#data2 = data2[mask]
#data2 = log_func(data2)
#
#mask = (data3 >=0) & (data3 <= 1000)
#data3 = data3[mask]
#data3 = log_func(data3)
#
#mask = (data4 >=0) & (data4 <= 1000)
#data4 = data4[mask]
#data4 = log_func(data4)
#
#mask = (data5 >=0) & (data5 <= 1000)
#data5 = data5[mask]
#data5 = log_func(data5)
#
#mask = (data6 >=0) & (data6 <= 1000)
#data6 = data6[mask]
#data6 = log_func(data6)
#
#mask = (data7 >=0) & (data7 <= 1000)
#data7 = data7[mask]
#data7 = log_func(data7)
#
#mask = (data8 >=0) & (data8 <= 1000)
#data8 = data8[mask]
#data8 = log_func(data8)


#fig1 = plt.figure()
#ax1 = fig1.add_subplot(1, 1, 1)
#ax1.hist(data1, 200, normed=1, facecolor='b')
#plt.xlabel(DATAFIELD_NAME)
#plt.title("Granule 1: 1500 |   MEAN: " + str(round(np.mean(data1), 2)) + "  |  STD: " + str(round(np.std(data1), 2)))
#plt.axis([-1, 16, 0, 3.0])
#plt.grid(True)
#
#fig2 = plt.figure()
#ax2 = fig2.add_subplot(1, 1, 1)
#ax2.hist(data2, 200, normed=1, facecolor='b')
#plt.xlabel(DATAFIELD_NAME)
#plt.title("Granule 2: 1505 |   MEAN: " + str(round(np.mean(data2), 2)) + "  |  STD: " + str(round(np.std(data2), 2)))
##plt.axis([-1, 40, 0, 0.25])
#plt.grid(True)
#
#fig3 = plt.figure()
#ax3 = fig3.add_subplot(1, 1, 1)
#ax3.hist(data3, 200, normed=1, facecolor='b')
#plt.xlabel(DATAFIELD_NAME)
#plt.title("Granule 3: 1510 |   MEAN: " + str(round(np.mean(data3), 2))  + "  |  STD: " + str(round(np.std(data3), 2)))
##plt.axis([-1, 40, 0, 0.25])
#plt.grid(True)
#
#fig4 = plt.figure()
#ax4 = fig4.add_subplot(1, 1, 1)
#ax4.hist(data4, 200, normed=1, facecolor='b')
#plt.xlabel(DATAFIELD_NAME)
#plt.title("Granule 4: 1515 |   MEAN: " + str(round(np.mean(data4), 2)) + "  |  STD: " + str(round(np.std(data4), 2)))
##plt.axis([-1, 40, 0, 0.25])
#plt.grid(True)
#
#fig5 = plt.figure()
#ax5 = fig5.add_subplot(1, 1, 1)
#ax5.hist(data5, 200, normed=1, facecolor='b')
#plt.xlabel(DATAFIELD_NAME)
#plt.title("Granule 5: 1520 |   MEAN: " + str(round(np.mean(data5), 2))  + "  |  STD: " + str(round(np.std(data5), 2)))
##plt.axis([-1, 40, 0, 0.25])
#plt.grid(True)
#
#fig6 = plt.figure()
#ax6 = fig6.add_subplot(1, 1, 1)
#ax6.hist(data6, 200, normed=1, facecolor='b')
#plt.xlabel(DATAFIELD_NAME)
#plt.title("Granule 6: 1525 |   MEAN: " + str(round(np.mean(data6), 2))  + "  |  STD: " + str(round(np.std(data6), 2)))
##plt.axis([-1, 40, 0, 0.25])
#plt.grid(True)
#
#fig7 = plt.figure()
#ax7 = fig7.add_subplot(1, 1, 1)
#ax7.hist(data7, 200, normed=1, facecolor='b')
#plt.xlabel(DATAFIELD_NAME)
#plt.title("Granule 7: 1530 |   MEAN: " + str(round(np.mean(data7), 2))  + "  |  STD: " + str(round(np.std(data7), 2)))
##plt.axis([-1, 40, 0, 0.25])
#plt.grid(True)
#
#fig8 = plt.figure()
#ax8 = fig8.add_subplot(1, 1, 1)
#ax8.hist(data8, 200, normed=1, facecolor='b')
#plt.xlabel(DATAFIELD_NAME)
#plt.title("Granule 8: 1535 |   MEAN: " + str(round(np.mean(data8), 2))  + "  |  STD: " + str(round(np.std(data8), 2)))
##plt.axis([-1, 40, 0, 0.25])
#plt.grid(True)



##==============================================================================
## Cloud Phase OpticalProperties
##==============================================================================
#
#DATAFIELD_NAME='Cloud_Phase_Optical_Properties'
#data3D = hdf.select(DATAFIELD_NAME)
#
#data = data3D[:,:]
#scale_factor = getattr(data3D, "scale_factor")
#
#if scale_factor != 1:
#    scale_func = np.vectorize(scale)
#    #
#    #scale the value by scale factor
#    data = scale_func(data)
#
##print data
#
#mask = (data ==0) |(data ==1) | (data == 2) | (data == 3) | (data == 4)
#data = data[mask]
#
#
#fig2 = plt.figure()
#ax2 = fig2.add_subplot(1, 1, 1)
#n, bins, patches = ax2.hist(data, normed=1, facecolor='b')
#
#plt.xlabel("Cloud Phase Optical Properties")
##plt.axis([-0.5, 4.0, 0, 1.7])
#plt.grid(True)
#
#
##==============================================================================
## CLoud Effective Radius
##==============================================================================
#DATAFIELD_NAME='Cloud_Effective_Radius'
#data3D = hdf.select(DATAFIELD_NAME)
#
#
#data = data3D[:,:]
#scale_factor = getattr(data3D, "scale_factor")
#
#if scale_factor != 1:
#    scale_func = np.vectorize(scale)
#    #
#    #scale the value by scale factor
#    data = scale_func(data)
#
##print data
#
#mask = (data >0) & (data <=90)
#data = data[mask]
#
#
#fig3 = plt.figure()
#ax3 = fig3.add_subplot(1, 1, 1)
#n, bins, patches = ax3.hist(data, normed=1, facecolor='c')
#
#plt.xlabel("Cloud Effective Radius")
##plt.axis([-0.5, 4.0, 0, 1.7])
#plt.grid(True)
## Read geolocation dataset.
##==============================================================================
## lat = hdf.select('Latitude')
## latitude = lat[:,:]
## lon = hdf.select('Longitude')
## longitude = lon[:,:]
##==============================================================================
#
##print latitude[0]
##print latitude[0][135]
##
##print longitude[0]
##print longitude[0][135]
##
##print "-----------\n\n"
##print latitude[405]
##print latitude[405][135]
##
##print longitude[405]
##print longitude[405][135]
#
##zipped0 = zip(latitude[0], longitude[0])
##
##zipped1 = zip(latitude[405], longitude[405])
#
#
##print (zipped)
##for x in zipped1:
##    print str(x[0]) + "," + str(x[1])