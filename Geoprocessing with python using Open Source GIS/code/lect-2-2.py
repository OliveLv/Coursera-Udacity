import ogr,os,sys
os.chdir('D:/notes/Open Source GIS/data/ospy_data2')
# get the driver
driver=ogr.GetDriverByName('ESRI Shapefile')

# create a new data source and leyer
if os.path.exists('test.shp'):
	driver.DeleteDataSource('test.shp')
ds=driver.CreateDataSource('test.shp')
if ds is None:
	print 'cannot create the file'
	sys.exit(1)
layer=ds.CreateLayer('test',geom_type=ogr.wkbPoint)

# add an id field to the output
fieldDefn=ogr.FieldDefn('id',ogr.OFTInteger)
layer.CreateField(fieldDefn)

# create a new point object
point=ogr.Geometry(ogr.wkbPoint)
point.AddPoint(150,75)

# get the FeatureDefn for the output layer
featureDefn=layer.GetLayerDefn()

# create a new feature
feature=ogr.Feature(featureDefn)
feature.SetGeometry(point)
feature.SetField('id',1)

# add the feature to the output layer
layer.CreateFeature(feature)

# destroy the geometry and feature and close the data source
point.Destroy()
feature.Destroy()
ds.Destroy()