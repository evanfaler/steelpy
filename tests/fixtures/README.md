# AISC v16 reference samples

`aisc_v16_samples.csv` contains values extracted from the US customary columns
of the AISC-authored **Shapes Database v16.0**, August 2023 (`Readme` and
`Database v16.0` sheets). It is independent of the package's CSV files.

- Publisher: https://www.aisc.org/aisc/publications/steel-construction-manual/aisc-shapes-database-v160/
- Workbook mirror: https://web.ics.purdue.edu/~jhunjhu0/Steel%20Design/aisc-shapes-database-v16.0.xlsx
- Retrieved: 2026-10-10. The publisher's workbook download returned HTTP 403;
  the workbook was obtained from Purdue's public steel-design course materials.
- Workbook SHA-256: `dec6202f8c2055bdefee9e13cb3d38e9110664c61dcf91d09604296ef2dcf660`

The samples cover all 14 profile families: weight, area, moment of inertia,
and selected dimensions and missing values. Source columns `W` and `A` map to
the library's `weight` and `area`. Section names use the library's underscore
convention and `DBL_L` prefix in place of `2L`; pipe names retain `Pipe` casing.
The source `–` marker means a property is not supplied.

During the CSV-loader replacement, every bundled section property was also
compared with this workbook. Numeric values were compared with a tolerance of
`1e-12` to account for Excel's floating-point representation. Future updates to
the source data should verify and update these samples intentionally.
