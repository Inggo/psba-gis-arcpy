import arcpy

# Map document file - usually passed via File Iterator, pass as parameter 0
file = arcpy.GetParameterAsText(0)
# Layers to hide - pass as string in parameter 1, delimit with pipe (|)
hideLayers = arcpy.GetParameterAsText(1).split("|")
# Layers to show - pass as string in parameter 2, delimit with pipe (|)
showLayers = arcpy.GetParameterAsText(2).split("|")
# Save the output in a different filename (same folder) - pass as string in parameter 3;
# if not set, will overwrite the original file
saveAs = arcpy.GetParameterAsText(3)

# Open map document
mxd = arcpy.mapping.MapDocument(file)

# Loop through all layers
for lyr in arcpy.mapping.ListLayers(mxd):
	# Hide layer if part of show list
	if lyr.name in hideLayers:
		lyr.visible = False
	# Show layer if part of hide list
	elif lyr.name in showLayers:
		lyr.visible = True

# Save the map document
if saveAs:
	mxd.saveACopy(saveAs)
else:
	mxd.save()
