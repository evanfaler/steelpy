# SteelPy

`steelpy` is a library that acts a database for AISC steel shapes for easy use in structural calculations and applications.  The library includes W, M, S, HP, WT, MT, ST, Pipe, HSS, L, and Double L profiles.

## Contents
* Installation

* Usage

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


