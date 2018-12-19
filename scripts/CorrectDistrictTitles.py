import arcpy

# Map document file - usually passed via File Iterator, pass as parameter 0
file = arcpy.GetParameterAsText(0)
# District name - pass as string in parameter 1
districtName = arcpy.GetParameterAsText(1)

# Open map document
mxd = arcpy.mapping.MapDocument(file)

# Update all text elements
for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
	elm.text = elm.text.replace("District " + districtName, districtName + " District")

# Save the map document
mxd.save()
