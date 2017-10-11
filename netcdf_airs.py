

import numpy as np
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import collections



def ncdump(nc_fid, verb=True):

    def print_ncattr(key):

        try:
            print "\t\ttype:", repr(nc_fid.variables[key].dtype)
            for ncattr in nc_fid.variables[key].ncattrs():
                print '\t\t%s:' % ncattr,\
                      repr(nc_fid.variables[key].getncattr(ncattr))
        except KeyError:
            print "\t\tWARNING: %s does not contain variable attributes" % key

    # NetCDF global attributes
    nc_attrs = nc_fid.ncattrs()
    if verb:
        print "NetCDF Global Attributes:"
        for nc_attr in nc_attrs:
            print '\t%s:' % nc_attr, repr(nc_fid.getncattr(nc_attr))
    nc_dims = [dim for dim in nc_fid.dimensions]  # list of nc dimensions
    # Dimension shape information.
    if verb:
        print "NetCDF dimension information:"
        for dim in nc_dims:
            print "\tName:", dim 
            print "\t\tsize:", len(nc_fid.dimensions[dim])
            print_ncattr(dim)
    # Variable information.
    nc_vars = [var for var in nc_fid.variables]  # list of nc variables
    if verb:
        print "NetCDF variable information:"
        for var in nc_vars:
            if var not in nc_dims:
                print '\tName:', var
                print "\t\tdimensions:", nc_fid.variables[var].dimensions
                print "\t\tsize:", nc_fid.variables[var].size
                print_ncattr(var)
    return nc_attrs, nc_dims, nc_vars

nc_f = '/Users/sevakm/Documents/AIRS_To_Modis/weather/2013.03.02.Ascending.nc' 
nc_fid = Dataset(nc_f, 'r')  
                             
#nc_attrs, nc_dims, nc_vars = ncdump(nc_fid)

# Extract data from NetCDF file
pressure = nc_fid.variables['tatm_layerPressures'][:]  # extract/copy the data
#print "shape: " + str(pressure.shape)

print pressure

def log(x):
        return np.log(1000/x) * 7
    
log_func = np.vectorize(log)

pressure = log_func(pressure)

#for x in pressure:
#    print x

#for x in pressure: 
#    print x

#arra [1, 3, 4, 5]

bottom2 = []
for index, x in enumerate(pressure):
    if x >=1 and x <=2.1:
        bottom2.append(index)


#print "indices: " + str(bottom2)
print "\n\n"

tatm_ig = nc_fid.variables['tatm_ig'][:]
tatm = nc_fid.variables['tatm'][:]

#print "Orig tatm shape:" + str(tatm.shape)

#print bottom2

bottom_first = bottom2[0]
bottom_last = bottom2[len(bottom2)-1]

tatm_2km = tatm[:, bottom_first: bottom_last +1]
tatm_ig_2km = tatm_ig[:, bottom_first: bottom_last +1]

#tatm_bad_rows= []
#tatm_ig_bad_rows= []

all_bad_rows =[]

#bad= []
#bad_ig =[]

for index, x in enumerate(tatm_2km):
    if np.isnan(x).any():
        all_bad_rows.append(index)

        
for index, x in enumerate(tatm_ig_2km):
    if np.isnan(x).any():
        if index not in all_bad_rows:
            all_bad_rows.append(index)
        


clean_tatm_2km = np.delete(tatm_2km, all_bad_rows, axis = 0)
clean_tatm_ig_2km = np.delete(tatm_ig_2km, all_bad_rows, axis = 0)


#==============================================================================
# Difference plot
#==============================================================================
r, c = clean_tatm_2km.shape
dif = np.empty([r, c])

#print "clean_tatm_2km shape: " + str(clean_tatm_2km.shape)
#print "dif shape: " + str(dif.shape)

print "first tatm: " + str(clean_tatm_2km[100][1])
print "first tatmIG: " + str(clean_tatm_ig_2km[100][1])


for row, x in enumerate(clean_tatm_2km):
    for col, y in enumerate(x):
        dif[row][col] = y -clean_tatm_ig_2km[row][col]
        

#print "flat shape: " + str(dif.flatten)
counter = collections.Counter(dif.flatten())
#print "Dif count: " + str(counter.most_common(len(dif.flatten())/10))
plt.figure()
plt.hist(dif, normed=1, facecolor='green', bins = 100)
plt.grid(True)
#plt.axis([-1, 5, 0, 0.2])
plt.title("min: " + str(np.min(dif.flatten())) + " max: " + str(np.max(dif.flatten())))
plt.show()

tatm_average = np.average(clean_tatm_2km)
tatm_ig_average = np.average(clean_tatm_ig_2km)

###########################


########3


fig = plt.figure(figsize = (8, 6))
gs1 = gridspec.GridSpec(2, 2)

fig.add_subplot(gs1[0])
n, bins, patches = plt.hist(clean_tatm_2km, normed=1, facecolor='green', bins =100)
plt.grid(True)
plt.title("tatm ALL | rows: " + str(len(clean_tatm_2km)) 
                    + "/" + str(len(tatm)))




code = nc_fid.variables['stopCode'][:]

#==============================================================================
# Stop code 1
#==============================================================================
#tatm_code_1 = clean_tatm_2km[:]
#to_delete = []
#
#for index, x in enumerate(code):
#    if x !=1:
#      to_delete.append(index)
#      
#tatm_code_1 = np.delete(tatm_code_1, to_delete, axis = 0)
##
#fig.add_subplot(gs1[1])
#n, bins, patches = plt.hist(tatm_code_1, normed=1, facecolor='green')
#plt.grid(True)
#plt.title("tatm stop code 1 | rows: " + str(len(tatm_code_1)) 
#                    + "/" + str(len(tatm)))
#
##==============================================================================
## Stop code 2
##==============================================================================
#tatm_code_2 = clean_tatm_2km[:]
#to_delete = []
#
#for index, x in enumerate(code):
#    if x !=2:
#      to_delete.append(index)
#
#tatm_code_2 = np.delete(tatm_code_2, to_delete, axis = 0)
#
#fig.add_subplot(gs1[2])
#n, bins, patches = plt.hist(tatm_code_2, normed=1, facecolor='green')
#plt.grid(True)
#plt.title("tatm stop code 2 | rows: " + str(len(tatm_code_2)) 
#                    + "/" + str(len(tatm)))
##
##
###==============================================================================
### Stop code 3
###==============================================================================
#tatm_code_3 = clean_tatm_2km[:]
#to_delete = []
#
#for index, x in enumerate(code):
#    if x !=3:
#      to_delete.append(index)
#
#tatm_code_3 = np.delete(tatm_code_3, to_delete, axis = 0)
#
#
#fig.add_subplot(gs1[3])
#n, bins, patches = plt.hist(tatm_code_3, normed=1, facecolor='green')
#plt.grid(True)
#plt.title("tatm stop code 3 | rows: " + str(len(tatm_code_3)) 
#                    + "/" + str(len(tatm)))
#plt.tight_layout()
#plt.show()
###==============================================================================
### IG
###==============================================================================
##fig = plt.figure(figsize = (8, 6))
##gs2 = gridspec.GridSpec(2, 2)
##
##fig.add_subplot(gs2[0])
##
##n, bins, patches = plt.hist(clean_tatm_ig_2km, normed=1, facecolor='green')
##plt.grid(True)
##plt.title("tatm_ig ALL | rows: " + str(len(clean_tatm_ig_2km)) 
##                    + "/" + str(len(tatm_ig)))
##
###==============================================================================
### Stop code 1
###==============================================================================
##tatm_ig_code_1 = clean_tatm_ig_2km[:]
##to_delete = []
##
##for index, x in enumerate(code):
##    if x !=1:
##      to_delete.append(index)
##
##tatm_ig_code_1 = np.delete(tatm_ig_code_1, to_delete, axis = 0)
###
##fig.add_subplot(gs1[1])
##n, bins, patches = plt.hist(tatm_ig_code_1, normed=1, facecolor='green')
##plt.grid(True)
##plt.title("tatm_ig stop code 1 | rows: " + str(len(tatm_ig_code_1)) 
##                    + "/" + str(len(tatm_ig)))
##
###==============================================================================
### Stop code 2
###==============================================================================
##tatm_ig_code_2 = clean_tatm_ig_2km[:]
##to_delete = []
##
##for index, x in enumerate(code):
##    if x !=2:
##      to_delete.append(index)
##
##tatm_ig_code_2 = np.delete(tatm_ig_code_2, to_delete, axis = 0)
##
###
##fig.add_subplot(gs1[2])
##n, bins, patches = plt.hist(tatm_ig_code_2, normed=1, facecolor='green')
##plt.grid(True)
##plt.title("tatm_ig stop code 2 rows: " + str(len(tatm_ig_code_2)) 
##                    + "/" + str(len(tatm_ig)))
##
##
###==============================================================================
### Stop code 3
###==============================================================================
##tatm_ig_code_3 = clean_tatm_ig_2km[:]
##to_delete = []
##
##for index, x in enumerate(code):
##    if x !=3:
##      to_delete.append(index)
##      
##tatm_ig_code_3 = np.delete(tatm_ig_code_3, to_delete, axis = 0)
##
##
##fig.add_subplot(gs1[3])
##n, bins, patches = plt.hist(tatm_ig_code_3, normed=1, facecolor='green')
##plt.grid(True)
##plt.title("tatm_ig code 3 rows: " + str(len(tatm_ig_code_3)) 
##                    + "/" + str(len(tatm_ig)))
##
##plt.tight_layout()
##plt.show()
##
##nc_fid.close()
##
###
##print "tatm_ig average: " + str(tatm_ig_average)
##print "tatm average: " + str(tatm_average)
##
