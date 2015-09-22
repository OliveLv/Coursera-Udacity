# Read pixel values from an image

# print out the pixel values from all three bands of
# aster.img at the points contained in sites.shp

import ogr,sys,os,gdal,time
from gdalconst import *

os.chdir('D:/notes/Open Source GIS/data/ospy_data4')

# get start time
startTime=time.time()

# read sites.shp and get the layer
fn='sites.shp'
driver=ogr.GetDriverByName('ESRI Shapefile')
sitesDS=driver.Open(fn)
if sitesDS is None:
	print 'cannot open file',fn
	sys.exit(1)
sitesLayer=sitesDS.GetLayer()

# read aster.img and get bands?
gdal.AllRegister()
ds=gdal.Open('aster.img',GA_ReadOnly)
if ds is None:
	print 'cannot open the file','aster.img'
	sys.exit(1)

# getting image dimensions
cols=ds.RasterXSize
rows=ds.RasterYSize
bands=ds.RasterCount

# getting georeference info
transforms=ds.GetGeoTransform()
xOrigin=transforms[0]
yOrigin=transforms[3]
pixelWidth=transforms[1]
pixelHeight=transforms[5]

# getting bandlist
bandList=[]
for i in range(bands):
	band=ds.GetRasterBand(i+1)
	data=band.ReadAsArray(0,0,cols,rows)
	bandList.append(data)

#geomType=sitesLayer.GetLayerDefn().GetGeomType()
#print geomType
sitesFeature=sitesLayer.GetNextFeature()
while sitesFeature:
	geom=sitesFeature.GetGeometryRef()
	x=geom.GetX()
	y=geom.GetY()
	xOffset=int((x-xOrigin)/pixelWidth)
	yOffset=int((y-yOrigin)/pixelHeight)
	s=str(x)+' '+str(y)+' '+str(xOffset)+' '+str(yOffset)+' '
	print s
	if xOffset not in range(rows) or yOffset not in range(cols):
		sitesFeature.Destroy()
		sitesFeature=sitesLayer.GetNextFeature()
		continue
	for i in range(bands):
		data=bandList[i]
		s+=str(data[yOffset,xOffset])+' '
	print s
	sitesFeature.Destroy()
	sitesFeature=sitesLayer.GetNextFeature()
sitesDS.Destroy()

# get end time
endTime=time.time()
print 'It took ',endTime-startTime,'seconds'	