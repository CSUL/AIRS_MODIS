# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
# Cloud top temp
#==============================================================================
std = [0.91, 0.92, 1.04, 1.18, 1.64]
mean = [0.57, 0.6, 0.38, 0.39, 0.77]


plt.figure()
p1 =plt.plot(std)
p2 =plt.plot(mean)
plt.legend( (p1[0], p2[0]), ('STD', 'Mean') )
plt.axhline(0, color='black', linestyle = 'dashed')
#plt.title("Cloud Top Temperature")


#==============================================================================
# Clusters
#==============================================================================
std =[1.06, 1.99, 2.06, 2.62, 2.87]
mean = [0.65, 0.21, 0, -0.1, 0.12]

plt.figure()
p1 = plt.plot(std)
p2 =plt.plot(mean)
plt.legend( (p1[0], p2[0]), ('STD', 'Mean') )
plt.axhline(0, color='black', linestyle = 'dashed')


#plt.title("Clusters")

#==============================================================================
# Brightness temp
#==============================================================================
std = [1.06, 1.22, 1.49, 2.34, 2.5]
mean = [0.74, 0.78, 0.3, -0.4, -0.47]

plt.figure()
#plt.scatter(std, mean)
p1 = plt.plot(std)
p2 =plt.plot(mean)
plt.legend( (p1[0], p2[0]), ('STD', 'Mean') )
plt.axhline(0, color='black', linestyle = 'dashed')
#plt.title("Brightness Temperature")