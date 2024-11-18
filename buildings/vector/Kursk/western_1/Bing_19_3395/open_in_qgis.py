from qgis.core import QgsProject, QgsRasterLayer, QgsVectorLayer

# Define the paths to the raster and vector datasets
raster_paths = [
    '../data/raster/Kursk/Bing_19_3395.tif'
]

vector_paths = [
    '../data/buildings/vector/Kursk/western_1/Bing_19_3395/roofs.shp',
    '../data/buildings/vector/Kursk/western_1/Bing_19_3395/projes.shp',
    '../data/buildings/vector/Kursk/western_1/Bing_19_3395/shades.shp'
]

# Get the current QGIS project instance
project = QgsProject.instance()

# Load and add raster layers to the project
for raster_path in raster_paths:
    layer_name = raster_path.split('/')[-1]  # Use the filename as the layer name
    raster_layer = QgsRasterLayer(raster_path, layer_name)
    if not raster_layer.isValid():
        print(f"Failed to load raster layer: {layer_name}")
    else:
        project.addMapLayer(raster_layer)

# Load and add vector layers to the project
for vector_path in vector_paths:
    layer_name = vector_path.split('/')[-2] + ' - ' + vector_path.split('/')[-1]  # Use the folder and filename as the layer name
    vector_layer = QgsVectorLayer(vector_path, layer_name, "ogr")
    if not vector_layer.isValid():
        print(f"Failed to load vector layer: {layer_name}")
    else:
        project.addMapLayer(vector_layer)
