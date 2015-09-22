# write a function to reproject a shapefile using EPSG codes

# user should pass in the input&output filenames and input&output EPSG codes
# put the function in a module

import ogr,osr,sys,os

def ProjectShapefile(inFN,outFN,inEPSG,outEPSG):
	inSR=osr.SpatialReference()
	inSR.ImportFromEPSG(inEPSG)
	outSR=osr.SpatialReference()
	outSR.ImportFromEPSG(outEPSG)
	coordTrans=osr.CoordinateTransformation(inSR,outSR)
	os.chdir('D:/notes/Open Source GIS/data/ospy3_data')
	driver=ogr.GetDriverByName('ESRI Shapefile')
	
	inDS=driver.Open(inFN)
	if inDS is None:
		print 'cannot open the file'
		return ;
	inLayer=inDS.GetLayer()
	geomType=inLayer.GetLayerDefn().GetGeomType()
	inFeature=inLayer.GetFeature(0)
	
	if os.path.exists(outFN):
		driver.DeleteDataSource(outFN)
	outDS=driver.CreateDataSource(outFN)
	if outDS is None:
		print 'cannot create this file'
		return ;
	outLayer=outDS.CreateLayer('test',geom_type=geomType)
	
	# create new fieldDefn to outLayer
	nField=inFeature.GetFieldCount()
	for idx in range(0,nField):
		fieldDefn=inFeature.GetFieldDefnRef(idx)
		outLayer.CreateField(fieldDefn)
		
	featureDefn=outLayer.GetLayerDefn()
	
	inFeature=inLayer.GetNextFeature()
	while inFeature:
		geom=inFeature.GetGeometryRef()
		geom.Transform(coordTrans)
		outFeature=ogr.Feature(featureDefn)
		outFeature.SetGeometry(geom)
		for i in range(0,nField):
			outFeature.SetField(i,inFeature.GetField(i))
		outLayer.CreateFeature(outFeature)
		outFeature.Destroy()
		inFeature.Destroy()
		inFeature=inLayer.GetNextFeature()
	inDS.Destroy()
	outDS.Destroy()
	
	# create the .poj file
	outSR.MorphToESRI()
	file=open(outFN.replace('.shp','.prj'),'w')
	file.write(outSR.ExportToWkt())
	file.close()

	