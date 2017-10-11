#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:35:14 2017

@author: sevakm
"""
import numpy as np


#
#for index, x in enumerate(range(1, 41, 4)):
##    print x
#    print x 

arr = np.load('/Users/sevakm/Documents/AIRS_To_Modis/Cloud_Phase_Optical_Properties.npy')

l, r, c = arr.shape

print l
#count = np.zeros(5)
#
#valid = [0, 1, 2, 3, 4]
#cnt =0
#
##print arr[0].shape
for x in range(1):
    print arr[x].shape
#    count[0] = count[0]+ np.count_nonzero(arr[x] ==0)
#    count[1] = count[1]+ np.count_nonzero(arr[x] ==1)
#    count[2] = count[2]+ np.count_nonzero(arr[x] ==2)
#    count[3] = count[3]+ np.count_nonzero(arr[x] ==3)
#    count[4] = count[4]+ np.count_nonzero(arr[x] ==4)
##    for y in arr[x]:
##        print y.shape
##        print y
##        if y !=0 or y !=1 or y!=2 or y!=3 or y!=4:
##            pass
##            cnt = cnt +1
##        if y ==0:
##            count[0] = count[0]+1
##        elif y ==1:
##            count[1] = count[1]+1
##        elif y ==2:
##            count[2] = count[2]+1
##        elif y ==3:
##            count[3] = count[3]+1
##        elif y ==4:
##            count[4] = count[4]+1
##    print str(x) + "/60750"
#
##print "cnt: " + str(count)
##print str(l * r* c)
#print "count: " + str(count)