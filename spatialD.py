### *- Program: Spatial'D
### *- Objective: A batch processing script that searches a workspace for vector
### dataset, checks to see if it has a spatial reference system defined, and
### if not, then assigns one. Also provides total for the number of feature
### classes in the workspace, total number of feature classes with a spatial
### reference system, and list of names of feature classes without a spatial
### reference system
### *- Input: Provided by the user (workspace)
### *- Output: Total number of feature classes, total number of feature classes
### with a spatial reference system, list of names of feature classes without a
### spatial reference system, and a completion message once the process of
### assigning a spatial reference system is complete

# - START PROGRAM -

# Import OS module to load appropriate paths depending on which system is being used
import os

# Import ArcPy module to use built-in functions to achieve the program objective
import arcpy
# From ArcPy, import the environment/workspace
from arcpy import env

# Ask the user to input a file path to set as a workspace
env.workspace = raw_input("\nPlease enter your directory [*.mdb or *.gdb]: ")
# Assign the workspace to a new variable
filePath = env.workspace

x = 0
while x < 1:                     # Set up a file validation system
    if os.path.exists(filePath): # If file path, exists: continue. Otherwise..
        x = 1                    # ..go to Line 57
        
        fCList = arcpy.ListFeatureClasses("*", "All") # List feature classes
        for fC in fCList:        # For files in the feature classes list..
            desc = arcpy.Describe(fC) # ..describe them for multiple purposes for later use
            spatialRef = desc.spatialReference # Describe the spatial reference system of the files
            
            if spatialRef.Name == 'Unknown': # If spatial reference system is unknown..
                continue # ..go to Line 43
                print "\n" + fC, ("has an 'Unknown' spatial reference\n") # Display list of names of feature classes with no spatial reference system
                
            else:
                definedfC = fC + '_UTM_1983' # Name of output file
                prjFile = 'Coordinate Systems/Projected Coordinate Systems/UTM/NAD 1983/NAD 1983 UTM Zone 11N.prj' # Default path to .prj file in ArcMap
                arcpy.Project_management(fC, definedfC, prjFile) # Define projection function from ArcPy
                
        for fC in fCList:        # For files in the feature classes list..
            if spatialRef.Name == 'Unknown': # ..if spatial reference system is unknown..
                print "\n" + fC, ("has an 'Unknown' spatial reference\n") # ..display those files
            else:
                Unknown =  [fC for fC in fCList if arcpy.Describe(fC).spatialReference.Name == 'Unknown'] # List of files with unknown spatial reference
                Known = len(fCList) - len(Unknown) # Determine the number of files with known spatial reference system

        print ("\nTotal number of feature classes with a defined spatial reference:"), Known # Display total number of files with known spatial reference
        fCCount = len(fCList)                                                                # Determine total of number of feature classes
        print ("\nTotal number of feature classes:"), fCCount                             # Display total number of files in workspace 
        print ("\nAll feature classes have now been defined in 'NAD 1983 UTM Zone 11N' format.\n") # Completion message for assigning a spatial reference
            
    else:
        raw_input("\n!ERROR!: File path does not exist." # If file path does not exist..
                  "\nPress Enter to continue. ")         # ..display an error message..
        env.workspace = raw_input("\nPlease enter your file path: ") # ..and ask user to..
        filePath = env.workspace                         # ..enter it again

# Import time module and exit the program in 10 seconds
import time
time.sleep(15)

# - END PROGRAM -

# I'm Dr. Sheldon Cooper, BSc, MSc, MA, PhD, and ScD... OMG right? *chuckle*
# - Sheldon Cooper (The Big Bang Theory)
