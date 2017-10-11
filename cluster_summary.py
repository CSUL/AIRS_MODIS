import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/data.csv')


cols = ['num_cluster']
data_frame = pd.DataFrame([], columns = cols)

percent = np.zeros(10)
for row in range(60750):
#    cluster_count =0
#    df_array =[]
    
    missing = df.iloc[row].iloc[41]
    good = 741 - missing
    
    
    
    for index, x in enumerate(range(1, 41, 4)):
        fraction = df.iloc[row].iloc[x]
#        if good !=0 and fraction >= (0.1*good):
        if good !=0 and fraction >= 1:
#            percent[index] = percent[index] + fraction/good
            percent[index] = percent[index] + 1
            
    print str(row) + "/60750"
print percent 
#np.save('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/percent_count_all.npy', np.array(percent))
#np.save('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/percent.npy', np.array(percent))

#arr = np.load('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/percent.npy')
#arr2 = np.load('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/percent_count.npy')
#
#
#
#
#for x in arr:
#    print ( x* 100)/60750
#else:
#    print
##
#print "-------------------"
#for x in arr2:
#    print x
#else: 
#    print 
#
##
#print "-------------------"
#df = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/Greater_10.csv')
#group = df.groupby('num_cluster')
#
#
#obj= group.count()
#
#print obj

 