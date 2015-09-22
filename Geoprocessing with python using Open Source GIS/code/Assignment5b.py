# Mosaic doq1.img and doq2.img together
# the pixel sizes are the same for both images
# read in each image all at once - that will make it easier
# if you display it in ArcMap,change the symbology so it dosen't stretch the data and it 
# look better

import sys,os,ogr,Numeric,gdal
from gdalconst import *
sys.path.append('D:/notes/Open Source GIS/data/ospy_data5')
import utils

# change working directory
os.chdir('D:/notes/Open Source GIS/data/ospy_data5')

# register all driver
gdal.AllRegister()

# open imges
ds1=gdal.Open('doq1.img',GA_ReadOnly)
if ds1 is None:
	print 'cannot open the file doq1.img'
	sys.exit(1)
ds2=gdal.Open('doq2.img',GA_ReadOnly)
if ds2 is None:
	print 'cannot open the file doq2.img'
	sys.exit(1)

# get image size
rows1=ds1.RasterXSize
cols1=ds1.RasterYSize
bands1=ds1.RasterCount

rows2=ds2.RasterXSize
cols2=ds2.RasterYSize
bands2=ds2.RasterCount

# get georeference information
transform1=ds1.GetGeoTransform()
pixelWidth1=transform1[1]
pixelHeight1=transform1[5]
minX1=transform1[0]
maxY1=transform1[3]
maxX1=minX1+(cols1*pixelWidth1)
minY1=maxY1+(rows1*pixelHeight1)

transform2=ds2.GetGeoTransform()
pixelWidth2=transform2[1]
pixelHeight2=transform2[5]
minX2=transform2[0]
maxY2=transform2[3]
maxX2=minX2+(cols2*pixelWidth2)
minY2=maxY2+(rows2*pixelHeight2)

# get the corner coordinates for the output
minX=min(minX1,minX2)
maxX=max(maxX1,maxX2)
minY=min(minY1,minY2)
maxY=max(maxY1,maxY2)

# get the number of rows and cols for the output
rows=int((maxX-minX)/pixelWidth1)
cols=int((maxY-minY)/abs(pixelHeight1))

# create output file,get out band
driver=ds1.GetDriver()
outDS=driver.Create('assignment5b_res.img',rows,cols,1)
outBand=outDS.GetRasterBand(1)

# compute the origin(upper left) offset for doq1
xOffset1=int((minX1-minX)/pixelWidth1)
yOffset1=int((maxY1-maxY)/pixelHeight1)
# get doq1 whole data
band1=ds1.GetRasterBand(1)
# write doq1 data to output
data1=band1.ReadAsArray(0,0,rows2,cols2)
outBand.WriteArray(data1,xOffset1,yOffset1)

# comput the origin(upper left) offset for doq2
xOffset2=int((minX2-minX)/pixelWidth1)
yOffset2=int((maxY2-maxY)/pixelHeight1)
# get doq2 whole data
band2=ds2.GetRasterBand(1)
# write doq2 data to output 
data2=band2.ReadAsArray(0,0,rows2,cols2)
outBand.WriteArray(data2,xOffset2,yOffset2)

# compute statistics for the output
outBand.FlushCache()
stats=outBand.GetStatistics(0,1)

# set the geotransform and projection on the output
geotransform=[minX,pixelWidth1,0,maxY,0,pixelHeight1]
outDS.SetGeoTransform(geotransform)
outDS.SetProjection(ds1.GetProjection())

# building pyromids
gdal.SetConfigOption('HFA_USE_RDD','YES')
outDS.BuildOverviews(overviewlist=[2,4,8,16])

ds1=None
ds2=None
outDS=None