import ogr,sys,os

# projections
# getting a layer's projection
#   layer.GetSpatialRef()
#   geom.GetSpatialReference()

# creating a new projection
import osr
  # create an empty SpatialReference object
spatialRef=osr.SpatialReference()
  # import projection information
spatialRef.ImportFromEPSG(32612)

# projecting a geometry
sourceSR=osr.SpatialReference()
sourceSR.ImportFromEPSG(32612)
targetSR=osr.SpatialReference()
targetSR.ImportFromEPSG(4326)
coordTrans=osr.CoordinateTransformation(sourceSR,targetSR)
  # geom.Transform(coordTrans)

# example
import ogr,osr,os
os.chdir('D:/notes/Open Source GIS/data/ospy_data1')
driver=ogr.GetDriverByName('ESRI Shapefile')
dataset=driver.Open('test.shp')
layer=dataset.GetLayer()
feature=layer.GetNextFeature()
geom=feature.GetGeometryRef()
print geom.GetX(),geom.GetY()
geoSR=osr.SpatialReference()
# unprojected WGS84
geoSR.ImportFromEPSG(4326)
utmSR=osr.SpatialReference()
# UTM 12N WGS84
utmSR.ImportFromEPSG(32612)
coordTrans=osr.CoordinateTransformation(geoSR,utmSR)
geom.Transform(coordTrans)
print geom.GetX(),geom.GetY()