# a script to calculate the average pixel value for the first band in aster.img
# Read in the data one block at a time
# Do the calculation two ways
# including zeros in the calculation
# ignoring zeros in the calculation

import sys,os,ogr,gdal,Numeric
from gdalconst import *

sys.path.append('D:/notes/Open Source GIS/data/ospy_data4')
import utils

# change working directory
os.chdir('D:/notes/Open Source GIS/data/ospy_data4')

# register all of the GDAL drivers
gdal.AllRegister()

# open the image
ds=gdal.Open('aster.img',GA_ReadOnly)
if ds is None:
	print 'cannot open the file'
	sys.exit(1)
	
# get image size
rows=ds.RasterXSize
cols=ds.RasterYSize
band=ds.RasterCount

# get the first band and block sizes
band=ds.GetRasterBand(1)
blockSize=utils.GetBlockSize(band)
xBlockSize=blockSize[0]
yBlockSize=blockSize[1]

# initialize variables
count=0
# num of pixels,ignoring zeros
ncount=0
# sum of pixel values
sum=0

# loop through the rows
for i in range(0,rows,xBlockSize):
	if i+xBlockSize<rows:
		rowNum=xBlockSize
	else:
		rowNum=rows-i
	# loop through the columns
	for j in range(0,cols,yBlockSize):
		if j+yBlockSize<cols:
			colNum=yBlockSize
		else:
			colNum=cols-j
		# read the data and do the calculations
		# change data type to float
		data=band.ReadAsArray(i,j,rowNum,colNum).astype(Numeric.Float)
		mask=Numeric.greater(data,0)
		sum+=Numeric.sum(Numeric.sum(data))
		ncount+=Numeric.sum(Numeric.sum(mask))
# num of pixels,including zeros 
count=rows*cols
# print results
print float(sum)/ncount,float(sum)/count