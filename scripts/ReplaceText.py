import arcpy

# Map document file - usually passed via File Iterator, pass as parameter 0
file = arcpy.GetParameterAsText(0)
# Text to replace - pass as parameter 1
textToReplace = arcpy.GetParameterAsText(1)
# Text to replace with - pass as parameter 2
textToReplaceWith = arcpy.GetParametersAsText(2)

# Open map document
mxd = arcpy.mapping.MapDocument(file)

# Update all text elements
for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
	elm.text = elm.text.replace(textToReplace, textToReplaceWith)

# Save the map document
mxd.save()
