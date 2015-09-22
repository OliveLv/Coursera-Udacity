# script to get pixel values at a set of coordinates
# by reading in one pixel at a time
# Took 0.47 seconds on my machine

import os,sys,time,gdal
from gdalconst import *

# start timing
startTime=time.time()

# coordinates to get pixel values for
xValues=[447520.0,432524.0,451503.0]
yValues=[4631976.0,4608827.0,4648114.0]

# set directory
os.chdir('D:/notes/Open Source GIS/data/ospy_data4')

# register all of the drivers
gdal.AllRegister()

# open the image
ds=gdal.Open('aster.img',GA_ReadOnly)
if ds is None:
	print 'cannot open image'
	sys.exit(1)

# get image size
rows=ds.RasterXSize
cols=ds.RasterYSize
bands=ds.RasterCount

# get georeference info
transform=ds.GetGeoTransform()
xOrigin=transform[0]
yOrigin=transform[3]
pixelWidth=transform[1]
pixelHeight=transform[5]

# loop through the coordinates
for i in range(3):
	
 	# get x,y
 	x=xValues[i]
 	y=yValues[i]
 	
 	# compute pixel offset
 	xOffset=int((x-xOrigin)/pixelWidth)
 	yOffset=int((y-yOrigin)/pixelHeight)
 	
 	# create a string to print out
 	s=str(x)+' '+str(y)+' '+str(xOffset)+' '+str(yOffset)+' '
 	
 	# loop through the bands
 	for j in range(bands):
 		band=ds.GetRasterBand(j+1) # 1-based index
 		# read data and add the value to the string
 		data=band.ReadAsArray(xOffset,yOffset,1,1)
 		value=data[0,0]
 		s+=str(value)+' '
 	# print out the data string 
 	print s
endTime=time.time()
print 'The script took '+str(endTime-startTime)+' seconds'