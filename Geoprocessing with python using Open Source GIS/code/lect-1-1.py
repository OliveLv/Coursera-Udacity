try:
	from osgeo import ogr
except:
	import ogr
import ogr,os,sys

# setting working directory
os.chdir('D:/notes/Open Source GIS/data/ospy_data1/')

# getting driver 'ESRI Shapefile' so it can use this data driver to read .shp file
driver=ogr.GetDriverByName('ESRI Shapefile')

# opening a DataSource
fn='sites.shp'
dataSource=driver.Open(fn,0)
if dataSource is None:
	print 'Could not open '+fn
	sys.exit(1)
else:
	print 'success'

# opening a layer
layer=dataSource.GetLayer()

# getting info about the layer
# loog through the features and count them
cnt=0
feature=layer.GetNextFeature()
while feature:
	cnt+=1
	feature.Destroy()
	feature=layer.GetNextFeature()
print 'There are',cnt,'features'

# get the number of features in the layer
numFeatures=layer.GetFeatureCount()
print 'Feature count: ',numFeatures
# get the extent as a tuple
extent=layer.GetExtent()
print 'Extent:',extent
print 'UL:',extent[0],extent[3]
print 'LR:',extent[1],extent[2]

# getting features
feature=layer.GetFeature(0)

# getting a feature's attributes
id = feature.GetField('id')
print id
# get attributes using GetFieldAsXXX XXX=String,Integer and so on
id =feature.GetFieldAsString('id')
print id

# getting a feature's geometry
geometry=feature.GetGeometryRef()
x=geometry.GetX()
y=geometry.GetY()
print x,"\t",y

# Destroying objects
feature.Destroy()
dataSource.Destroy()


