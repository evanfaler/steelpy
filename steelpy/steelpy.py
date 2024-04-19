import pandas as pd
from collections import namedtuple
import os
import glob

class Steel:
    def __init__(self, name):
        self.name = name
        self.profiles = {}

    def add_variable(self, name, value):
        self.profiles[name] = value

    def __getattr__(self, name):
        if name in self.profiles:
            return self.profiles[name]
        raise AttributeError(f"'Steel' object has no attribute '{name}'")
    
class Profile:
    def __init__(self, name):
        self.name = name
        self.sections = {}

    def add_variable(self, name, value):
        self.sections[name] = value

    def __getattr__(self, name):
        if name in self.sections:
            return self.sections[name]
        raise AttributeError(f"'Profile' object has no attribute '{name}'")
    
class Section:
    def __init__(self, name):
        self.name = name
        self.properties = {}

    def add_variable(self, name, value):
        self.sections[name] = value

    def __getattr__(self, name):
        if name in self.sections:
            return self.sections[name]
        raise AttributeError(f"'Section' object has no attribute '{name}'")
    
    
aisc = Steel('aisc')

# Get the directory of the currently executing module
module_dir = os.path.dirname(__file__)
# Construct the relative path to shape files folder.
directory_path = os.path.join(module_dir, 'shape files')

# Get a list of all .xlsx files in the directory
shape_files = glob.glob(os.path.join(directory_path, "*.xlsx"))

# Iterate over each .xlsx file
for file in shape_files: 
    # Get current shape being considered e.g. 'W_shapes'
    curFileName = os.path.basename(file)[:-5]

    # Read Excel file into a pandas DataFrame
    df = pd.read_excel(file)

    # Define a named tuple class for the shape section properties dynamically
    ShapeProperties = namedtuple('ShapeProperties', df.columns[1:])

    # Create a dictionary to store shape section properties
    props_dict = {}

    # Populate the dictionary with shape section properties
    for row in df.itertuples(index=False):
        key = row[0]  # Key is taken from the first column
        properties = ShapeProperties(*row[1:])  # Create a namedtuple for properties
        props_dict[key] = properties

    # Define a named tuple class for the steel shapes
    SteelShapes = namedtuple('SteelShapes', props_dict.keys())

    # Create dictionary for 

    # Create a named tuple instance for steel shapes
    steel_shapes = SteelShapes(**props_dict)

    #add shape to aisc class
    aisc.add_variable(curFileName, steel_shapes)