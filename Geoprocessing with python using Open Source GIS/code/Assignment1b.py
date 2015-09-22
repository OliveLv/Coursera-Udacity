# copy selected feature from one shapefile to another

# create a new point shapefile and add an ID field
# loop through the points in sites.shp
#   if the cover attribute for a point is 'tree' then write that point out to new shapefile

import ogr,os,sys

os.chdir('D:/notes/Open Source GIS/data/ospy_data1')
driver=ogr.GetDriverByName('ESRI Shapefile')
fn='sites.shp'
inDS=driver.Open(fn,0)
if inDS is None:
	print 'cannot open this file'
	sys.exit(1)
inLayer=inDS.GetLayer()


out='assignment_res.shp'
if os.path.exists(out):
	driver.DeleteDataSource(out)
# create a new shapefile
outDS=driver.CreateDataSource(out)
if outDS is None:
	print 'cannot create the file'
	sys.exit(1)
# create a new point layer
outLayer=outDS.CreateLayer('test',geom_type=ogr.wkbPoint)

# add an ID field
fieldDefn=inLayer.GetFeature(0).GetFieldDefnRef('id')
outLayer.CreateField(fieldDefn)

# get layer's FeatureDefn object
featureDefn=outLayer.GetLayerDefn()
inFeature=inLayer.GetNextFeature()
while inFeature:
	cover=inFeature.GetFieldAsString('cover')
	if cover=='trees':
	    # create a new feature use FeatureDefn object
		outFeature=ogr.Feature(featureDefn)
		outFeature.SetGeometry(inFeature.GetGeometryRef())
		outFeature.SetField('id',inFeature.GetField('id'))
		
		# write the feature to the layer
		outLayer.CreateFeature(outFeature)
		
		outFeature.Destroy()
	inFeature.Destroy()
	inFeature=inLayer.GetNextFeature()
inDS.Destroy()
outDS.Destroy()

# read result data
print 'id','x','y'
fn='assignment_res.shp'
ds=driver.Open(fn)
layer=ds.GetLayer()
feature=layer.GetNextFeature()
while feature:
	id=feature.GetFieldAsString('id')
	geometry=feature.GetGeometryRef()
	x=geometry.GetX()
	y=geometry.GetY()
	print id,x,y
	feature.Destroy()
	feature=layer.GetNextFeature()
ds.Destroy()
	

