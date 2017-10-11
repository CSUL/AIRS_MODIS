import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/clouds_2.csv')


group = df.groupby(['cloud_1', 'cloud_2'])

print group.count()


cols = ['cloud_1', 'cloud_2']
data_frame = pd.DataFrame([], columns = cols)
#
##cnt =0
for row in range(60750):
    cluster_count =0
    df_array =[]
    
    missing = df.iloc[row].iloc[41]
    good = 741 - missing
    
    clouds =np.zeros(10)

    for index, x in enumerate(range(1, 41, 4)):
        fraction =df.iloc[row].iloc[x]
        if good !=0 and fraction >= (0.1*good):
            cluster_count = cluster_count+1
            clouds[index] = 1
    
    if cluster_count ==2:
        for index, x in enumerate(clouds):
            if x ==1:
                df_array.append(index) 
        data_frame.loc[len(data_frame)]= df_array
   
    
    print str(row) + "/60750"
  
data_frame.to_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/clouds_2.csv')


 