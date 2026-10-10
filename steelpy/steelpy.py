import csv
import os
import glob


def _is_missing(value):
    # NaN is not equal to itself; None also represents a missing value.
    return value is None or value != value


class Steel:
    def __init__(self, name):
        self.name = name
        self.profiles = {}

    def add_profile(self, name, value):
        self.profiles[name] = value

    def __getattr__(self, name):
        profiles = self.__dict__.get('profiles', {})
        if name in profiles:
            return profiles[name]
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
                Missing property values are excluded from criteria and sorted last.
        """
        filtered_dict = {}
        for section_name in self.sections:
            section = self.sections[section_name]
            meets_criteria = True
            for prop, values in criteria.items():
                prop_value = getattr(section, prop)
                if _is_missing(prop_value):
                    meets_criteria = False
                    break
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
            def sort_key(item):
                value = getattr(item[1], sort_by)
                # Sort known values first and missing values last.
                return (1, 0) if _is_missing(value) else (0, value)

            filtered_dict = dict(sorted(filtered_dict.items(), key=sort_key))

        return filtered_dict
    
    def __getattr__(self, name):
        sections = self.__dict__.get('sections', {})
        if name in sections:
            return sections[name]
        raise AttributeError(f"'Profile' object has no attribute '{name}'")
    
class Section:
    def __init__(self, name):
        self.name = name
        self.properties = {}

    def add_property(self, name, value):
        self.properties[name] = value

    def __getattr__(self, name):
        properties = self.__dict__.get('properties', {})
        if name in properties:
            return properties[name]
        raise AttributeError(f"'Section' object has no attribute '{name}'")
    
aisc = Steel('AISC')

# Get the directory of the currently executing module.
module_dir = os.path.dirname(__file__)
# Construct the relative path to the shape files folder.
directory_path = os.path.join(module_dir, 'shape files')
# Get a list of all CSV files in the directory.
shape_files = glob.glob(os.path.join(directory_path, "*.csv"))

# Iterate over each CSV profile file.
for file in shape_files:
    # Get the profile name from the filename, for example 'W_shapes'.
    cur_profile_name = os.path.basename(file)[:-4]
    # Create a Profile object to hold the sections in this file.
    cur_profile = Profile(cur_profile_name)
    # Open the CSV file; DictReader uses its header row as the property names.
    with open(file, newline='', encoding='utf-8') as source:
        # Create a Section object for each data row in the CSV file.
        for row in csv.DictReader(source):
            # Separate the section name from the remaining property values.
            cur_section_name = row.pop('shape')
            cur_section = Section(cur_section_name)
            # Store numeric properties as floats and the '–' missing marker as NaN.
            cur_section.properties = {
                name: float(value) if value != '–' else float('nan')
                for name, value in row.items()
            }
            # Add the current Section object to the current Profile object.
            cur_profile.add_section(cur_section_name, cur_section)
    # Add the completed Profile object to the Steel object.
    aisc.add_profile(cur_profile_name, cur_profile)
