# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

#!/opt/python/anaconda-2.4/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 19:10:40 2017

@author: sevakm
"""
from scipy.cluster.vq import kmeans2
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.cluster import KMeans
#from matplotlib.colors import LogNorm
#from mpl_toolkits.mplot3d import Axes3D
import collections
import pandas as pd
from matplotlib import cm
import matplotlib.gridspec as gridspec


df = pd.read_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/data2.csv')

#path = '/Users/sevakm/Documents/AIRS_To_Modis/normalized/' + 'cloud_top_pressure_1km_NORMALIZED.npy'
path = '/Users/sevakm/Documents/AIRS_To_Modis/' + 'cloud_top_pressure_1km.npy'
path2 = '/Users/sevakm/Documents/AIRS_To_Modis/' + 'Cloud_Optical_Thickness.npy'
path3 = '/Users/sevakm/Documents/AIRS_To_Modis/' + 'Cloud_Effective_Radius.npy'

phase_path = '/Users/sevakm/Documents/AIRS_To_Modis/Cloud_Phase_Optical_Properties.npy'

index_path  = '/Users/sevakm/Documents/AIRS_To_Modis/index.npy'

temp_path = '/Users/sevakm/Documents/AIRS_To_Modis/cloud_top_temperature_1km.npy'

temperature = np.load(temp_path)

print np.min(temperature[0])
print np.max(temperature[0])




#
#path = '/Users/sevakm/Documents/AIRS_To_Modis/normalized/' + 'cloud_top_pressure_1km_NORMALIZED.npy'
#path2 = '/Users/sevakm/Documents/AIRS_To_Modis/normalized/' + 'Cloud_Optical_Thickness_NORMALIZED.npy'
#path3 = '/Users/sevakm/Documents/AIRS_To_Modis/normalized/' + 'Cloud_Effective_Radius_NORMALIZED.npy'


indices = np.load(index_path)

pressure = np.load(path)
pressure1 = np.load(path)
JOB_SIZE, r, c = pressure.shape
#pressure_data = pressure
#
#
#r, row, col = pressure_data.shape
#pressure_data = pressure_data.reshape(r * row, col)

thickness = np.load(path2)
thickness1 = np.load(path2)
#thickness_data = thickness
#r, row, col = thickness_data.shape
#thickness_data = thickness_data.reshape(r * row, col)

phase = np.load(phase_path)
phase1 = np.load(phase_path)



centers = np.array([
                    [195, 1.3],#0
                    [195, 9.4],#1
                    [195, 60],#2
                    [560, 1.3],#3
                    [560, 9.4],#4
                    [560, 60], #5
                    [840, 1.3],#6
                    [840, 9.4],#7
                    [840, 60],#8
                    [0, 0]#9
                    ,[-9999, -9999]
                    ])
    
#print "center shape: " + str(centers.shape)

#test patch one

#==============================================================================
#DATAFRAME TO HOLD ALL CLUSTER INFO
cols = ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10']
        
data_frame = pd.DataFrame([], columns = cols)
#print "DATAFRAME: " + str(data_frame)
#==============================================================================
def log(x):
    if x >=0 and x <1000:
        return np.log(1000/x) * 7
    else:
        return x
log_func = np.vectorize(log)

loss = 0


seven = [23323,
42781,
43439,
43704,
46075,
47979,
49233,
52539,
54850,
55904
]

one = [38,39,40,41,42,43,44,48,49,50,51,52,53,54,55,56,58,59,60,61,62,122,123,124,125,130,131,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,213,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,302,315,316,317,318,319,320,321,322,323,324,326,327,328,341,342,392,403,404,405,406,407,408,409,410,411,412,413,414,431,442,479,480,481,482,483,492,493,494,495,496,497,498,499,500,501,502,503,569,570,571,572,573,574,582,583,584,585,586,587,588,589,590,591,592,593,656,657,658,659,660,675,676,677,678,679,680,681,682,697,744,745,746,747,753,766,767,768,769,771,833,834,835,836,843,852,853,854,855,856,857,858,859,860,920,921,922,923,924,937,938,939,940,941,942,943,946,947]
two = [0,1,4,5,6,14,15,18,19,21,22,23,24,25,28,29,34,45,46,47,63,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,91,99,101,102,103,104,105,108,109,110,111,112,113,114,116,121,135,154,155,156,157,158,159,160,161,162,163,164,165,166,169,170,171,180,181,182,188,191,193,195,200,201,202,203,206,212,216,217,220,241,243,244,245,246,247,248,249,250,251,252,253,254,255,258,259,260,264,270,277,281,282,283,284,285,286,287,290,293,303,305,308,311,312,313,314,325,331,332,333,334,335,336,337,338,339,340,343,344,345,346,347,348,349,353,366,370,375,376,379,393,396,417,419,420,421,422,423,424,425,426,427,428,429,430,432,433,434,436,437,438,439,440,441,443,444,445,446,451,452,453,457,465,466,468,475,476,504,505,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,541,547,549,554,555,556,557,564,565,575,577,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611]
three = [2,3,7,8,9,12,13,16,17,20,26,27,30,32,33,35,36,37,57,65,79,82,83,84,85,86,87,90,92,93,96,97,100,106,107,115,117,118,119,120,127,128,129,132,133,134,152,153,167,168,174,175,177,183,185,186,187,189,190,192,194,196,197,198,199,205,207,209,210,214,215,218,219,221,242,256,257,261,265,267,269,271,272,274,276,278,279,280,288,289,291,292,294,295,296,298,299,301,304,306,307,329,330,350,351,352,354,355,358,359,360,361,362,363,364,368,369,371,372,373,374,377,378,380,381,383,386,387,388,389,390,391,394,395,397,400,401,402,415,416,418,435,449,454,455,456,458,459,460,461,462,463,464,467,469,470,471,472,473,474,477,478,484,486,488,489,490,491,506,536,537,542,546,548,550,553,558,561,562,563,568,576,578,579,580,581,596,612,620,625,628,629,633,636,639,640,641,642,644,645,646,647,648,649,650,651,653,655,664,665,667,672,673,674,683,684,685,702,712,713,714,715,718,724,727,728,729,730,733,736,737,738,740,742,743,749,751,752,754,755,760,772,778,791,792,802,803,804,808,810,812,816,817,819,820,821,822,823,825,829,830,831,837,841,844,846,847,848,850,861,880,881,882,888,891,892,894,896,902,903,905,906,907,908,909,910,912,913,914,916,917,918,919,926,927,928,931,932,934,948,968,969,970,971,981,987,989,991,995,1001,1002,1003,1004,1005,1006,1007,1009,1015,1016,1024,1038,1042,1043,1044,1057,1058,1061,1070,1071,1072,1073,1074,1075,1077,1079,1081,1082,1091,1092,1093,1094,1095,1096,1105,1106,1113,1114,1122,1125,1127,1128,1146,1147,1159,1162,1164,1165,1166,1167,1171,1174,1176,1177,1178,1179,1180,1181,1185,1186,1195,1196,1198,1199,1200,1202,1204,1205,1211,1212,1213,1214,1218,1220,1222,1235,1237,1248,1249,1251]
four = [10,11,31,64,88,89,94,95,98,126,172,173,176,178,184,204,208,211,222,223,224,225,263,266,268,273,275,297,300,309,310,356,365,367,382,384,385,398,399,447,448,450,485,487,507,538,539,540,545,551,552,559,560,566,567,594,595,626,630,634,654,668,669,670,671,716,717,719,720,721,722,725,757,758,759,805,806,811,814,818,845,895,901,904,911,935,936,949,950,985,988,993,994,996,997,1023,1039,1076,1078,1080,1083,1085,1086,1087,1123,1124,1160,1161,1168,1169,1170,1172,1173,1175,1203,1215,1216,1250,1261,1262,1265,1275,1305,1344,1345,1348,1349,1351,1353,1364,1365,1375,1382,1433,1434,1435,1436,1439,1444,1445,1452,1453,1454,1455,1456,1520,1521,1523,1524,1531,1532,1535,1541,1542,1546,1599,1600,1601,1610,1611,1617,1618,1619,1620,1621,1636,1642,1647,1650,1687,1688,1691,1705,1710,1725,1726,1727,1740,1741,1742,1743,1781,1789,1808,1822,1823,1824,1826,1872,1878,1880,1885,1886,1890,1891,1895,1910,1953,1954,1955,1977,1978,1980,2042,2054,2059,2060,2061,2065,2067,2070,2073,2074,2143,2148,2151,2157,2163,2175,2223,2228,2233,2238,2239,2245,2250,2324,2328,2333,2354,2396,2403,2404,2413,2420,2423,2424,2425,2430,2439,2484,2485,2508,2509,2515,2521,2526,2530,2573,2598,2599,2602,2603,2604,2612,2620,2621,2675,2688,2689,2690,2691,2692,2693,2709,2752,2762,2763,2767,2778,2779,2780,2783,2795,2842,2851,2852,2855,2856,2870,2873,2885,2887,2888]
five = [179,262,357,543,544,631,632,809,897,898,899,1257,1263,1346,1350,1352,1441,1442,1526,1616,1711,1795,1801,1887,2064,2149,2150,2154,2240,2241,2244,2329,2331,2334,2514,2766,2857,2946,3035,3049,3139,3227,3316,3575,4106,4446,4447,4448,4628,4719,4720,4721,4806,4807,4813,4898,4899,4900,4925,4976,4984,4988,5065,5066,5103,5164,5256,5257,5258,5279,5311,5341,5344,5368,5369,5370,5428,5432,5597,5633,5684,5685,5698,5718,5722,5782,5783,5785,5803,5850,5865,5866,5867,5876,5893,5899,5952,5954,5957,5985,6038,6039,6040,6052,6064,6125,6129,6216,6217,6218,6243,6249,6305,6306,6308,6327,6332,6339,6395,6405,6422,6529,6575,6582,6583,6660,6663,6666,6753,6754,6762,6840,6934,6939,7026,7028,7110,7112,7113,7114,7117,7118,7201,7204,7290,7292,7294,7381,7383,7384,7385,7386,7387,7470,7473,7565]
six = [2330,4989,5165,5457,5715,5892,6128,7200,7291,7380,7471,7474,16804,17208,17487,17562,18368,18721,18722,21172,21182,21501,22107,22287,22359,22373,22437,22462,22549,23230,23413,23430,23499,23701,23716,23717,23946,24034,24053,24406,25475,25739,27109,37665,38091,38503,38574,38752,38770,38940,38942,39419,40327,40330,40604,41334,41503,41860,41899,41902,41949,41984,42031,42039,42137,42151,42158,42167,42219,42237,42238,42241,42242,42243,42303,42329,42396,42405,42406,42407,42424,42427,42435,42482,42494,42499,42508,42529,42593,42598,42601,42680,42682,42691,42692,42752,42767,42771,43261,43562,43658,43664,44021,44059,44575,44576,44583,45297,45486,45762,45898,45987,45989,46252,46544,46615,47517,47534,48069,48596,48779,48784,48788,48970,49115,49144,49862,51216,51223,51762,51782,52023,52923,53102,53402,54760,54847,54848,54849,55701,55702,55813,55881,55971,56003,56060,56063,56342,56382,57062,57229,57303,57313,58215,58226,58315,58769,60690]

for round in range(JOB_SIZE):
    
    temperature_data = temperature[round]
    row, col = temperature_data.shape
    temperature_data = temperature_data.reshape(row* col, 1)
    
    pressure_data = pressure[round]
    row, col = pressure_data.shape
    
#    print "row:" + str(row) + " col: " + str(col)
    pressure_data = pressure_data.reshape(row* col, 1)
    
    thickness_data = thickness[round]
    row, col = thickness_data.shape
    thickness_data = thickness_data.reshape(row* col, 1)
    
    phase_data = phase[round]
    row, col = phase_data.shape
    phase_data = phase_data.reshape(row* col, 1)
    
    bad_val_array =[]
    bad_val_bool_array = np.full((741, 1), False, dtype=bool)
    
#    print bad_val_bool_array
    
    #Clean bad data 
    
#    summary =[]
    
    index =0
    for x, y, z in zip(pressure_data, thickness_data, phase_data):
        
        #clean pressure_data
        for a, b, c in zip(x, y, z):
            if a <0 or a >1000:
                if c ==1:
                    pressure_data[index] =1
                else:
                    if not index in bad_val_array:
                        bad_val_array.append(index)
                        bad_val_bool_array[index] = True
#                        summary.append(c)
#                        print "bad: " + str(c)
                        continue
                    
            #clean thickness_data
            if b < 0 or b >100:
                if c ==1:
                    thickness_data[index] =0
                else:
                    if not index in bad_val_array:
                        bad_val_array.append(index)
                        bad_val_bool_array[index] = True
#                        print "bad: " + str(c)
#                        summary.append(c)
                        
                              
          
        index = index +1
        
#        print str(round) + "/" + str(JOB_SIZE)


#print "results: " + collections.Counter(summary)
#    plot_data = np.concatenate((log_func(pressure_data), thickness_data), axis = 1)
#    plot_data = np.delete(plot_data, bad_val_array, axis = 0)
    
#    data_mask1 = np.ma.array(pressure_data, mask=bad_val_bool_array ) 
#    data_mask2 = np.ma.array(thickness_data, mask=bad_val_bool_array ) 
    
#    data = np.concatenate((data_mask1, data_mask2), axis =1)
    
    
    data = np.concatenate((pressure_data, thickness_data), axis =1)
#    print "concat shape: " + str(data.shape)
    
    for index, x in enumerate(data):
        if index in bad_val_array:
            data[index] = [-9999, -9999]
    
            
#    data = np.delete(data, bad_val_array, axis = 0)

    
#    print "data shape: " + str(data.shape)
#    print "bad_val_array:" + str(len(bad_val_array))
#    print "shape of data: " + str(data.shape)
    
#    loss = loss + len(bad_val_array)
#    print str(round) + "/" + str(JOB_SIZE)
    
    
#    print "bad val size: " + str(loss)    

    

    
    km = '' #placeholder for to hold the result of k-means
    
    if len(data) == 0:
        zeros = np.zeros(10).tolist()
       
        data_frame.loc[len(data_frame)] = zeros
#        data_frame.loc[len(data_frame)] = len(bad_val_array)
    else: 
        km = kmeans2(data, centers)
        
        
        
        df_array= np.zeros(10)
        
        
        counter=collections.Counter(km[1])
        
#        print counter
#        print km[0]
        good = 741 - len(bad_val_array)
        for index, x in enumerate(km[0]):
    #        print "index: " + str(index)
            
            if index in counter and index != 10:#10 is for bad data. We don't use it
                fraction = counter[index]
                if index !=9: #cloud type other than clear
                    
                    
                    if fraction >= (0.1*good):
                        cur_mask = km[1] == index
                        cur_temp = temperature_data[cur_mask]
                        
    #                    print "min: " + str(np.min(cur_temp))
    #                    print "max: " + str(np.max(cur_temp))
    #                    
    #                    print "old temp: " + str(cur_temp.shape)
                        
                        msk = np.logical_and(cur_temp >=(150000 * 0.00999999977648), cur_temp <=(350000 * 0.00999999977648))
                        cur_temp = np.ma.array(cur_temp, mask = msk)
                        
    #                    print "newp temp: " + str(cur_temp.shape)
                        
                        df_array[index] = np.sum(cur_temp)/fraction
                    
                else:#clear sky
                    if fraction >= (0.1*good):
                        df_array[index] = -1 #-1 for clear sky to be replaced by clear sky mean
                                         #temp from other file
                        
            
                
        data_frame.loc[len(data_frame)]= df_array
        print str(round) + "/" + str(JOB_SIZE)
        
data_frame.to_csv('/Users/sevakm/Documents/AIRS_To_Modis/DataFrame/metric3_with_clear.csv')

#
