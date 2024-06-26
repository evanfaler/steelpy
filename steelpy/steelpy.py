import pandas as pd
from collections import namedtuple
import os
import glob

class Steel:
    def __init__(self, name):
        self.name = name
        self.profiles = {}

    def add_profile(self, name, value):
        self.profiles[name] = value

    def __getattr__(self, name):
        if name in self.profiles:
            return self.profiles[name]
        raise AttributeError(f"'Steel' object has no attribute '{name}'")
    
class Profile:
    def __init__(self, name):
        self.name = name
        self.sections = {}

    def add_section(self, name, value):
        self.sections[name] = value
    
    def filter(self, criteria, sort_by='weight'):
        """
        Filters the self.sections dictionary based on given criteria, max values, min values, or both.

        Args:
            criteria (dict): Dictionary where keys are properties to filter by and values are dictionaries with 'max' and 'min' keys.
                example dictionary: {'d': {'min': 10, 'max': 20}, 'Ix': {'min': 500}} will return sections between 10 and 20 inches deep with an Ix greater than 500 in4
            sort_by (string, optional): property by which the filtered collection will be sorted.  Defaults to section weight.

        Returns:
            dict: Dictionary of all Section objects that meet the provided criteria.
        """
        filtered_dict = {}
    
        filtered_dict = {}
        for section_name in self.sections:
            section = self.sections[section_name]
            meets_criteria = True
            for prop, values in criteria.items():
                prop_value = getattr(section, prop)
                if 'min' in values and prop_value < values['min']:
                    meets_criteria = False
                    break
                if 'max' in values and prop_value > values['max']:
                    meets_criteria = False
                    break
            if meets_criteria:
                filtered_dict[section_name] = section

        # Sort the filtered dictionary by the specified attribute
        if sort_by:
            filtered_dict = dict(sorted(filtered_dict.items(), key=lambda item: getattr(item[1], sort_by)))

        return filtered_dict
    
    def __getattr__(self, name):
        if name in self.sections:
            return self.sections[name]
        raise AttributeError(f"'Profile' object has no attribute '{name}'")
    
class Section:
    def __init__(self, name):
        self.name = name
        self.properties = {}

    def add_property(self, name, value):
        self.properties[name] = value

    def __getattr__(self, name):
        if name in self.properties:
            return self.properties[name]
        raise AttributeError(f"'Section' object has no attribute '{name}'")
    
aisc = Steel('AISC')

# Get the directory of the currently executing module
module_dir = os.path.dirname(__file__)
# Construct the relative path to shape files folder.
directory_path = os.path.join(module_dir, 'shape files')

# Get a list of all .xlsx files in the directory
shape_files = glob.glob(os.path.join(directory_path, "*.csv"))

# Iterate over each .xlsx profile file
for file in shape_files: 
    # Get current shape being considered e.g. 'W_shapes' from file name.
    cur_profile_name = os.path.basename(file)[:-4]

    # Read Excel file into a pandas DataFrame
    df = pd.read_csv(file)

    # create Profile object for current profile
    cur_profile = Profile(cur_profile_name)

    # generate array of section property names from first row of each excel file.
    section_property_names = df.columns[1:].values

    # iterate over each row of excel file, create new Section object for each row.
    for index, row in df.iterrows():
        cur_section_name = row.iloc[0]
        cur_section = Section(cur_section_name)
        section_property_values = row[1:].values

        # iterate through each cell of the row and add properties to the Section object.
        for i, property_name in enumerate(section_property_names):
            cur_section.add_property(property_name, section_property_values[i])
        
        # add the current Section object to the current Profile object.
        cur_profile.add_section(cur_section_name, cur_section)
    
    # Add current Profile object to the Steel object.
    aisc.add_profile(cur_profile_name, cur_profile)