import numpy as np
import pandas as pd

df = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/data.csv')


#group = df.groupby('num_cluster')
#print group.count()

    
count =0
for row in range(60750):
    missing = df.iloc[row].iloc[41]
#    good = 741- missing
    if missing <=740:
        count = count +1
    print str(row) + "/60750"

print "count is: " + str(count)

    


