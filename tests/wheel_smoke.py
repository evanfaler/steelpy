"""Run with python -I after installing the wheel into a clean environment."""
import importlib.metadata
import math
from pathlib import Path
import sys
import unittest

import steelpy
from steelpy import aisc


class InstalledWheelTests(unittest.TestCase):
    def test_wheel_has_all_profiles_and_no_runtime_dependencies(self):
        repository = Path(__file__).resolve().parents[1]
        self.assertNotIn(repository, Path(steelpy.__file__).resolve().parents)
        self.assertFalse(importlib.metadata.requires('steelpy'))
        self.assertEqual(len(aisc.profiles), 14)
        self.assertEqual(sum(len(p.sections) for p in aisc.profiles.values()), 2299)
        self.assertEqual(aisc.W_shapes.W12X26.Ix, 204.0)
        self.assertTrue(math.isnan(aisc.W_shapes.W14X90.WGo))
        self.assertEqual(len(aisc.W_shapes.filter({'WGo': {'min': 0}})), 73)
        self.assertTrue({'pandas', 'numpy', 'openpyxl'}.isdisjoint(sys.modules))


if __name__ == '__main__':
    unittest.main()
