# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib.backends.backend_pdf import PdfPages
#import collections
from matplotlib import cm
import matplotlib.gridspec as gridspec


df = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/data2.csv')
#phase_path = '/Users/sevakm/Documents/AIRS_To_Modis/Cloud_Phase_Optical_Properties.npy'
path2 = '/Users/sevakm/Documents/AIRS_To_Modis/' + 'Cloud_Optical_Thickness.npy'
path3 = '/Users/sevakm/Documents/AIRS_To_Modis/' + 'cloud_top_pressure_1km.npy'
phase_path = '/Users/sevakm/Documents/AIRS_To_Modis/Cloud_Phase_Optical_Properties.npy'

index_path  = '/Users/sevakm/Documents/AIRS_To_Modis/index.npy'


indices = np.load(index_path)#indexes for scanline and 

thickness = np.load(path2)
pressure = np.load(path3)
phase = np.load(phase_path)

cols = ['num_cluster']
data_frame = pd.DataFrame([], columns = cols)



def log(x):
    if x >=0 and x <1000:
        return np.log(1000/x) * 7
    else:
        return x
log_func = np.vectorize(log)

#with PdfPages('/Users/sevakm/Documents/AIRS_To_Modis/contour_pdf/all3.pdf') as pdf:
    
for row in range(10):
    cluster_count =0
    df_array =[]
    
    missing = df.iloc[row].iloc[31]
    good = 741 - missing
    
    clouds = np.zeros(10)#cloud number 0 -9
    
    for cl_num, x in enumerate(range(1, 31, 3)):
        fraction =df.iloc[row].iloc[x]

        if good !=0 and fraction >= (0.1*good):
            cluster_count = cluster_count+1
            clouds[cl_num] = clouds[cl_num] +1
    
    
    fig = plt.figure(figsize = (8, 6))

    
    gs1 = gridspec.GridSpec(2, 2)
    
    
    
    patch = thickness[row]
    patch = np.ma.array(patch, mask=patch < 0)   
    mini = np.min(patch)
    mini = np.around(mini, 2)
    maxi = np.max(patch)
    maxi = np.around(maxi)
    fig.add_subplot(gs1[0])
    cp = plt.contourf(patch,levels = np.arange(0, 55, 5), extend = 'both')
    plt.title('TH | clouds: ' + str(cluster_count) +  ' | min: ' + str(mini)  +
              " max: " + str(maxi) )
    cbar =plt.colorbar(cp)
    
    
    patch = pressure[row]
    patch = np.ma.array(patch, mask=patch < 0)   
    
    patch = log_func(patch)
    
    mini = np.min(patch)
    maxi = np.max(patch)
    fig.add_subplot(gs1[1])
    
    cp = plt.contourf(patch,levels = np.linspace(0, 16), extend = 'both',cmap= cm.jet)
    
    cls =''
    for ind, c in enumerate(clouds):
        if c >0:
            cls = cls + "<" + str(ind) + ">"
    plt.title('PR | types: ' + str(cls))
    plt.colorbar(cp)

    
    patch = phase[row]
    mini = np.min(patch)
    maxi = np.max(patch)
    fig.add_subplot(gs1[2])
    cp = plt.contourf(patch,levels = np.arange(1, 5, 0.9))    
    plt.title(str('PH ' + str(indices[row])))
    cbar =plt.colorbar(cp)
    cbar.ax.get_yaxis().set_ticks([])
    for j, lab in enumerate(['Clear','Liquid','Ice','?']):
        cbar.ax.text(1.5, (2 * j + 1) / 8.0, lab, ha='left', va='center')
    cbar.ax.get_yaxis().labelpad = 15
    
   

    plt.tight_layout()
    
    fig.savefig('/Users/sevakm/Documents/AIRS_To_Modis/images/' + str(row) + '.png')
    plt.show()
