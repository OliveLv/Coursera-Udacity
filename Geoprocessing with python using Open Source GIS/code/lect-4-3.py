# script to count the number of non-zero pixels in the first band

import os,sys,ogr,gdal,Numeric
from gdalconst import *

sys.path.append('D:/notes/Open Source GIS/data/ospy_data4')
os.chdir('D:/notes/Open Source GIS/data/ospy_data4')
import utils
# register all of the GDAL drivers
gdal.AllRegister()

# open the image aster.img
ds=gdal.Open('aster.img',GA_ReadOnly)
if ds is None:
	print 'cannot open the file','aster.img'
	sys.exit(1)

# get image size
rows=ds.RasterXSize
cols=ds.RasterYSize
bands=ds.RasterCount

# get the band 1 and block sizes
band=ds.GetRasterBand(1)
blockSize=utils.GetBlockSize(band)
xBlockSize=blockSize[0]
yBlockSize=blockSize[1]

# initialize variable
count=0

# loop through the rows
for i in range(0,rows,xBlockSize):
	if i+xBlockSize>=rows:
		rowNum=rows-i
	else:
		rowNum=xBlockSize
	# loop through the colums
	for j in range(0,cols,yBlockSize):
		if j+yBlockSize>=cols:
			colNum=cols-j
		else:
			colNum=yBlockSize
		# read the data and do the calculations
		data=band.ReadAsArray(i,j,rowNum,colNum)
		count+=Numeric.sum(Numeric.sum(Numeric.greater(data,0)))
# print results
print count