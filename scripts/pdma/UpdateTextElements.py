# DEPRECATED, use ReplaceText instead
import arcpy

# Open current MXD file, get district name parameter
mxd = arcpy.mapping.MapDocument("CURRENT")
districtName = arcpy.GetParameterAsText(0)
oldDistrictName = arcpy.GetParameterAsText(1)

# Update all text elements
for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
	elm.text = elm.text.replace(oldDistrictName, districtName) 

mxd.save()