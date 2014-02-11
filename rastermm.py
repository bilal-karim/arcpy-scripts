# -*- coding: utf-8 -*-
# Program: RASTR.MM
# Version: 1.0
# Objective: To determine the max & min values in a raster dataset

# - BEGIN PROGRAM -
# Ascii art and name

print(
      r"""
               _____            _____ _______ _____    __  __ __  __ 
              |  __ \    /\    / ____|__   __|  __ \  |  \/  |  \/  |
              | |__) |  /  \  | (___    | |  | |__) | | \  / | \  / |
              |  _  /  / /\ \  \___ \   | |  |  _  /  | |\/| | |\/| |
              | | \ \ / ____ \ ____) |  | |  | | \ \ _| |  | | |  | |
              |_|  \_|_/    \_\_____/   |_|  |_|  \_(_)_|  |_|_|  |_|

                        -._ Developed by: Bilal Karim _.-                                
        """
      )

# Main body of code

import os # Import OS module for later use to load appropriate paths, depending on which system is being used

filePath = raw_input("\n Hello, user. "   # Provide info/instructions and ask user to input file path
                      "RASTR.MM lets you determine the MAX and MIN values of your raster dataset."
                      "\n \n Please type in the path of your raster file and press 'Enter': ")
                    
x = 0 # Set up a file path validation system
while x < 1:
    if os.path.exists(filePath):          # If file path exists, continue. Otherwise, go to Line 58
        x = 1
        rasterFile = open(filePath, "r")  # Open the file in read mode
        data = rasterFile.readlines()[6:] # Read lines in data except for first 6 lines (i.e., skip header information)
        check = True                      # Validation system for later use to determine max & min values
        for lines in data:
            content = lines.split()       # Split lines of data and assign to a new variable   
            for dNvalue in content:
                dNvalue = int(dNvalue)    # Convert strings of DN values from data into integers for max & min evaluation
                if check == True:         
                    max = -1              # Validation system for min value (i.e., anything lower than 255)
                    min = 255             # Validation system for max value (i.e., anything higher than -1)
                    check = False
                else:
                    if dNvalue > max:     # Check to see if the currently read value is greater than max (i.e., -1)..
                        max = dNvalue     # ..and keep continuing until the max value is found from the data
                    if dNvalue < min:     # Check to see if the currently read value is less than min (i.e., 255)..
                        min = dNvalue     # ..and keep continuing until the min value is found from the data
        print ("\n Oh, hai there!"), ("\n Your maximum value is"), max, # Display max value to user
        print ("\n Your minimum value is"), min  # Display min value to user
        rasterFile.close()                # Close the file
    else:                                                                             # If file path does not exist.. 
        raw_input("\n ** ERROR: File does not exist. Press 'Enter' to continue. ** ") # ..display an error message, and..
        filePath = raw_input("\n Please type in the path to your raster file and press 'Enter': ") # ..ask the user to input the file path again

print ("\n RASTR.MM will exit in 5 seconds. \n") # Display exit message for users running this program in Command Prompt/Terminal
import time # Import time module..
time.sleep(5) # ..and exit the program in 5 seconds

# - END PROGRAM -
# What’s the most resilient parasite? Bacteria? A virus? An intestinal worm? An idea. Resilient. Highly contagious.
# Once an idea has taken hold of the brain, it is almost impossible to eradicate. An idea that is fully formed..
# ..fully understood - that sticks; right in there somewhere - Dom Cobb (Inception)
