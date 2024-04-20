# SteelPy

`steelpy` is a library that acts a database for AISC steel shapes for easy use in structural calculations and applications.  The library includes W, M, S, HP, WT, MT, ST, Pipe, HSS, L, and Double L profiles.

## Contents
* [Installation](#installation)

* [Usage](#usage)

* [Filter Method](#filter-method)

* [Property Table](#property-table)

* [Property Descriptions](#property-descriptions)

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
### Property Table
| **Attribute** | **C**   | **DBL_L** | **HP**  | **HSS_R** | **HSS** | **L**   | **M**   | **MC**  | **MT**  | **PIPE** | **S**   | **ST**  | **W**   | **WT**  |
|:-------------:|:-------:|:---------:|:-------:|:---------:|:-------:|:-------:|:-------:|:-------:|:-------:|:--------:|:-------:|:-------:|:-------:|:-------:|
| **weight**    | &check; | &check;   | &check; | &check;   | &check; | &check; | &check; | &check; | &check; | &check;  | &check; | &check; | &check; | &check; |
| **area**      | &check; | &check;   | &check; | &check;   | &check; | &check; | &check; | &check; | &check; | &check;  | &check; | &check; | &check; | &check; |
| **d**         | &check; | &check;   | &check; | _         | _       | &check; | &check; | &check; | &check; | _        | &check; | &check; | &check; | &check; |
| **bf**        | &check; | _         | &check; | _         | _       | _       | &check; | &check; | &check; | _        | &check; | &check; | &check; | &check; |
| **tw**        | &check; | _         | &check; | _         | _       | _       | &check; | &check; | &check; | _        | &check; | &check; | &check; | &check; |
| **tf**        | &check; | _         | &check; | _         | _       | _       | &check; | &check; | &check; | _        | &check; | &check; | &check; | &check; |
| **k**         | &check; | _         | &check; | _         | _       | &check; | &check; | &check; | &check; | _        | &check; | &check; | &check; | &check; |
| **x**         | &check; | _         | _       | _         | _       | &check; | _       | &check; | _       | _        | _       | _       | _       | _       |
| **eo**        | &check; | _         | _       | _         | _       | _       | _       | &check; | _       | _        | _       | _       | _       | _       |
| **xp**        | &check; | _         | _       | _         | _       | &check; | _       | &check; | _       | _        | _       | _       | _       | _       |
| **Ix**        | &check; | &check;   | &check; | &check;   | &check; | &check; | &check; | &check; | &check; | &check;  | &check; | &check; | &check; | &check; |
| **Zx**        | &check; | &check;   | &check; | &check;   | &check; | &check; | &check; | &check; | &check; | &check;  | &check; | &check; | &check; | &check; |
| **Sx**        | &check; | &check;   | &check; | &check;   | &check; | &check; | &check; | &check; | &check; | &check;  | &check; | &check; | &check; | &check; |
| **rx**        | &check; | &check;   | &check; | &check;   | &check; | &check; | &check; | &check; | &check; | &check;  | &check; | &check; | &check; | &check; |
| **Iy**        | &check; | &check;   | &check; | &check;   | &check; | &check; | &check; | &check; | &check; | &check;  | &check; | &check; | &check; | &check; |
| **Zy**        | &check; | &check;   | &check; | &check;   | &check; | &check; | &check; | &check; | &check; | &check;  | &check; | &check; | &check; | &check; |
| **Sy**        | &check; | &check;   | &check; | &check;   | &check; | &check; | &check; | &check; | &check; | &check;  | &check; | &check; | &check; | &check; |
| **ry**        | &check; | &check;   | &check; | &check;   | &check; | &check; | &check; | &check; | &check; | &check;  | &check; | &check; | &check; | &check; |
| **J**         | &check; | _         | &check; | &check;   | &check; | &check; | &check; | &check; | &check; | &check;  | &check; | &check; | &check; | &check; |
| **Cw**        | &check; | _         | &check; | _         | _       | &check; | &check; | &check; | &check; | _        | &check; | &check; | &check; | &check; |
| **Wno**       | &check; | _         | &check; | _         | _       | _       | &check; | &check; | _       | _        | &check; | _       | &check; | _       |
| **Sw1**       | &check; | _         | &check; | _         | _       | _       | &check; | &check; | _       | _        | &check; | _       | &check; | _       |
| **Sw2**       | &check; | _         | _       | _         | _       | _       | _       | &check; | _       | _        | _       | _       | _       | _       |
| **Sw3**       | &check; | _         | _       | _         | _       | _       | _       | &check; | _       | _        | _       | _       | _       | _       |
| **Qf**        | &check; | _         | &check; | _         | _       | _       | &check; | &check; | _       | _        | &check; | _       | &check; | _       |
| **Qw**        | &check; | _         | &check; | _         | _       | _       | &check; | &check; | _       | _        | &check; | _       | &check; | _       |
| **ro**        | &check; | &check;   | _       | _         | _       | &check; | _       | &check; | &check; | _        | _       | &check; | _       | &check; |
| **H**         | &check; | &check;   | _       | _         | &check; | &check; | _       | &check; | &check; | _        | _       | &check; | _       | &check; |
| **rts**       | &check; | _         | &check; | _         | _       | _       | &check; | &check; | _       | _        | &check; | _       | &check; | _       |
| **ho**        | &check; | _         | &check; | _         | _       | _       | &check; | &check; | _       | _        | &check; | _       | &check; | _       |
| **PA**        | &check; | _         | &check; | _         | _       | &check; | &check; | &check; | _       | _        | &check; | _       | &check; | &check; |
| **PB**        | &check; | _         | &check; | _         | _       | &check; | &check; | &check; | _       | _        | &check; | _       | &check; | &check; |
| **PC**        | &check; | _         | &check; | _         | _       | _       | &check; | &check; | _       | _        | &check; | _       | &check; | &check; |
| **PD**        | &check; | _         | &check; | _         | _       | _       | &check; | &check; | _       | _        | &check; | _       | &check; | &check; |
| **T**         | &check; | &check;   | &check; | _         | _       | &check; | &check; | &check; | _       | _        | &check; | _       | &check; | _       |
| **WGi**       | &check; | _         | &check; | _         | _       | _       | &check; | &check; | &check; | _        | &check; | &check; | &check; | &check; |
| **b**         | _       | &check;   | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **y**         | _       | &check;   | _       | _         | _       | &check; | _       | _       | &check; | _        | _       | &check; | _       | &check; |
| **yp**        | _       | &check;   | _       | _         | _       | &check; | _       | _       | &check; | _        | _       | &check; | _       | &check; |
| **k1**        | _       | _         | &check; | _         | _       | _       | &check; | _       | _       | _        | _       | _       | &check; | _       |
| **OD**        | _       | _         | _       | &check;   | _       | _       | _       | _       | _       | &check;  | _       | _       | _       | _       |
| **tnom**      | _       | _         | _       | &check;   | &check; | _       | _       | _       | _       | &check;  | _       | _       | _       | _       |
| **tdes**      | _       | _         | _       | &check;   | &check; | _       | _       | _       | _       | &check;  | _       | _       | _       | _       |
| **C**         | _       | _         | _       | &check;   | &check; | _       | _       | _       | _       | _        | _       | _       | _       | _       |
| **Ht**        | _       | _         | _       | _         | &check; | _       | _       | _       | _       | _        | _       | _       | _       | _       |
| **Iz**        | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **rz**        | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **Sz**        | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **tan_a**     | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **Iw**        | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **zA**        | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **zB**        | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **zC**        | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **wA**        | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **wB**        | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **wC**        | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **SwA**       | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **SwB**       | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **SwC**       | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **SzA**       | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **SzB**       | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **SzC**       | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **PA2**       | _       | _         | _       | _         | _       | &check; | _       | _       | _       | _        | _       | _       | _       | _       |
| **ID**        | _       | _         | _       | _         | _       | _       | _       | _       | _       | &check;  | _       | _       | _       | _       |
| **WGo**       | _       | _         | _       | _         | _       | _       | _       | _       | _       | _        | _       | _       | &check; | &check; |

### Property Descriptions

| **Attribute** | **Description**                                                                                                                                                                                                                                                                                                                                                               |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **weight**    | Nominal weight, lb/ft                                                                                                                                                                                                                                                                                                                                                         |
| **area**      | Cross-sectional area, in.2                                                                                                                                                                                                                                                                                                                                                    |
| **d**         | Overall depth of member, or width of shorter leg for angles, or width of the outstanding legs of long legs back-to-back double angles, or the width of the back-to-back legs of short legs back-to-back double angles, in.                                                                                                                                                    |
| **bf**        | Width of flange, in.                                                                                                                                                                                                                                                                                                                                                          |
| **tw**        | Thickness of web, in.                                                                                                                                                                                                                                                                                                                                                         |
| **tf**        | Thickness of flange, in.                                                                                                                                                                                                                                                                                                                                                      |
| **k**         | Distance from outer face of flange to web toe of fillet used for design, in.                                                                                                                                                                                                                                                                                                  |
| **x**         | Horizontal distance from designated edge of member, as defined in the AISC Steel Construction Manual Part 1, to center of gravity of member, in.                                                                                                                                                                                                                              |
| **eo**        | Horizontal distance from designated edge of member, as defined in the AISC Steel Construction Manual Part 1, to shear center of member, in.                                                                                                                                                                                                                                   |
| **xp**        | Horizontal distance from designated edge of member, as defined in the AISC Steel Construction Manual Part 1, to plastic neutral axis of member, in.                                                                                                                                                                                                                           |
| **Ix**        | Moment of inertia about the x-axis, in.4                                                                                                                                                                                                                                                                                                                                      |
| **Zx**        | Plastic section modulus about the x-axis, in.3                                                                                                                                                                                                                                                                                                                                |
| **Sx**        | Elastic section modulus about the x-axis, in.3                                                                                                                                                                                                                                                                                                                                |
| **rx**        | Radius of gyration about the x-axis, in.                                                                                                                                                                                                                                                                                                                                      |
| **Iy**        | Moment of inertia about the y-axis, in.4                                                                                                                                                                                                                                                                                                                                      |
| **Zy**        | Plastic section modulus about the y-axis, in.3                                                                                                                                                                                                                                                                                                                                |
| **Sy**        | Elastic section modulus about the y-axis, in.3                                                                                                                                                                                                                                                                                                                                |
| **ry**        | Radius of gyration about the y-axis , in.                                                                                                                                                                                                                                                                                                                                     |
| **J**         | Torsional constant, in.4                                                                                                                                                                                                                                                                                                                                                      |
| **Cw**        | Warping constant, in.6                                                                                                                                                                                                                                                                                                                                                        |
| **Wno**       | Normalized warping function, as used in Design Guide 9, in.2                                                                                                                                                                                                                                                                                                                  |
| **Sw1**       | Warping statical moment at point 1 on cross section, as used in AISC Design Guide 9 and shown in Figures 1 and 2, in.4                                                                                                                                                                                                                                                        |
| **Sw2**       | Warping statical moment at point 2 on cross section, as used in AISC Design Guide 9 and shown in Figure 2, in.4                                                                                                                                                                                                                                                               |
| **Sw3**       | Warping statical moment at point 3 on cross section, as used in AISC Design Guide 9 and shown in Figure 2, in.4                                                                                                                                                                                                                                                               |
| **Qf**        | Statical moment for a point in the flange directly above the vertical edge of the web, as used in AISC Design Guide 9, in.3                                                                                                                                                                                                                                                   |
| **Qw**        | Statical moment for a point at mid-depth of the cross section, as used in AISC Design Guide 9, in.3                                                                                                                                                                                                                                                                           |
| **ro**        | Polar radius of gyration about the shear center, in.                                                                                                                                                                                                                                                                                                                          |
| **H**         | Depth of the flat wall of square HSS or longer flat wall of rectangular HSS, in.                                                                                                                                                                                                                                                                                              |
| **rts**       | Effective radius of gyration, in.                                                                                                                                                                                                                                                                                                                                             |
| **ho**        | Distance between the flange centroids, in.                                                                                                                                                                                                                                                                                                                                    |
| **PA**        | Shape perimeter minus one flange surface , as used in Design Guide 19, in.                                                                                                                                                                                                                                                                                                    |
| **PB**        | Shape perimeter, as used in AISC Design Guide 19, in.                                                                                                                                                                                                                                                                                                                         |
| **PC**        | Box perimeter minus one flange surface, as used in Design Guide 19, in.                                                                                                                                                                                                                                                                                                       |
| **PD**        | Box perimeter, as used in AISC Design Guide 19, in.                                                                                                                                                                                                                                                                                                                           |
| **T**         | Thickness of angle leg, in.                                                                                                                                                                                                                                                                                                                                                   |
| **WGi**       | The workable gage for the inner fastener holes in the flange that provides for entering and tightening clearances and edge distance and spacing requirements. The actual size, combination, and orientation of fastener components should be compared with the geometry of the cross section to ensure compatibility. See AISC Manual Part 1 for additional information, in.  |
| **b**         | Overall width of square HSS or shorter wall of rectangular HSS, in.                                                                                                                                                                                                                                                                                                           |
| **y**         | Vertical distance from designated edge of member, as defined in the AISC Steel Construction Manual Part 1, to center of gravity of member, in.                                                                                                                                                                                                                                |
| **yp**        | Vertical distance from designated edge of member, as defined in the AISC Steel Construction Manual Part 1, to plastic neutral axis of member, in.                                                                                                                                                                                                                             |
| **k1**        | Distance from web center line to flange toe of fillet used for detailing, in.                                                                                                                                                                                                                                                                                                 |
| **OD**        | Outside diameter of round HSS or pipe, in.                                                                                                                                                                                                                                                                                                                                    |
| **tnom**      | Nominal thickness of HSS and pipe wall, in.                                                                                                                                                                                                                                                                                                                                   |
| **tdes**      | Design thickness of HSS and pipe wall, in.                                                                                                                                                                                                                                                                                                                                    |
| **C**         | HSS torsional constant, in.3                                                                                                                                                                                                                                                                                                                                                  |
| **Ht**        | Overall depth of square HSS or longer wall of rectangular HSS, in.                                                                                                                                                                                                                                                                                                            |
| **Iz**        | Moment of inertia about the z-axis, in.4                                                                                                                                                                                                                                                                                                                                      |
| **rz**        | Radius of gyration about the z-axis, in.                                                                                                                                                                                                                                                                                                                                      |
| **Sz**        | Elastic section modulus about the z-axis, in.3 . For single angles, see SzA, SzB, and SzC.                                                                                                                                                                                                                                                                                    |
| **tan_a**     | Tangent of the angle between the y-y and z-z axes for single angles, where a is shown in Figure 3                                                                                                                                                                                                                                                                             |
| **Iw**        | Moment of inertia about the w-axis for single angles, in.4                                                                                                                                                                                                                                                                                                                    |
| **zA**        | Distance from point A to center of gravity along z-axis, as shown in Figure 3, in.                                                                                                                                                                                                                                                                                            |
| **zB**        | Distance from point B to center of gravity along z-axis, as shown in Figure 3, in.                                                                                                                                                                                                                                                                                            |
| **zC**        | Distance from point C to center of gravity along z-axis, as shown in Figure 3, in.                                                                                                                                                                                                                                                                                            |
| **wA**        | Distance from point A to center of gravity along w-axis, as shown in Figure 3, in.                                                                                                                                                                                                                                                                                            |
| **wB**        | Distance from point B to center of gravity along w-axis, as shown in Figure 3, in.                                                                                                                                                                                                                                                                                            |
| **wC**        | Distance from point C to center of gravity along w-axis, as shown in Figure 3, in.                                                                                                                                                                                                                                                                                            |
| **SwA**       | Elastic section modulus about the w-axis at point A on cross section, as shown in Figure 3, in.3                                                                                                                                                                                                                                                                              |
| **SwB**       | Elastic section modulus about the w-axis at point B on cross section, as shown in Figure 3, in.3                                                                                                                                                                                                                                                                              |
| **SwC**       | Elastic section modulus about the w-axis at point C on cross section, as shown in Figure 3, in.3                                                                                                                                                                                                                                                                              |
| **SzA**       | Elastic section modulus about the z-axis at point A on cross section, as shown in Figure 3, in.3                                                                                                                                                                                                                                                                              |
| **SzB**       | Elastic section modulus about the z-axis at point B on cross section, as shown in Figure 3, in.3                                                                                                                                                                                                                                                                              |
| **SzC**       | Elastic section modulus about the z-axis at point C on cross section, as shown in Figure 3, in.3                                                                                                                                                                                                                                                                              |
| **PA2**       | Single angle shape perimeter minus long leg surface, as used in AISC Design Guide 19, in.                                                                                                                                                                                                                                                                                     |
| **ID**        | Inside diameter of pipe, in.                                                                                                                                                                                                                                                                                                                                                  |
| **WGo**       | The bolt spacing between inner and outer fastener holes when the workable gage is compatible with four holes across the flange. See AISC Manual Part 1 for additional information, in.                                                                                                                                                                                        |
