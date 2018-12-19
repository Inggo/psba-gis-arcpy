import arcpy

# Map document file - usually passed via File Iterator, pass as parameter 0
file = arcpy.GetParameterAsText(0)
# Description - required, pass as parameter 1
description = arcpy.GetParameterAsText(1)
# Summary - optional, pass as parameter 2, defaults to description
summary = arcpy.GetParameterAsText(2)
# Tags - optional, pass as parameter 3, defaults to description
tags = arcpy.GetParameterAsText(3)

# Set defaults
summary = summary if summary else description
tags = tags if tags else description

# Open map document
mxd = arcpy.mapping.MapDocument(file)

# Set map properties
mxd.description = description
mxd.summary = summary
mxd.tags = tags

# Save the map document
mxd.save()
