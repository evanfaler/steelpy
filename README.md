# SteelPy

`steelpy` is a library that acts a database for AISC steel shapes for easy use in structural calculations and applications.  The library includes W, M, S, HP, WT, MT, ST, Pipe, HSS, L, and Double L profiles.

## Contents
* [Installation](#installation)

* [Usage](#usage)

* [Filter Method](#filter-method)

## Installation
Install using pip:
```
pip install steelpy
```

## Usage
To use the steelpy library, first import the module

```
from steelpy import aisc
```

The library includes W, M, S, HP, WT, MT, ST, Pipe, HSS, L, and Double L profiles.  To access a library of shapes, simply use dot notation for the group of profiles:
```
aisc.C_shapes
aisc.DBL_L_shapes
aisc.HP_shapes
aisc.HSS_R_shapes
aisc.HSS_shapes
aisc.L_shapes
aisc.M_shapes
aisc.MC_shapes
aisc.MT_shapes
aisc.PIPE_shapes
aisc.S_shapes
aisc.ST_shapes
aisc.W_shapes
aisc.WT_shapes
```
From there, specific sections and properties are queried in a similar manner:
```
beam = aisc.W_shapes.W12X26
Fy = 50
Aw = beam.d * beam.tw
Cv = 1.0
Vn = 0.6*Fy*Aw*Cv
```
Sections with fractions, hyphens or decimal points in their names are queried by replacing each with underscore:
```
aisc.C_shapes.C12X20_7
aisc.L_shapes.L4X4X1_4
aisc.W_shapes.W6X8_5
```
Values are consistent with the AISC Steel Construction Manual, 16th Ed. and use the imperial system (inches, lbs).  .csv files for each library of shapes is saved in steelpy > shape files and can be referenced for the available shape profiles and associated properties.

## Filter Method
The `filter` method allows you to filter the sections of a collection based on specified criteria, maximum values, minimum values, or a combination thereof. Additionally, you can sort the filtered result by a specified property.

### Parameters
* `criteria`: A `dictionary` where keys are the properties to filter by, and values are dictionaries with 'min' and/or 'max' keys specifying the minimum and maximum values for each property.
* `sort_by`: (Optional) The attribute by which to sort the filtered result. Defaults to sort by weight.

### Return Value
A `dictionary` containing all `Section` objects that meet the provided filtering criteria, sorted by the specified attribute if `sort_by` is provided.

### Usage Example
```
# Example usage 1: Filter sections based on a single property with a minimum value and sort the results by another property
filtered_result = aisc.W_shapes.filter({'Zx': {'min': 150}}, sort_by='Iy')

# Example usage 2: Filter sections based on multiple properties with different maximum and minimum values
filtered_result = aisc.W_shapes.filter({'d': {'min': 8, 'max': 12.3}, 'Ix': {'max': 100}})

# Access the filtered sections in example 2
for section_name, section_object in filtered_result.items():
    print(f"Section: {section_name}, d: {section_object.d}, Ix: {section_object.Ix}")

# Expected output:
# Section: W12X16, d: 12.0, Ix: 103.0
# Section: W12X19, d: 12.2, Ix: 130.0
# Section: W12X22, d: 12.3, Ix: 156.0
# ...
```


