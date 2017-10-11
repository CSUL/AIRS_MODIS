import pandas as pd
import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

df = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/data2.csv')

#index_path  = '/Users/sevakm/Documents/AIRS_To_Modis/index_summary.npy'
#indices = np.load(index_path)#indexes for scanline and 
#
data_frame =pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/index.csv')

nc_f = '/Users/sevakm/Documents/AIRS_To_Modis/weather/2013.03.02.Ascending.nc' 
nc_fid = Dataset(nc_f, 'r')  
                             


# Extract data from NetCDF file
pressure = nc_fid.variables['tatm_layerPressures'][:]  # extract/copy the data


def log(x):
        return np.log(1000/x) * 7
    
log_func = np.vectorize(log)

pressure = log_func(pressure)


bottom2 = []
for index, x in enumerate(pressure):
    if x >=1 and x <=2.1:
        bottom2.append(index)

print "\n\n"

tatm_ig = nc_fid.variables['tatm_ig'][:]
tatm = nc_fid.variables['tatm'][:]

bottom_first = bottom2[0]
bottom_last = bottom2[len(bottom2)-1]

tatm_2km = tatm[:, bottom_first: bottom_last +1]
tatm_ig_2km = tatm_ig[:, bottom_first: bottom_last +1]

clean_tatm_2km = np.ma.array(tatm_2km, mask= np.isnan(tatm_2km))   
clean_tatm_ig_2km =np.ma.array(tatm_ig_2km, mask= np.isnan(tatm_ig_2km)) 

#==============================================================================
# plot
#==============================================================================
arr = np.array(data_frame['c'])
max_cluster_count = np.max(data_frame['c'])


tatm_delete_indices =[]
for index, x in enumerate(clean_tatm_2km):
    if x.all() is np.ma.masked:
        tatm_delete_indices.append(index)

#print "shape: " + str(len(tatm_indices) *6) + "/" + str(clean_tatm_2km.size)

#tatm_ig_indices =[]
for index, x in enumerate(clean_tatm_ig_2km):
    if x.all() is np.ma.masked:
        if index not in tatm_delete_indices:
            tatm_delete_indices.append(index)

#print one_cluster.iloc[2]

#print "ones: " + str(one_cluster.shape)






#==============================================================================
# all cluster graphs
#==============================================================================

granule = nc_fid.variables['granule'][:]
scanline = nc_fid.variables['track'][:]
footprint = nc_fid.variables['xTrack'][:]

#current cluster (cont 1-10max)
#for cluster_count in np.arange(2, 8):
#    cluster = np.array(data_frame.loc[
#                                    (data_frame['c'] == cluster_count) 
#                                    &(data_frame['f'] >= 26)
#                                    &(data_frame['f'] <= 69)
#                                ])
#
#    cluster = cluster[:, 1:cluster.shape[1]-1]
#
#    current_tatm_delete_indices = tatm_delete_indices[:]
##    current_good_tatm =[]
#    
#    cluster_list = cluster.tolist()
#    
#    for x in range(tatm_2km.shape[0]):
#        if x not in current_tatm_delete_indices:
#            tatm_pos_arr= []
#            
#            tatm_s = scanline[x]
#            tatm_f = footprint[x]
#            tatm_g =granule[x]
#            
#            tatm_pos_arr.append(tatm_s)
#            tatm_pos_arr.append(tatm_f)
#            tatm_pos_arr.append(tatm_g)
#            
#            
#            if tatm_pos_arr not in cluster_list:
#                current_tatm_delete_indices.append(x)
#            
#            print str(cluster_count) + ": " + str(x)

cluster_path = '/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/cluster'
cluster_path = cluster_path + str(7) + ".npy"
#    
#    np.save(cluster_path, np.array(current_tatm_delete_indices))
    

delete = np.load(cluster_path)

tatm_delete_indices = delete.tolist()

tatm_2km = np.delete(tatm_2km, tatm_delete_indices, axis =0)
tatm_ig_2km = np.delete(tatm_ig_2km, tatm_delete_indices, axis =0)

r, c = tatm_2km.shape
dif = np.zeros([r, c])
dif[dif ==0] = 9999


for row, x in enumerate(tatm_2km):
    for col, y in enumerate(x):
        if ~np.isnan(y) and ~np.isnan(tatm_ig_2km[row][col]):
            dif[row][col] = y - tatm_ig_2km[row][col]

items = dif[dif !=9999]
count =items.size

dif = np.ma.array(dif, mask= dif ==9999)


plt.figure()
n, b ,p =plt.hist(dif.compressed(), normed=1, facecolor='green', align ='mid', range = [-10, 10], bins =1000)
plt.grid(True)

plt.title("CLUSTERS: " + str(7) + " min: " + str(round(np.min(dif), 2)) + "| max: " + str(round(np.max(dif), 2))
        + "| STD: " + str(round(np.std(items), 2)) 
        + " | mean: " + str(round(np.mean(items), 2))  + "| values: "+ str(count))
plt.show()


#cols = ['s', 'f', 'g', 'c']
#data_frame = pd.DataFrame([], columns = cols)
#
#
#    
#       
#
#    
#for row in range(len(indices)):
#    cluster_count =0
#    df_array =[]
#    
#    missing = df.iloc[row].iloc[31]
#    good = 741 - missing
#    
#    clouds = np.zeros(10)#cloud number 0 -9
#    
#    for cl_num, x in enumerate(range(1, 31, 3)):
#        fraction =df.iloc[row].iloc[x]
#
#        if good !=0 and fraction >= (0.1*good):
#            cluster_count = cluster_count+1
#            clouds[cl_num] = clouds[cl_num] +1
#            
#    df_array.append(indices[row][0])
#    df_array.append(indices[row][1])
#    df_array.append(indices[row][2])
#    df_array.append(cluster_count)
#    
#    data_frame.loc[len(data_frame)]= df_array
#    print str(row) + "/" + str(len(indices))
#
#data_frame.to_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/index.csv')

    
    