import blood_calculator as bc

print("This is the database.py file")
print("Python thinks this is called {}".format(__name__))

# Will automatically run what's being imported
# Imported the whole module (every function included)
# Can call other functions by: bc.function_name("Other Test")

# If only need one function:
# from blood_calculator import HDL_analysis, generic_input
# No need to specify where it comes from later on in this module
# Also needs if name == main to avoid running whole program

# (Don't use this) Another method:
# from blood_calculator import *
# All functions will be imported, no need to specify
# Considered bad pratice b/c not readable/tracable,
# cannot know which function comes from where


HDL = 55

HDL_analysis = bc.HDL_analysis(HDL)

print("The HDL analysis is {}".format(HDL_analysis))
