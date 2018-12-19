import arcpy

# Open current MXD file, get district name parameter
mxd = arcpy.mapping.MapDocument("CURRENT")
districtName = arcpy.GetParameterAsText(0)
oldDistrictName = arcpy.GetParameterAsText(1)

# Update Definition Query of Union Council Boundary
for lyr in arcpy.mapping.ListLayers(mxd, "Union Council Boundary"):
	lyr.definitionQuery = lyr.definitionQuery.replace(oldDistrictName.upper(), districtName.upper())
	arcpy.AddMessage("Layer name: " + lyr.name)
	for lblClass in lyr.labelClasses:
		lblClass.expression = '"{}" + [_1__Field1] +  "{}"'.format("<FNT size = '5'>","</FNT>")

mxd.save()
		
arcpy.RefreshActiveView()
