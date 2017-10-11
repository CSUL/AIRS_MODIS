import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import collections


#df = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/clouds_7.csv')

df = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/data2.csv')
#

#print np.array(df)
#group = df.groupby(['cloud_1'
#                    ,
#                    'cloud_2'
#                    ,
#                    'cloud_3'
#                    ,
#                    'cloud_4'
#                    , 
#                    'cloud_5'
#                    , 
#                    'cloud_6'
#                    , 
#                    'cloud_7'
#                    ], sort = True).count()
##
##count = group.count()
##count= group.count()
##
##print count['Unnamed: 0']
##
#group = group.rename(index=str, columns={"Unnamed: 0": "count"})
#group = group.sort_values(['count'], ascending=[False])
#
#
#
#group_sort = group.loc[group['count'] >= np.max(group['count']) * 0.01]
#
#print "sum: " + str(np.max(group['count']))
#
#
#pl = group_sort.plot(kind='bar', title= '7 types of clouds', figsize = (8, 6))
#
#pl = group.plot(kind='bar', title= '7 types of clouds', figsize = (8, 6))



#percent = np.array([  5226.94586017,   5696.707799,     1131.19807018,   631.1949616,
#    933.2336812,     207.59471209,   6415.96665029,   6908.01741709,
#   1351.9509104,  28723.59031776])
#
#for index, x in enumerate(percent):
#    percent[index]= (x/60750) 
#
#print percent
#    
#
#
##print np.array(count).shape
#
#
#
#d =pd.DataFrame(group.size().reset_index(name = "Group_Count"))
#
#for index, row in d.iterrows():
#    cl1 = row['cloud_1'] 
#    cl2 = row['cloud_2']
#    pr = percent[cl1] * percent[cl2] * 100
#    rd = round(pr, 2)
#    print str((cl1, cl2)) + ": " + str(rd) + "%"





#for x in np.array(count):
#    print x


#
#cols = ['cloud_1', 'cloud_2', 'cloud_3', 'cloud_4', 'cloud_5', 'cloud_6',
#                        'cloud_7']
#data_frame = pd.DataFrame([], columns = cols)
#
##cnt =0
#for row in range(60750):
#    cluster_count =0
#    df_array =[]
#    
#    missing = df.iloc[row].iloc[31]
#    good = 741 - missing
#    
#    clouds =np.zeros(10)
#
#    for index, x in enumerate(range(1, 31, 3)):
#        fraction =df.iloc[row].iloc[x]
#        if good !=0 and fraction >= (0.1*good):
#            cluster_count = cluster_count+1
#            clouds[index] = 1
#    
#    if cluster_count ==7:
#        for index, x in enumerate(clouds):
#            if x ==1:
#                df_array.append(index) 
#        data_frame.loc[len(data_frame)]= df_array
#   
#    
#    print str(row) + "/60750"
#  
#data_frame.to_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/clouds_7.csv')


 # -*- coding: utf-8 -*-

