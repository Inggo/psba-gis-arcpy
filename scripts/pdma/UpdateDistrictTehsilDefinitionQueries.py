import arcpy

# Open current MXD file, get district name parameter
mxd = arcpy.mapping.MapDocument("CURRENT")
districtName = arcpy.GetParameterAsText(0)
oldDistrictName = arcpy.GetParameterAsText(1)

# Update Definition Queries of District, Tehsil Boundary layers
for lyr in (arcpy.mapping.ListLayers(mxd, "Tehsil Boundary") + arcpy.mapping.ListLayers(mxd, "District Boundary")):
	lyr.definitionQuery = lyr.definitionQuery.replace(oldDistrictName, districtName)
	
mxd.save()
		
arcpy.RefreshActiveView()

