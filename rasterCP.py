### *- Program: RasterCP
### *- Objective: To determine if a directory has raster data. If so, provide
### the user with information such as file name, format, and number of bands
### *- Input: Provided by the user (workspace)
### *- Output: Display a list of raster files with their name, format, and
### band count

# - START PROGRAM -

# Import OS module to load appropriate paths depending on which system is being used
import os

# Import ArcPy module to use built-in functions to achieve the program objective
import arcpy
# From ArcPy, import the environment/workspace
from arcpy import env

# Ask the user to input a file path to set as a workspace
env.workspace = raw_input("Please enter your directory [raster dataset]: ")
# Assign the workspace to a new variable
filePath = env.workspace

x = 0
while x < 1:                     # Set up a file validation system
    if os.path.exists(filePath): # If file path, exists: continue. Otherwise..
        x = 1                    # ..go to Line 46
        
        rasterList = arcpy.ListDatasets("*", "Raster") # List rasters datasets ONLY
        if len(rasterList) == 0: # If there are no raster datasets, display error message
            print("\n!ERROR!: File path does not contain any raster data. "
            "\nPlease restart the program and select a directory with raster data.")
            
        else:                    # If raster datasets do exist..
            for fileNames in rasterList: # ..for every file in that list..
                print ("\nNAME:"), fileNames # ..print their names
                
                desc = arcpy.Describe(filePath + "\\" + fileNames) # Create a variable for describe function
                print ("FORMAT:"), desc.Format # Print the format of raster file
                print ("BANDS:"), desc.bandCount, ("\n") # Print the number of bands of raster file
    else:
        raw_input("\n!ERROR!: File path does not exist." # If file path does not exist..
                  "\nPress Enter to continue. ")         # ..display an error message..
        env.workspace = raw_input("\nPlease enter your file path: ") # ..and ask user to..
        filePath = env.workspace                         # ..enter it again

# - END PROGRAM -

# Out of clutter, find simplicity; from discord, find harmony;
# in the middle of difficulty, lies opportunity - Albert Einstein
