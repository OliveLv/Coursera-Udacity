try:
	from osgeo import ogr
except:
	import ogr
import sys,os

# getting a writeable layer
os.chdir('D:/notes/Open Source GIS/data/ospy_data1')
driver=ogr.GetDriverByName('ESRI Shapefile')
fn='sites.shp'
dataSource=driver.Open(fn,0)
if dataSource is None:
	print 'cannot open',fn
	sys.exit(1)
layer=dataSource.GetLayer()
dataSource.Destroy()

# creating a writeable layer
# checking if the datasource exists
fn='test.shp'
if os.path.exists(fn):
	driver.DeleteDataSource(fn)
# create a new datasource
ds=driver.CreateDataSource(fn)
layer=ds.CreateLayer('test',geom_type=ogr.wkbPoint)

# adding fields



# creating new features
# get a FeatureDefn object 
featureDefn=layer.GetLayerDefn()
# create a new feature
feature=ogr.Feature(featureDefn)
# set the geometry for new feature
# feature.SetGeometry(point)
# set the attributes with SetField
feature.SetField('id',23)
# write the feature to layer
layer.CreateFeature(feature)
