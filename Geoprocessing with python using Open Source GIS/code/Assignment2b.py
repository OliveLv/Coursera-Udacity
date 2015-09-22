# Reproject a shapefile

# create a new polygon shapefile
# loop through the polygons in ut_counties.shp,reproject each one,and write it
# out to the new shapefile
# go from EPSG 4269 to EPSG 26912
import ogr,osr,os,sys
os.chdir('D:/notes/Open Source GIS/data/ospy_data2')
driver=ogr.GetDriverByName('ESRI Shapefile')
# get in datasource and layer
inDS=driver.Open('ut_counties.shp',0)
if inDS is None:
	print 'cannot open this file'
	sys.exit(1)
inLayer=inDS.GetLayer()

# create a new shp and layer
fn='assignment2b_res.shp'
if os.path.exists(fn):
	driver.DeleteDataSource(fn)
outDS=driver.CreateDataSource(fn)
if outDS is None:
	print 'cannot create the file'
	sys.exit(1)
outLayer=outDS.CreateLayer('test',geom_type=ogr.wkbPolygon)

# define a new field
fieldDefn=ogr.FieldDefn('id',ogr.OFTInteger)
# get a field define from other layer
# feature=inLayer.GetFeature(0)
# fieldDefn=feature.GetFieldDefnRef('name')
# create a new field
outLayer.CreateField(fieldDefn)

# get feature define 
featureDefn=outLayer.GetLayerDefn()

# get in feature
inFeature=inLayer.GetNextFeature()

# create coordinate transformation
sourceSR=osr.SpatialReference()
sourceSR.ImportFromEPSG(4269)
targetSR=osr.SpatialReference()
targetSR.ImportFromEPSG(26912)
coordTrans=osr.CoordinateTransformation(sourceSR,targetSR)


while inFeature:
	geom=inFeature.GetGeometryRef()
	geom.Transform(coordTrans)
	outFeature=ogr.Feature(featureDefn)
	outFeature.SetGeometry(geom)
	outLayer.CreateFeature(outFeature)
	outFeature.Destroy()
	inFeature.Destroy()
	inFeature=inLayer.GetNextFeature()
inDS.Destroy()
outDS.Destroy()

# create the shapefiles
targetSR.MorphToESRI()
file=open('assinment2b_res.prj','w')
file.write(targetSR.ExportToWkt())
file.close()


# read result
fn='assignment2b_res.shp'
ds=driver.Open(fn,0)
if ds is None:
	print 'cannot open the file'
	sys.exit(1)
layer=ds.GetLayer()
feature=layer.GetNextFeature()
while feature:
	geometry=feature.GetGeometryRef()
	ring=geometry.GetGeometryRef(0)
	num=ring.GetPointCount()
	#print ring.GetX(0),ring.GetY(0),ring.GetX(num-1),ring.GetY(num-1)
#	for i in range(0,num):
#		x=ring.GetX(i)
#		y=ring.GetY(i)
#		s=s+" "+str(x)+" "+str(y)
#	print s
	feature.Destroy()
	feature=layer.GetNextFeature()
ds.Destroy()