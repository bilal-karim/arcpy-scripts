# -*- coding: utf-8 -*-
# Program: DMS2DD
# Version: 1.0
# Objective: To convert geographic coordinates from DMS to DD, and vice versa

# — Begin Code —

# ASCII art and name of the program
print(
      r"""
                    ____  __  __ ____ ____  ____  ____  
                   |  _ \|  \/  / ___|___ \|  _ \|  _ \ 
                   | | | | |\/| \___ \ __) | | | | | | |
                   | |_| | |  | |___) / __/| |_| | |_| |
                   |____/|_|  |_|____/_____|____/|____/ 

                    —._ Developed by: Bilal Karim _.—                                
        """
      )

# Instructions and information about the program for the user
raw_input("Hello, user. DMS2DD is a program that lets you convert geographic coordinates (latitude/longitude) entered in degrees, minutes, seconds (DMS) format into decimal degrees (DD), and vice-versa. Press 'Enter' to begin.")

# Provide the user with an option (DMS to DD or DD to DMS)
mode = int(raw_input("\n Enter '1' to convert geographic coordinates from DMS to DD. \n \n - or - \n \n Enter '2' to convert geographic coordinates from DD to DMS. \n \n"))

# Define the variables
D = "Degrees"
M = "Minutes"
S = "Seconds"
DD = "Decimal Degrees"
DM = "Decimal Minutes"

# Using while statements, decide which formula to use
# Mode 1 will convert DMS to DD
while mode == 1: 
    
    while D > 360: # Limit for Degrees
        D = input("\n Enter Degrees: ") # Ask the user to input Degrees
        if D > 360:
            print("\n ** Error: Please enter a value less than or equal to 360 degrees. **")
            # If the user enters a value higher than 360, display this message

    while M > 60: # Limit for Minutes
        M = input("\n Enter Minutes: ") # Ask the user to input Minutes
        if M > 60:
            print("\n ** Error: Please enter a value less than or equal to 60 degrees. **")
            # If the user enters a value higher than 60, display this message

    while S > 60: # Limit for Seconds
        S = input("\n Enter Seconds: ")
        if S > 60:
            print("\n ** Error: Please enter a value less than or equal to 60 degrees. **")
            # If the user enters a value higher than 60, display this message

# The formula to convert from DMS to DD
# where D = degrees, M = minutes, S = seconds
    DD = D + float(M)/60 + float(S)/3600
    
# Display the final result
    print ("\n Your converted value is"), DD, ("\n \n Bio-digital jazz, man - Kevin Flynn (TRON: Legacy) \n \n")
    break

# Mode 2 will convert from DD to DMS
while mode == 2:

    while DD > 360: # Limit for Decimal Degrees
        DD = float(input("\n Enter Decimal Degrees: ")) # Ask user to input Decimal Degrees
        if DD > 360:
            print("\n ** Error: Please enter a value less than or equal to 360 degrees. **")
    
    # The Degree value calculated as follows
    D = int(DD) 

    # Take the decimal portion of DD and multiply by 60 
    DM = abs(DD - D) * 60

    # The Minutes value calculated as follows
    M = int(DM)

    # The Seconds value calculated as follows
    S = (DM - M) * 60 

    # Display the final result
    print ("\n Your converted value is"),D,("°"), M,("'"), S,("''"), ("\n \n Live long and prosper - Spock (Star Trek) \n \n")
    break

# If user enters a number greater than 2 for mode, display restart message
if mode > 2:
    print ("\n ** Error: Please restart the program and select a mode. **")

# — End Code —

# Design is not just what it looks like & feels like. Design is how it works – Steve Jobs
