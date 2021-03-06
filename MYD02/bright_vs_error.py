# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import pandas as pd

path = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/EV_1KM_Emissive.npy'
bright = np.load(path)

print bright.shape
data_frame =pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/index.csv')

#path = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/bright_summary.npy'
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


bright_arr = []

for x in bright:
    bright_arr.append(np.std(x))

sorted_arr = np.sort(bright_arr)
bright_arr = np.array(bright_arr)
    



range_one = sorted_arr[int(len(sorted_arr) *0.2)]
range_two = sorted_arr[int(len(sorted_arr) *0.4)]
range_three = sorted_arr[int(len(sorted_arr) *0.6)]
range_four = sorted_arr[int(len(sorted_arr) *0.8)]
range_five = sorted_arr[-1]


#range_five = int(len(arr) *0.2)
#print "e: " + str(range_one)
#
#print "percent: " + str(range_one)
#print "percent: " + str(range_two)
#print "percent: " + str(range_three)
#print "percent: " + str(range_four)

mask_arr = []

mask_arr.append(bright_arr < range_one)
mask_arr.append((bright_arr >= range_one) & (bright_arr < range_two))
mask_arr.append((bright_arr >= range_two) & (bright_arr < range_three))
mask_arr.append((bright_arr >= range_three) & (bright_arr < range_four))
mask_arr.append(bright_arr >= range_four)

#print "sh: " + str(np.array(mask_arr).shape)
#
#print "len: " + str(np.intersect1d(mask_arr[1][mask_arr[1] ==True], mask_arr[4][mask_arr[4] ==True]) )

#cluster = np.array(data_frame.loc[:])
#
#cluster = cluster[:, 1:cluster.shape[1]-1]
#
#
#std_list1 = cluster[mask_arr[0]].tolist()
#std_list2 = cluster[mask_arr[4]].tolist()
#
#
#
##for x in range(20):
##    print str(std_list1[x]) + " : " + str(std_list2[x])
#cnt =0
#for lin in std_list1:
#    if lin in std_list2:
#        cnt = cnt + 1
#
#print "cnt: " + str(cnt)

       
#    


#print mask

#current cluster (cont 1-10max)
#for cur_std in np.arange(5):
#    cluster = np.array(data_frame.loc[:])
#    
#    cluster = cluster[:, 1:cluster.shape[1]-1]
#    
##    print "shape b4: " + str(cluster.shape)
#    
#    std_list = cluster[mask_arr[cur_std]].tolist()
#    
#    
##    print "shape after: " + str(std_list.shape)
#    
#    current_tatm_delete_indices = tatm_delete_indices[:]
##    current_good_tatm =[]
#    
#    
#    
#    for index, x in enumerate(range(tatm_2km.shape[0])):
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
#            if tatm_pos_arr not in std_list:
#                current_tatm_delete_indices.append(x)
##            else:
##                current_good_tatm.append(x)
#    
##    print str(cur_std) + ": " + str(len(current_good_tatm))
#    #            
#            print str(index) + "/" + str(tatm_2km.shape[0])
#    #
#    cluster_path = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/range'
#    cluster_path = cluster_path + str(cur_std +1) + ".npy"
#    
#    np.save(cluster_path, np.array(current_tatm_delete_indices))


cluster_path = '/Users/sevakm/Documents/AIRS_To_Modis/MYD02/range'
cluster_path = cluster_path + str(5) + ".npy"

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

plt.title("STD range: [" + str(round(range_four, 2)) +  ", "  
                       + str(round(range_five, 2)) + ") |" 
                 + " min: " 
                       + str(round(np.min(dif), 2)) + "| max: " + str(round(np.max(dif), 2))
        + " | mean: " + str(round(np.mean(items), 2))  + "| std: " + str(round(np.std(items), 2)) )
    

plt.show()
##    

#plt.figure(figsize =(8, 6))
#n, b ,p =plt.hist(arr, normed=1, 
#                  bins =1000,
#                  histtype = 'step',
##                  range =[0,1],
#                  cumulative=True)
##plt.xticks(np.arange(100))
#print norm.pdf(arr).shape
#
#plt.title("min: " + str(np.min(arr)) + " | max: " 
#                  + str(round(np.max(arr), 2)) + 
#                  " | mean: " + str(round(np.mean(arr), 2)))
#plt.grid(True)
#
##print b[1]
##ax = plt.gca()
##print ax.lines[0]
#
#plt.figure()
#n, b ,p =plt.hist(arr, normed=1, 
#                  facecolor='green',bins =1000,
#                  cumulative=False, range =[0, 20])
#
#plt.title("min: " + str(np.min(arr)) + " | max: " 
#                  + str(round(np.max(arr), 2)) + 
#                  " | mean: " + str(round(np.mean(arr), 2)))