# write polygons to a shapefile

# create a new polygon shapefile and populate it with the polygons defined in ut_counties.txt
# each line in the file looks like : county_name:x1 y1,x2 y2,...,xn yn where x1=xn and y1=yn

import ogr,os,sys
os.chdir('D:/notes/Open Source GIS/data/ospy_data2')
driver=ogr.GetDriverByName('ESRI Shapefile')
# read file ut_countries.txt
fn='ut_counties.txt'
reader=open(fn,'r')
# create a new data source and layer with geom_type= xxxxPolygon
fn='assignment2a_res.shp'
if os.path.exists(fn):
	driver.DeleteDataSource(fn)
ds=driver.CreateDataSource(fn)
if ds is None:
	print 'cannot create this file'
	sys.exit(1)
layer=ds.CreateLayer('test',geom_type=ogr.wkbPolygon)

# create a field called 'name' to layer
fieldDefn=ogr.FieldDefn('name',ogr.OFTString)
layer.CreateField(fieldDefn)

# get featureDefn object from layer
featureDefn=layer.GetLayerDefn()

for line in reader:
	form=line.split(':')
	if len(form)!=2:
		continue
	name,points=form
	coords=points.split(',')
	# create polygon, polygon can contain many rings,each ring may have many points
	polygon=ogr.Geometry(ogr.wkbPolygon)
	# creat a ring
	ring=ogr.Geometry(ogr.wkbLinearRing)
	for coord in coords:
		xy=coord.split(' ')
		x=float(xy[0])
		y=float(xy[1])
		ring.AddPoint(x,y)
	polygon.AddGeometry(ring)
	# create a new feature
	feature=ogr.Feature(featureDefn)
	# set feature's geometry
	feature.SetGeometry(polygon)
	# set attribute id in feature
	feature.SetField('name',str(name))
	# write feature to layer
	layer.CreateFeature(feature)
	ring.Destroy()
	polygon.Destroy()
	feature.Destroy()
reader.close()
ds.Destroy()

# read result
fn='assignment2a_res.shp'
ds=driver.Open(fn,0)
if ds is None:
	print 'cannot open the file'
	sys.exit(1)
layer=ds.GetLayer()
feature=layer.GetNextFeature()
while feature:
	id=feature.GetField('name')
	s=str(id)
	geometry=feature.GetGeometryRef()
	ring=geometry.GetGeometryRef(0)
	num=ring.GetPointCount()
	print id,ring.GetX(0),ring.GetY(0),ring.GetX(num-1),ring.GetY(num-1)
#	for i in range(0,num):
#		x=ring.GetX(i)
#		y=ring.GetY(i)
#		s=s+" "+str(x)+" "+str(y)
#	print s
	feature.Destroy()
	feature=layer.GetNextFeature()
ds.Destroy()
 