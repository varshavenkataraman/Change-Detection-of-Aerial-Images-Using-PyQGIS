import processing
from qgis.core import QgsApplication

QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.x/apps/qgis", True)
qgs = QgsApplication([], False)
qgs.initQgis()

raster1_path = r'C:\path\to\nanjing1.jpg'   
raster2_path = r'C:\path\to\nanjing2.jpg'   

output_path = r'C:\path\to\change_detected.tif'

params = {
    'INPUT_A': raster1_path,
    'BAND_A': 1,
    'INPUT_B': raster2_path,
    'BAND_B': 1,

    'INPUT_C': None,
    'BAND_C': -1,
    'INPUT_D': None,
    'BAND_D': -1,
    'INPUT_E': None,
    'BAND_E': -1,
    'INPUT_F': None,
    'BAND_F': -1,

    'FORMULA': 'abs(B - A)',  #Change = abs(Image2 - Image1)
    'OUTPUT': output_path,

    'RTYPE': 5,   
    'EXTRA': '',
    'OPTIONS': '',
    'OUTPUT_EXTENT': None,
    'OUTPUT_PROJECTION': None
}

processing.run("gdal:rastercalculator", params)

print("Change detection completed!")
print(" Output saved at:", output_path)

qgs.exitQgis()
