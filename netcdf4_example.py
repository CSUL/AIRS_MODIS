

import numpy as np
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/
import matplotlib.pyplot as plt



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

nc_f = '/Users/sevakm/Documents/AIRS_To_Modis/weather/g151/g151.2013.03.02.nc' 
nc_fid = Dataset(nc_f, 'r')  
                             
#nc_attrs, nc_dims, nc_vars = ncdump(nc_fid)
print "----------"

pressure = nc_fid.variables['tatm_layerPressures'][:]

print "shape: " + str(pressure.shape)

for x in pressure: 
    print x
tatm_ig = nc_fid.variables['tatm_ig'][:]
tatm = nc_fid.variables['tatm'][:]



#for x in tatm[r-2]: 
#    print x

#print pressure
#print nc_vars

# Extract data from NetCDF file
#pressure = nc_fid.variables['tatm_layerPressures'][:]  # extract/copy the data











