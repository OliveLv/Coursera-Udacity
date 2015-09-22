# a script that imports the new module and uses the function to reproject all of the shapefiles
# in this week's data
# go from EPSG 26912 to EPSG 4269
import Assignment3b,os
#os.chdir('D:/notes/Open Source GIS/code')
Assignment3b.ProjectShapefile('cache_towns.shp','cache_towns_res.shp',26912,4269)