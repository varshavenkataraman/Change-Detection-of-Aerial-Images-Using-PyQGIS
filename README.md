# Change-Detection-of-Aerial-Images-Using-PyQGIS
Image Processing project detecting temporal changes in satellite imagery using PyQGIS &amp; GDAL Raster Calculator.

Pixel-based change detection using PyQGIS and GDAL Raster Calculator to compute absolute differences between two raster images.

Change Detection on Aerial Images (PyQGIS)

Datasets Courtesy: https://github.com/ChenHongruixuan/ChangeDetectionRepository/tree/master/Dataset/Landsat/Nanjing

Overview
This project detects changes in aerial/satellite images over time using
a pixel-based raster differencing approach in PyQGIS.

It uses GDAL Raster Calculator to compute differences between two images.

Methodology
1. Load two georeferenced images (before & after)
2. Apply raster differencing:
   
   Change = abs(Image2 - Image1)

3. Generate output raster highlighting changes

Tech Stack
- PyQGIS
- GDAL
- Python

Input
- `nanjing1.jpg` (Before)
- `nanjing2.jpg` (After)

Output
- `change_detected.tif`

Result
Bright regions in output indicate higher change intensity.

How to Run
1. Install QGIS
2. Open Python Console OR run script externally
3. Update file paths
4. Run script
