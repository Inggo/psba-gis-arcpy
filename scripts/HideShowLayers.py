import arcpy

# Map document file - usually passed via File Iterator, pass as parameter 0
file = arcpy.GetParameterAsText(0)
# Layers to hide - pass as string in parameter 1, delimit with pipe (|)
hideLayers = arcpy.GetParameterAsText(1).split("|")
# Layers to show - pass as string in parameter 2, delimit with pipe (|)
showLayers = arcpy.GetParameterAsText(2).split("|")

# Open map document
mxd = arcpy.mapping.MapDocument(file)

# Loop through all layers
for lyr in arcpy.mapping.ListLayers(mxd):
	# Hide layer if part of show list
	if lyr.name in hideLayers:
		lyr.visible = false
	# Show layer if part of hide list
	elif lyr.name in showLayers:
		lyr.visible = true

# Save the map document
mxd.save()
