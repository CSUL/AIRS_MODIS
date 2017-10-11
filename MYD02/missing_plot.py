# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/data2.csv')


missing = np.array(df['m'])

sorted_arr = np.sort(missing)
missing = np.array(missing)
    



range_one = sorted_arr[int(len(sorted_arr) *0.2)]
range_two = sorted_arr[int(len(sorted_arr) *0.4)]
range_three = sorted_arr[int(len(sorted_arr) *0.6)]
range_four = sorted_arr[int(len(sorted_arr) *0.8)]
range_five = sorted_arr[-1]


mask_arr = []

mask_arr.append(missing < range_one)
mask_arr.append((missing >= range_one) & (missing < range_two))
mask_arr.append((missing >= range_two) & (missing < range_three))
mask_arr.append((missing >= range_three) & (missing < range_four))
mask_arr.append(missing >= range_four)



plt.figure(figsize =(8, 6))
n, b ,p =plt.hist(missing, normed=1, 
                  bins =1000,
                  histtype = 'step',
#                  range =[0,1],
                  cumulative=True)
#plt.xticks(np.arange(100))


plt.title("min: " + str(np.min(missing)) + " | max: " 
                  + str(round(np.max(missing), 2)) + 
                  " | mean: " + str(round(np.mean(missing), 2)))
plt.grid(True)

#print b[1]
#ax = plt.gca()
#print ax.lines[0]

plt.figure()
n, b ,p =plt.hist(missing, normed=1, 
                  facecolor='green',bins =1000,
                  cumulative=False)

plt.title("min: " + str(np.min(missing)) + " | max: " 
                  + str(round(np.max(missing), 2)) + 
                  " | mean: " + str(round(np.mean(missing), 2)))
plt.axis([0, 741, 0, 0.03])