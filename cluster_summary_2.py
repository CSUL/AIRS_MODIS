import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/data2.csv')

print len(df[df['m'] ==741])

#arr = np.array([  5226.94586017,   5696.707799,     1131.19807018,   631.1949616,
#    933.2336812,     207.59471209,   6415.96665029,   6908.01741709,
#   1351.9509104,  28723.59031776])
#
#for x in arr:
#    print (x/60750) * 100


#
#cols = ['num_cluster']
#data_frame = pd.DataFrame([], columns = cols)
#
#percent = np.zeros(10)
#for row in range(60750):
##    cluster_count =0
##    df_array =[]
#    
#    missing = df.iloc[row].iloc[31]
#    good = 741 - missing
#    
#    
#    
#    for index, x in enumerate(range(1, 31, 3)):
#        fraction = df.iloc[row].iloc[x]
#        if good !=0 and fraction >= (0.1*good):
##        if good !=0 and fraction >= 1:
#            percent[index] = percent[index] + fraction/good
##            percent[index] = percent[index] + 1
#            
#    print str(row) + "/60750"
#print percent 
#
##np.save('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/percent_count_all.npy', np.array(percent))
#np.save('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/percent.npy', np.array(percent))

arr = np.load('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/percent.npy')
#arr2 = np.load('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/percent_count.npy')

#arr3 = np.load('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/percent_count_all.npy')
#
#for x in arr3:
#    print x/60750


#for x in arr:
#    print x
for index, x in enumerate(arr):
    print "ind: " + str(index) + " " + str(( x* 100)/(60750 - len(df[df['m'] ==741])))
    

#else:
#    print
#
#print "-------------------"
#for x in arr2:
#    print x
#else: 
#    print 

#
#print "-------------------"
#df = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/Greater_10.csv')
#group = df.groupby('num_cluster')
#
#
#obj= group.count()
#
#print obj

 