# Create an NDVI image
#  read in data from aster.img
#  create an NDVI image
#  write out NDVI to new file

# can do entire image at once or block by block 
# calculate statistics,set projection and georeferencing information,and build pyramids

import Numeric,ogr,os,sys,gdal
from gdalconst import *

sys.path.append('D:/notes/Open Source GIS/data/ospy_data5')
import utils

# change the working directory
os.chdir('D:/notes/Open Source GIS/data/ospy_data5')
# read data

# register all driver
gdal.AllRegister()

ds=gdal.Open('aster.img',GA_ReadOnly)
if ds is None:
	print 'cannot open the file'
	sys.exit(1)

# get image size
rows=ds.RasterXSize
cols=ds.RasterYSize
bands=ds.RasterCount

# create a new image
driver=ds.GetDriver()
outDS=driver.Create('assignment5a_res.img',rows,cols,1,GDT_Float32)
if outDS is None:
	print 'cannot create file assignment5a_res.img'
	sys.exit(1)
band=outDS.GetRasterBand(1)

# get band 2 and band 3,
# get blocksize
band2=ds.GetRasterBand(2)
band3=ds.GetRasterBand(3)
blockSize=utils.GetBlockSize(band2)
xBlockSize=blockSize[0]
yBlockSize=blockSize[1]

# calculate NDVI and write it to band
for r in range(0,rows,xBlockSize):
	if r+xBlockSize<rows:
		numRow=xBlockSize
	else:
		numRow=rows-r
	for c in range(0,cols,yBlockSize):
		if c+yBlockSize<cols:
			numCol=yBlockSize
		else:	
			numCol=cols-c
		data2=band2.ReadAsArray(r,c,numRow,numCol).astype(Numeric.Float16)
		data3=band3.ReadAsArray(r,c,numRow,numCol).astype(Numeric.Float16)
		
		# do the calculations
		mask=Numeric.greater(data2+data3,0)
		ndvi=Numeric.choose(mask,(-99,(data3-data2)/(data3+data2)))
		
		# write the data
		band.WriteArray(ndvi,r,c)

# flush data to disk
band.FlushCache()
# set the NoData value 
band.SetNoDataValue(-99)
# calculate stats
stats=band.GetStatistics(0,1)
		
# set projection and georeferencing information
proj=ds.GetProjection()
outDS.SetProjection(proj)
geoinfo=ds.GetGeoTransform()
outDS.SetGeoTransform(geoinfo)

# building pyramids
gdal.SetConfigOption('HFA_USE_RDD','YES')
outDS.BuildOverviews(overviewlist=[2,4,8,16,32,64,128])

# gdal not using method destory(),while set the variables to 'None'
ds=None
outDS=None
