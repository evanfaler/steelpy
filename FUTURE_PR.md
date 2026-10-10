# Repository audit follow-up status

The four must-fix findings and the following cleanup items are implemented.
Numbering matches the original audit.

- [x] **5. Refresh dependency resolution.** Poetry regenerated the lockfile for
  Python `^3.9`, and `poetry check --lock` passes. The exported requirements are
  empty because the package now has no third-party runtime dependencies. The
  homepage was moved into the existing Poetry metadata table so modern Poetry
  accepts the configuration.
- [x] **6. Expand automated verification.** Eight regression tests pass locally
  on Python 3.9–3.14. A source distribution and a wheel were built, and the wheel
  passes an isolated import check in clean environments on all six versions.
  CI repeats the source tests, distribution builds, and clean-wheel check on
  Python 3.9–3.14. Independent AISC v16 reference samples cover all 14 families;
  all 51,897 bundled property values were compared with the AISC-authored
  workbook from Purdue's public course materials, with no differences beyond
  floating-point representation. See `tests/fixtures/README.md` for provenance.
- [x] **7. Remove the unused Excel dependency.** `openpyxl` and `et-xmlfile` are
  gone, along with pandas and its dependencies. Installed-wheel metadata has
  no runtime dependency requirements; it loads all 14 profiles and 2,299 sections.
- [x] **8. Delete dead code.** Removed the unused `namedtuple` import and the
  duplicate `filtered_dict = {}` assignment.

Remaining verification: GitHub Actions has not run remotely. Python 3.15 was
released on 2026-10-09, but its final runtime was not available in the temporary
runtime installer or GitHub Actions manifest during this work. Add it to the
matrix when available. AISC's direct workbook download still returns HTTP 403;
the independent reference workbook was obtained from the documented Purdue mirror.
