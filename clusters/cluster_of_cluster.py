# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/data2.csv')





#cols = ['cloud_1', 'cloud_2']
#data_frame = pd.DataFrame([], columns = cols)
#
##cnt =0
cloud_types = np.zeros(100).reshape((10, 10))

#for row in range(60750):
#    cluster_count =0
#    df_array =[]
#    
#    missing = df.iloc[row]['m']
#    good = 741 - missing
#
#    
#    clouds =np.zeros(10)
#
#    for index, x in enumerate(range(1, 31, 3)):
#        fraction =df.iloc[row].iloc[x]
#        if good !=0 and fraction >= (0.1*good):
#            cluster_count = cluster_count+1
#            clouds[index] = 1
#            
#    cloud_types[cluster_count -1] = np.add(cloud_types[cluster_count -1], clouds)
##    print clouds
##    print cluster_count
#    
##            clouds[index] = 1
#    
##    if cluster_count ==1:
##        for index, x in enumerate(clouds):
##            if x ==1:
##                cloud_types[index] = cloud_types[index] +1
#                
#   
#    
#    print str(row) + "/60750"
##    print cloud_types
#    

path = '/Users/sevakm/Documents/AIRS_To_Modis/cluster_of_cluster/cloud_types.npy'
#np.save(path, np.array(cloud_types))
#print cloud_types

arr = np.load(path)
#

for index, cluster in enumerate(arr):
    if np.sum(cluster) !=0:
        plt.figure()
        y_pos =np.arange(len(cluster))
        plt.bar(y_pos, cluster)
        
        plt.xticks(y_pos, np.arange(10))
        plt.title("Cluster " + str(index +1))
        plt.show()
        
        print cluster.astype(int)



#clear= df.loc[(df['f10'] >=74)]
#print clear[(clear['f1'] >=74)].shape
#for x in range(1):
#    print clear[(clear['f1'] >=1)]
  
#data_frame.to_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/clouds_2_2.csv')


 # -*- coding: utf-8 -*-

