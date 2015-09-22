import gdal,osr,os
from gdalconst import *

os.chdir('D:/notes/Open Source GIS/data/ospy_data6')

inFn='aster.img'
outFn='aster_geo.img'

driver=gdal.GetDriverByName('HFA')
driver.Register()

# input wkt
inDS=gdal.Open(inFn)
inWkt=inDS.GetProjection()

# output wkt
outSr=osr.SpatialReference()
outSr.ImportFromEPSG(4326)
outWkt=outSr.ExportToWkt()

# reproject
gdal.CreateAndReprojectImage(inDS,outFn,src_wkt=inWkt,dst_wkt=outWkt,dst_driver=driver,eResampleAlg=GRA_Bilinear)

inDS=None