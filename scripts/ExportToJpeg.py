import arcpy

# Map document file - usually passed via File Iterator, pass as parameter 0
file = arcpy.GetParameterAsText(0)
# Width of JPEG file - optional, pass as paramter 1, defaults to 3509
width = int(arcpy.GetParameterAsText(1))
# Height of JPEG file - optional, pass as paramter 2, defaults to 2489
height = int(arcpy.GetParameterAsText(2))
# Resolution of JPEG file - optional, pass as parameter 3, defaults to 300
resolution = int(arcpy.GetParameterAsText(2))

# Set defaults if parameters are not set
width = width if width > 0 else 3509
height = height if height > 0 else 2489
resolution = resolution if resolution > 0 else 300

# Open current MXD File
mxd = arcpy.mapping.MapDocument(file)

# Export to JPG on same folder, with specific resolution
arcpy.mapping.ExportToJPEG(mxd, mxd.filePath.replace('.mxd','.jpg'), "PAGE_LAYOUT", 3509, 2489, 300)

# No changes to map document are made, so no saves are done
