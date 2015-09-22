import ogr
# creating points
point=ogr.Geometry(ogr.wkbPoint)
point.AddPoint(10,20)

# creating lines
line=ogr.Geometry(ogr.wkbLineString)
line.AddPoint(10,10)
line.AddPoint(20,20)
line.SetPoint(0,30,30)
print line.GetPointCount()
print line.GetX(0)
print line.GetY(0)

# creating polygons
outring=ogr.Geometry(ogr.wkbLinearRing)
outring.AddPoint(0,0)
outring.AddPoint(100,0)
outring.AddPoint(100,100)
outring.AddPoint(0,100)
outring.AddPoint(0,0)

inring=ogr.Geometry(ogr.wkbLinearRing)
inring.AddPoint(25,25)
inring.AddPoint(25,75)
inring.AddPoint(75,75)
inring.AddPoint(25,75)
inring.CloseRings

polygon=ogr.Geometry(ogr.wkbPolygon)
polygon.AddGeometry(outring)
polygon.AddGeometry(inring)
print polygon.GEtGeometryCount()

# get a ring object from a polygon with method GetGeometryRef(index)
# outring=polygon.GetGeometryRef(0)
# inring=polygon.GetGeometryRef(1)

# multi Geometries
multipoint=ogr.Geometry(ogr.wkbMultiPoint)
point=ogr.Geometry(ogr.wkbPoint)
point.AddPoint(10,10)
multipoint.AddGeometry(point)
point.AddPoint(20,20)
multipoint.AddGeometry(point)