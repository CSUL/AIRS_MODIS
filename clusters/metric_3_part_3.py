# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt




metric = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/metric3_without_clear.csv')
indices = np.load('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/airs_to_modis_cluster_index_temperature_10.npy')
data = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/data2.csv')


values = []
mean_vals =[]

zero_stds =[]

for take, row in enumerate(indices):
    numerator = 0
    denominator =0
    for metric_index, data_index in enumerate(range(1, 31, 3)):
        temperature = metric.iloc[row][metric_index + 2]
#        print "temP: " + str(temperature) + " | row: " + str(row)
#    print "-----------"
        if temperature >0:
            fraction =data.iloc[row].iloc[data_index]
            cur_num = fraction* temperature
            numerator = numerator + cur_num
            denominator = denominator + fraction
    
    mean = numerator/denominator
    mean_vals.append(mean)
    if np.isnan(mean):
        print "NAN: " + str(take)
#    print "mean: " + str(mean)
    
    numerator = 0

    for metric_index, data_index in enumerate(range(1, 31, 3)):
        temperature = metric.iloc[row][metric_index + 2]
        if temperature >0:
#            print "temp:" + str(temperature) + " |row:  " + str(row) + " mn: " + str(mean)
            fraction =data.iloc[row].iloc[data_index]
            cur_num = fraction* math.pow((temperature-mean), 2)
            numerator = numerator + cur_num
            
#    print "numerator/denominator: " + str(numerator)
    std = math.sqrt(numerator/denominator)
#    if std ==0:
#        print "num: " + str(numerator) + " denom: " + str(denominator) + " row | " + str(row)
    values.append(std)
    
    
    if std ==0:
        zero_stds.append(row)
        
    print take


np.save('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/metric_3_ZERO_std.npy', np.array(zero_stds))

#np.save('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/metric_3_std.npy', np.array(values))
#np.save('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/metric_3_mean.npy', np.array(mean_vals))


#------------         
#arr = np.load('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/metric_3_std.npy')
#means = np.load('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/metric_3_mean.npy')
#
#print np.min(means)
#print np.max(means)
#
#print arr[np.isnan(arr)].shape
#
#print "arr: " + str(arr.shape)
#
#for x in range(10):
#    print arr[x]
##
##print np.min(arr)
##print np.max(arr)
##
#
#
##indices = np.load('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/airs_to_modis_cluster_index.npy')
#


#path = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/EV_1KM_Emissive.npy'
#bright = np.load(path)
#
#
##bright = np.take(bright, indices)
#
#
#
#bright_arr = []
#
#count = 0
#for index, x in enumerate(indices):
#    std = np.std(bright[x])
#    
#    if not np.all(bright[x] ==-1):
#        bright_arr.append(std)
#        
#        
#print "bright_arr: " + str(len(bright_arr))



#==============================================================================
# 
#==============================================================================
#plt.figure()
#plt.plot(bright_arr)
##n, b ,p =plt.hist(bright_arr, normed=1, 
##                  facecolor='green',bins =1000,
##                  cumulative=False)
#
#
#
#plt.figure()
#n, b ,p =plt.hist(bright_arr, normed=1, 
#                  bins =1000,
#                  histtype = 'step',
##                  range =[0,1],
#                  cumulative=True)
#plt.title("Cumulutive distribution")
#plt.show()
#
#plt.figure()
#plt.plot(arr)
##n, b ,p =plt.hist(arr, normed=1, 
##                  facecolor='green',
##                  cumulative=False)
#
#
#
#plt.figure(figsize =(10, 8))
#n, b ,p =plt.hist(arr, normed=1, 
#                  bins =1000,
#                  histtype = 'step',
##                  range =[0,1],
#                  cumulative=True)
#plt.title("Cumulutive distribution of Cloud-top Temperature STD")
#plt.xlabel("STD")
#plt.show()
        

#plt.figure(figsize =(10, 8))
#p1 = plt.plot(arr)
#p2 = plt.plot(bright_arr, alpha=.5, color = 'r')
#plt.legend( (p1[0], p2[0]), ('Cloud top temperature STD', 'Brightness temperature STD') )
#plt.show()

#plt.figure(figsize = (10, 8))
#plt.scatter(arr, bright_arr)
#plt.xlabel("Cloud Top Temperature STD")
#plt.ylabel("Brightness Temperature STD")

    


    
    
    


