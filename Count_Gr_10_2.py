import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/Greater_10_2.csv')

#print np.sum(df[['m']]) / (741* 60750) -np.sum(df[['m']])
group = df.groupby('num_cluster')


obj= group.count()

print obj
#
#arr = np.array(obj)
#
#D= obj.to_dict()['Unnamed: 0']
#
#plt.bar(range(len(D)), D.values(), align='center')
#plt.xticks(range(len(D)), D.keys())
#
#plt.show()

#cols = ['num_cluster']
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
#
#    for x in range(1, 31, 3):
#        fraction =df.iloc[row].iloc[x]
#
#        if good !=0 and fraction >= (0.1*good):
#            cluster_count = cluster_count+1
#
#    df_array.append(cluster_count)
#    data_frame.loc[len(data_frame)]= df_array
#    print str(row) + "/60750"
#
#    
#data_frame.to_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/Greater_10_2.csv')


 