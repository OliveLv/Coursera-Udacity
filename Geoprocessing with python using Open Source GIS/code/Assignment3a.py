# use filters and buffers

# use an attribute filter to restrict cache_towns.shp to Nibley("name" field)
# buffer the Nibley geometry by 1500
# use the new geometry with a spatial filter on sites.shp to find all sites within 1500 meters of Nibley
# print out the "id" value for those sites
import os,ogr,sys

# set the working directory
os.chdir('D:/notes/Open Source GIS/data/ospy3_data')

# get the shapefile driver
driver=ogr.GetDriverByName('ESRI Shapefile')

# open cache_towns.shp and get the layer
fn='cache_towns.shp'
townDS=driver.Open(fn,0)
if townDS is None:
	print 'can open the file'
	sys.exit(1)
townLayer=townDS.GetLayer()


# use an attribute filter to restrict cache_towns.shp to "Nibley"
townLayer.SetAttributeFilter("name='Nibley'")


# get the Nibley geometry and buffer it by 1500
nibleyFeature=townLayer.GetNextFeature()
nibleyGeom=nibleyFeature.GetGeometryRef()
bufferGeom=nibleyGeom.Buffer(1500)
nibleyFeature.Destroy()

# open sites.shp and get the layer
fn='sites.shp'
sitesDS=driver.Open(fn,0)
if sitesDS is None:
	print 'can open the file'
	sys.exit(1)
sitesLayer=sitesDS.GetLayer()

# use a spatial filter on sites.shp to get all sites
# within 1500 meters of Nibley
sitesLayer.SetSpatialFilter(bufferGeom)

# loop through the remaining features in sites.shp and print their id values
feature=sitesLayer.GetNextFeature()
while feature:
	#geom=feature.GetGeometryRef()
	id=feature.GetField('id')
	print id
	feature.Destroy()
	feature=sitesLayer.GetNextFeature()

# close the shapefiles
sitesDS.Destroy()
townDS.Destroy()
