#!/opt/python/anaconda-2.4/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 19:10:40 2017

@author: sevakm
"""
from scipy.cluster.vq import kmeans2
import numpy as np
#import matplotlib.pyplot as plt
#from sklearn.cluster import KMeans
#from matplotlib.colors import LogNorm
#from mpl_toolkits.mplot3d import Axes3D
import collections
import pandas as pd




#path = '/Users/sevakm/Documents/AIRS_To_Modis/normalized/' + 'cloud_top_pressure_1km_NORMALIZED.npy'
path = '/Users/sevakm/Documents/AIRS_To_Modis/' + 'cloud_top_pressure_1km.npy'
path2 = '/Users/sevakm/Documents/AIRS_To_Modis/' + 'Cloud_Optical_Thickness.npy'
path3 = '/Users/sevakm/Documents/AIRS_To_Modis/' + 'Cloud_Effective_Radius.npy'

#path = '/Users/sevakm/Documents/AIRS_To_Modis/normalized/' + 'cloud_top_pressure_1km_NORMALIZED.npy'
#path2 = '/Users/sevakm/Documents/AIRS_To_Modis/normalized/' + 'Cloud_Optical_Thickness_NORMALIZED.npy'
#path3 = '/Users/sevakm/Documents/AIRS_To_Modis/normalized/' + 'Cloud_Effective_Radius_NORMALIZED.npy'



pressure = np.load(path)
JOB_SIZE, r, c = pressure.shape
pressure_data = pressure


r, row, col = pressure_data.shape
pressure_data = pressure_data.reshape(r * row, col)

thickness = np.load(path2)
thickness_data = thickness
r, row, col = thickness_data.shape
thickness_data = thickness_data.reshape(r * row, col)


radius = np.load(path3)
radius_data = radius
r, row, col = radius_data.shape
radius_data = radius_data.reshape(r * row, col)

#print "shape: " + str(radius_data.shape)


row, col = pressure_data.shape

p_col = pressure_data.reshape(row * col, 1) 
t_col = thickness_data.reshape(row * col, 1)
r_col = radius_data.reshape(row * col, 1)

data = np.concatenate((p_col, t_col, r_col), axis =1)

print "data shape b4: " + str(data.shape)
#print "shape: " + str(data.shape)

#remove bad data rows
#data = data[data[:,0] > 0]
data =data[np.logical_and(data[:,0] >= 0, data[:,1] >= 0, data[:,2] >= 0)]

print "data shape after: " + str(data.shape)

#print "shape: " + str(data.shape)
#####################

#find average radius for range(50 - 440)
row_temp = data[np.logical_and(data[:,0] >= 50, data[:,0] < 440)]
row_cirrus_mean = np.mean(row_temp.T[2])
#print "row_cirrus_mean: " + str(row_cirrus_mean)
##########################3

#find average radius for range(440 - 680)
row_temp = data[np.logical_and(data[:,0] >= 440, data[:,0] < 680)]
row_altocumulus_mean = np.mean(row_temp.T[2])

#print "row_altocumulus_mean: " + str(row_altocumulus_mean)
##########################3

#find average radius for range(440 - 680)
row_temp = data[np.logical_and(data[:,0] >= 680, data[:,0] <=1000)]
#print "GOOD STUFF: " + str(row_temp.shape)
row_cumulus_mean = np.mean(row_temp.T[2])

#print "row_cumulus_mean: " + str(row_cumulus_mean)
##########################3



centers = np.array([
                    [195, 1.3, row_cirrus_mean],     #0
                    [195, 9.4, row_cirrus_mean],     #1
                    [195, 60, row_cirrus_mean],      #2
                    [560, 1.3, row_altocumulus_mean],#3
                    [560, 9.4, row_altocumulus_mean],#4
                    [560, 60, row_altocumulus_mean], #5
                    [840, 1.3, row_cumulus_mean],    #6
                    [840, 9.4, row_cumulus_mean],    #7
                    [840, 60, row_cumulus_mean],     #8
                    [0, 0, 0]                        #9
                    ])
    
#print "center shape: " + str(centers.shape)

#test patch one

#==============================================================================
#DATAFRAME TO HOLD ALL CLUSTER INFO
cols = ['f', 'p', 't', 'r', 
        'f', 'p', 't', 'r', 
        'f', 'p', 't', 'r', 
        'f', 'p', 't', 'r',
        'f', 'p', 't', 'r',
        'f', 'p', 't', 'r', 
        'f', 'p', 't', 'r',
        'f', 'p', 't', 'r',
        'f', 'p', 't', 'r',
        'f', 'p', 't', 'r',
        'm']
data_frame = pd.DataFrame([], columns = cols)
#print "DATAFRAME: " + str(data_frame)
#==============================================================================
for round in range(JOB_SIZE):
    pressure_data = pressure[round]
    row, col = pressure_data.shape
    pressure_data = pressure_data.reshape(row* col, 1)
    
    thickness_data = thickness[round]
    row, col = thickness_data.shape
    thickness_data = thickness_data.reshape(row* col, 1)
    
    radius_data = radius[round]
    row, col = radius_data.shape
    radius_data = radius_data.reshape(row* col, 1)
    
    bad_val_array =[]
    
    #Clean bad data 
    for index, x in enumerate(pressure_data):
        for y in x:
            if y <0 or y >1000:
                if not index in bad_val_array:
                    bad_val_array.append(index)
                    continue
    for index, x in enumerate(thickness_data):
        for y in x:
            if y <0 or y >100:
                if not index in bad_val_array:
                    bad_val_array.append(index)
                    continue
    
    for index, x in enumerate(radius_data):
        for y in x:
            if y <0 or y >90:
                if not index in bad_val_array:
                    bad_val_array.append(index)
                    continue
    
    
#    print len(bad_val_array)
    
    data = np.concatenate((pressure_data, thickness_data, radius_data), axis =1)
    data = np.delete(data, bad_val_array, axis = 0)
    

    
#    fig2 = plt.figure()
#    ax1 = fig2.add_subplot(1, 1, 1)
#    ax1.hist(pressure_data, 200, normed=1, facecolor='b')
#    #plt.axis([-1, 16, 0, 3.0])
#    plt.grid(True)
#    plt.show()
    
    km = '' #placeholder for to hold the result of k-means
    
    if len(data) == 0:
        zeros = np.zeros(40).tolist()
        zeros.append(len(bad_val_array))
        data_frame.loc[len(data_frame)] = zeros
#        data_frame.loc[len(data_frame)] = len(bad_val_array)
    else: 
        km = kmeans2(data, centers)
        
        
        
        df_array=[]
        
        counter=collections.Counter(km[1])
        
        for index, x in enumerate(km[0]):
    #        print "index: " + str(index)
            if index in counter:
    #            print "index: " + str(counter[index])
                df_array.append(counter[index])
            else:
                df_array.append(0)
                
            df_array = df_array + x.tolist()
            
        
        df_array.append(len(bad_val_array))
        data_frame.loc[len(data_frame)]= df_array
    #    print data_frame
#    print "print frame: " 
#    print data_frame
        
    print str(round) + "/" + str(JOB_SIZE)
    
data_frame.to_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/data_tl2.csv')

        
    
##    counter=collections.Counter(km[1])
###    
##    print counter
#    
##    print "\n\n"
##    for x in km[1]:
##        print x,
##    else: 
##        print 
#        
#    
##    classes = {'Cirrus': 0, 'Cirrostratus': 0, 'Deep Convection' : 0,
##               'Altocumulus': 0, 'Altostratus': 0, 'Nimbostratus' : 0,
##               'Cumulus': 0, 'Stratucumulus': 0, 'Stratus': 0}
##    
##    for x in km[0]:
##        if x[0] >= 50 and x[0] <440 and x[1] >=0 and x[1] <3.6:
##            classes['Cirrus'] = classes['Cirrus'] +1
##        elif x[0] >= 50 and x[0] <440 and x[1] >=3.6 and x[1] <23:
##            classes['Cirrostratus'] = classes['Cirrostratus'] +1
##        elif x[0] >= 50 and x[0] <440 and x[1] >=23 and x[1] <=379:
##            classes['Deep Convection'] = classes['Deep Convection'] +1
##        
##        elif x[0] >= 440 and x[0] <680 and x[1] >=0 and x[1] <3.6:
##            classes['Altocumulus'] = classes['Altocumulus'] +1
##        elif x[0] >= 440 and x[0] <680 and x[1] >=3.6 and x[1] <23:
##            classes['Altostratus'] = classes['Altostratus'] +1
##        elif x[0] >= 440 and x[0] <680 and x[1] >=23 and x[1] <=379:
##            classes['Nimbostratus'] = classes['Nimbostratus'] +1
##            
##        elif x[0] >= 680 and x[0] <=1000 and x[1] >=0 and x[1] <3.6:
##            classes['Cumulus'] = classes['Cumulus'] +1
##        elif x[0] >= 680 and x[0] <=1000 and x[1] >=3.6 and x[1] <23:
##            classes['Stratucumulus'] = classes['Stratucumulus'] +1  
##        elif x[0] >= 680 and x[0] <=1000 and x[1] >=23 and x[1] <=379:
##            classes['Stratus'] = classes['Stratus'] +1
##            
##    print classes
#    
##    km = KMeans(n_clusters=10, random_state=0, 
##                init = centers, max_iter =1000, algorithm = 'auto').fit(data)
##    km = KMeans(n_clusters=10, random_state=1, max_iter =1000).fit(data)
##    
##    #
##    #
##    labels = km.labels_
##    
##    cluster_centers_ = km.cluster_centers_
##    
##    
##    #PLOT
##    fig = plt.figure(1, figsize=(4, 3))
##    plt.clf()
##    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=120)
##    
##    plt.cla()
##    
##    colors =['b', 'g', 'r', 'c', 'm', 'y', 'b', '#f442c8', '#efc700', '#3e874b']
##    ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=km.astype(np.float))
##    
##    ax.w_xaxis.set_ticklabels([])
##    ax.w_yaxis.set_ticklabels([])
##    ax.w_zaxis.set_ticklabels([])
##    ax.set_xlabel('cloud_top_pressure_1km')
##    ax.set_ylabel('Cloud_Optical_Thickness')
##    ax.set_zlabel('Cloud_Effective_Radius')
##    plt.show()
##    
##    
##    ##
##    #print "\nlabels:\n" + str(labels)
##    
##    counter=collections.Counter(labels)
##    
##    #counter['Cirrus'] = counter.pop(1)
##    #counter['Cirrostratus'] = counter.pop(2)
##    #counter['Deep Convection'] = counter.pop(3)
##    #
##    #counter['Altocumulus'] = counter.pop(4)
##    #counter['Altostratus'] = counter.pop(5)
##    #counter['Nimbostratus'] = counter.pop(6)
##    #
##    #counter['Cumulus'] = counter.pop(7)
##    #counter['Stratucumulus'] = counter.pop(8)
##    #counter['Stratus'] = counter.pop(9)
##    #
##    #counter['Clear Sky'] = counter.pop(10)
##    
##    
##    print counter
##    #print "\ncluster centers:\n" + str(cluster_centers_[7])
##    for index, x in enumerate(cluster_centers_):
##        print str(index) + ": "  + str(x)
##    
##
##
##
