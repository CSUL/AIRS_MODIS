

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
granule = nc_fid.variables['granule'][:]

#print collections.Counter(granule)

scanline = nc_fid.variables['track'][:]
footprint = nc_fid.variables['xTrack'][:]



#print "min: " + str(np.min(footprint))
#print "max: " + str(np.max(footprint))
#print "Shape: " + str(scanline.shape)
##
#arr = np.array([[1, 2, 3, 4, 5],
#       [6, 7, 8, 9, 10]])
#
#test = [2, 3, 4, 5]
#
#
#print test
#print arr[0]
#
#
#
#if test in arr[:, 1:arr.shape[1]].tolist():
#    print 'yep'
#else:
#    print 'nope'
#



index_path  = '/Users/sevakm/Documents/AIRS_To_Modis/index_summary.npy'
indices = np.load(index_path)#indexes for scanline and 

import pandas as pd

df = pd.DataFrame(indices,columns=['c1','c2','c3'])
print df.groupby(['c1','c2','c3']).size()













