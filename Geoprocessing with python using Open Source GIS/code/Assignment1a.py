# Read coordinates and attributes from a shapefile

# loop through the points in sites.shp
#  write out id,x&y coordinates,and cover type for each point to a text file ,one point per line

try:
	from osgeo import ogr
except:
	import ogr
import ogr,os,sys
os.chdir('D:/notes/Open Source GIS/data/ospy_data1')
driver=ogr.GetDriverByName('ESRI Shapefile')
fn='sites.shp'
dataSource=driver.Open(fn,0)
output='assignment1a_res.txt'
file=open(output,'w')
if dataSource is None:
	print 'cannot open',fn
	sys.exit(1)
layer=dataSource.GetLayer()
feature=layer.GetNextFeature()
while feature:
	id = feature.GetField('id')
	cover=feature.GetField('cover')
	geometry=feature.GetGeometryRef()
	x=geometry.GetX()
	y=geometry.GetY()
	s=str(id)+","+str(x)+"&"+str(y)+","+str(cover)+"\n"
	file.write(s)
	#print id,x,y,cover
	feature.Destroy()
	feature=layer.GetNextFeature()
dataSource.Destroy()
file.close()