#!/bin/python
import random
import sys
import numpy as np

if len(sys.argv) != 6:
	print '\nUsage: python generateData.py <lat_min> <lat_max> <lon_min> <lon_max> <num_points>\n'
	print 'Example: python generateData.py 30 37 120 127 50'
	exit(1)
	
lat_min = int(sys.argv[1])
lat_max = int(sys.argv[2])
lon_min = int(sys.argv[3])
lon_max = int(sys.argv[4])
num_points = int(sys.argv[5])
file_name = 'data_file_{}_points.csv'.format(num_points)

print '\nGenerating data...\n'

with open(file_name,'w') as datafile:
	datafile.write("DepLat,DepLon,ArrLat,ArrLon\n")
	for i in range(num_points):
		lats = np.random.uniform(lat_min,lat_max,2)
		lons = np.random.uniform(lon_min,lon_max,2)
		datafile.write("%f,%f,%f,%f\n" % (lats[0],lons[0],lats[1],lons[1]))
		
	
print '%s placed in working directory...\n'	% file_name