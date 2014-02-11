### *- Program: FeatureCC
### *- Objective: To determine the total number of point, line, and polygon shapefiles
### in a directory
### *- Input: Provided by the user (workspace)
### *- Output: Display total files for point, line, and polygon shapefiles to the user

# - START PROGRAM -

# Import OS module to load appropriate paths depending on which system is being used
import os

# Import ArcPy module to use built-in functions to achieve the program objective
import arcpy
# From ArcPy, import the environment/workspace
from arcpy import env

# Ask the user to input a file path to set as a workspace
env.workspace = raw_input("\nPlease enter your file path: ")
# Assign the workspace to a new variable
filePath = env.workspace

x = 0
while x < 1:                     # Set up a file validation system       
    if os.path.exists(filePath): # If file path, exists: continue. Otherwise..
        x = 1                    # ..go to Line 45
        
        point = arcpy.ListFeatureClasses("*", "Point")  # List point feature classes
        line = arcpy.ListFeatureClasses("*", "Line")    # List line feature classes
        poly = arcpy.ListFeatureClasses("*", "Polygon") # List polygon feature classes
        
        pointCount = len(point) # Count the number of point feature classes
        lineCount = len(line)   # Count the number of line feature classes
        polyCount = len(poly)   # Count the number of polygon feature classes
        
        print("\nPOINTS:"), pointCount, ("files")  # Print total for point feature classes 
        print("LINES:"), lineCount, ("files")      # Print total for line feature classes
        print("POLYGONS:"), polyCount, ("files\n") # Print total for polygon feature classes
        
    else:
        raw_input("\n!ERROR! - File path does not exist." # If file path does not exist..
                  "\nPress Enter to continue. ")          # ..display an error message..
        env.workspace = raw_input("\nPlease enter your file path: ") # ..and ask user to..
        filePath = env.workspace                          # ..enter it again

# Import time module and exit the program in 10 seconds
import time
time.sleep(10)

# - END PROGRAM -

# I'm gonna make him an offer he can't refuse
# - Don Vito Corleone (The Godfather)
