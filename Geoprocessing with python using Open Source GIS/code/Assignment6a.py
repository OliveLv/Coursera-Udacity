# use a 3x3 high pass filter to detect edges in band 1 of smallaster.img
# the output data type will be Float
# use pixel notation

import osr,gdal,ogr,sys,os,Numeric
from gdalconst import *

os.chdir('D:/notes/Open Source GIS/data/ospy_data6')

gdal.AllRegister()
ds=gdal.Open('smallaster.img',GA_ReadOnly)
if ds is None:
	print 'cannot open file smallaster.img'
	sys.exit(1)
#
rows=ds.RasterXSize
cols=ds.RasterYSize
bands=ds.RasterCount

#
band=ds.GetRasterBand(1)
# data is an array,not a matrix
data=band.ReadAsArray(0,0,rows,cols).astype(Numeric.Float)
outData=Numeric.zeros((cols,rows),Numeric.Float)
for j in range(1,rows-1):
	for i in range(1,cols-1):
		# use pixel notation
		outData[i,j]=-0.7*data[i-1,j-1]-data[i-1,j]-0.7*data[i-1,j+1]-0.7*data[i,j-1]+6.8*data[i,j]-0.7*data[i,j+1]-0.7*data[i+1,j-1]-data[i+1,j]-0.7*data[i+1,j+1];
# use slice
#outData[1:rows-1,1:cols-1]=(-0.7*data[0:rows-2,0:cols-2]-data[0:rows-2,1:cols-1]-0.7*data[0:rows-2,2:cols]-data[1:rows-1,0:cols-2]+6.8*data[1:rows-1,1:cols-1]-data[1:rows-1,2:cols]-0.7*data[2:rows,0:cols-2]-data[2:rows,1:cols-1]-0.7*data[2:rows,2:cols])

driver=ds.GetDriver()
outDS=driver.Create('assignment6a_res.img',rows,cols,1)
if outDS is None:
	print 'cannot create file assignment6a_res.img'
	sys.exit(1)
outBand=outDS.GetRasterBand(1)
outBand.WriteArray(outData,0,0)

outBand.FlushCache()
outBand.GetStatistics(0,1)

outDS.SetGeoTransform(ds.GetGeoTransform())
outDS.SetProjection(ds.GetProjection())

ds=None
outDS=None
