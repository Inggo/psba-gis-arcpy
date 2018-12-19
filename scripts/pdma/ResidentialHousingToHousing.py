# DEPRECATED, use ReplaceText instead
import arcpy

file = arcpy.GetParameterAsText(0)

mxd = arcpy.mapping.MapDocument(file)

# Update all text elements
for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
	elm.text = elm.text.replace("Residential Housing", "Housing")

mxd.save()
