ArcPy Scripts
=============

Short and useful Python scripts for automating tasks in ArcGIS 10.x using the ArcPy module.

1. **dms2dd**: Convert geographic coordinates from DMS to DD, and vice versa.
2. **featureCC**: Determine the total number of point, line, and polygon shapefiles in a directory.
3. **rasterCP**: Determine if a directory has raster data. If so, provide the user with information such as file name, format, and number of bands.
4. **rasterMM**: Determine the max & min values in a raster dataset.
5. **spatialD**: A batch processing script that searches a workspace for vector dataset, checks to see if it has a spatial reference system defined. If not, then assigns one. Also provides total for the number of feature classes in the workspace, total number of feature classes with a spatial reference system, and list of names of feature classes without a spatial reference system.

Field Calculator Scripts
========================

.cal files for automating tasks in the Field Calculator.

1. **latitudeDD**: Convert latitude DMS values to DD using indexing in a table.
2. **longitudeDD**: Convert longitude DMS values to DD using indexing in a table.
3. **merge**: Combine data from two different fields into a new column.
