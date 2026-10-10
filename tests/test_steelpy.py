import copy
import csv
import math
import pickle
from pathlib import Path
import unittest

from steelpy import aisc


ROOT = Path(__file__).resolve().parents[1]


class SteelPyRegressionTests(unittest.TestCase):
    def test_representative_values_match_independent_aisc_source(self):
        path = ROOT / 'tests' / 'fixtures' / 'aisc_v16_samples.csv'
        with path.open(newline='', encoding='utf-8') as source:
            for row in csv.DictReader(source):
                with self.subTest(shape=row['shape'], property=row['property']):
                    section = getattr(getattr(aisc, row['profile']), row['shape'])
                    value = getattr(section, row['property'])
                    if row['value'] == '–':
                        self.assertTrue(math.isnan(value))
                    else:
                        self.assertTrue(math.isclose(value, float(row['value']),
                                                     rel_tol=1e-12, abs_tol=1e-12))

    def test_loaded_properties_match_csv_numbers(self):
        count = 0
        for path in (ROOT / 'steelpy' / 'shape files').glob('*.csv'):
            profile = getattr(aisc, path.stem)
            with path.open(newline='') as source:
                for row in csv.DictReader(source):
                    section = getattr(profile, row.pop('shape'))
                    count += 1
                    for prop, raw in row.items():
                        value = getattr(section, prop)
                        if raw == '–':
                            self.assertTrue(math.isnan(value), (section.name, prop))
                        else:
                            self.assertEqual(value, float(raw), (section.name, prop))
        self.assertEqual(len(aisc.profiles), 14)
        self.assertEqual(count, 2299)

    def test_missing_properties_are_excluded_from_bounds(self):
        cases = [
            ('W_shapes', 'WGo', 73), ('WT_shapes', 'WGo', 73),
            ('C_shapes', 'WGi', 24), ('MC_shapes', 'WGi', 33),
            ('M_shapes', 'WGi', 1), ('MT_shapes', 'WGi', 1),
            ('S_shapes', 'WGi', 21), ('ST_shapes', 'WGi', 21),
            ('L_shapes', 'H', 61), ('L_shapes', 'SwB', 76),
        ]
        for name, prop, count in cases:
            with self.subTest(profile=name, property=prop):
                profile = getattr(aisc, name)
                for bounds in ({'min': 0}, {'max': math.inf}):
                    result = profile.filter({prop: bounds})
                    self.assertEqual(len(result), count)
                    self.assertTrue(all(math.isfinite(getattr(s, prop))
                                        for s in result.values()))

                values = [getattr(s, prop)
                          for s in profile.filter({}, sort_by=prop).values()]
                self.assertEqual(values[:count], sorted(values[:count]))
                self.assertTrue(all(math.isnan(v) for v in values[count:]))
                self.assertEqual(len(values), len(profile.sections))

    def test_filter_bounds_are_inclusive_and_default_sort_is_weight(self):
        result = aisc.W_shapes.filter({'d': {'min': 8, 'max': 12.3},
                                      'Ix': {'min': 100}})
        self.assertEqual(len(result), 32)
        self.assertIn('W8X31', result)
        self.assertIn('W12X22', result)
        self.assertNotIn('W12X14', result)
        weights = [s.weight for s in result.values()]
        self.assertEqual(weights, sorted(weights))
        self.assertEqual(aisc.W_shapes.filter({'d': {'min': 1000}}), {})

    def test_filter_preserves_order_without_sorting_and_can_sort_names(self):
        result = aisc.W_shapes.filter({}, sort_by=None)
        self.assertEqual(list(result), list(aisc.W_shapes.sections))
        self.assertEqual(list(aisc.W_shapes.filter({}, sort_by='name')),
                         sorted(aisc.W_shapes.sections))
        with self.assertRaises(AttributeError):
            aisc.W_shapes.filter({'missing_property': {'min': 0}})

    def test_custom_missing_properties_are_excluded_and_sorted_last(self):
        from steelpy.steelpy import Profile, Section

        profile = Profile('custom')
        for name, value in [('absent', None), ('unknown', math.nan),
                            ('large', 10), ('zero', 0)]:
            section = Section(name)
            section.add_property('value', value)
            profile.add_section(name, section)
        self.assertEqual(list(profile.filter({'value': {'min': 0, 'max': 10}},
                                            sort_by='value')), ['zero', 'large'])
        self.assertEqual(list(profile.filter({}, sort_by='value')),
                         ['zero', 'large', 'absent', 'unknown'])
        self.assertEqual(profile.filter({'value': {'min': 11}}, sort_by=None), {})

    def test_objects_can_be_copied_and_restored(self):
        for original in (aisc, aisc.W_shapes, aisc.W_shapes.W12X26):
            with self.subTest(object_type=type(original).__name__):
                for restored in (copy.deepcopy(original),
                                 pickle.loads(pickle.dumps(original))):
                    self.assertIsNot(restored, original)
                    self.assertEqual(restored.name, original.name)
                    with self.assertRaises(AttributeError):
                        getattr(restored, 'missing_attribute')

        for restored in (copy.deepcopy(aisc), pickle.loads(pickle.dumps(aisc))):
            beam = restored.W_shapes.W12X26
            self.assertEqual(beam.Ix, 204.0)
            beam.properties['Ix'] = 0
            self.assertEqual(aisc.W_shapes.W12X26.Ix, 204.0)

    def test_readme_property_table_matches_available_attributes(self):
        table = (ROOT / 'README.md').read_text().split('### Property Table\n', 1)[1]
        table = table.split('### Property Descriptions', 1)[0]
        rows = [[c.strip() for c in line.split('|')[1:-1]]
                for line in table.splitlines() if line.startswith('|')]
        groups = [c.strip('*') + '_shapes' for c in rows[0][1:]]
        documented = set()
        for row in rows[2:]:
            prop = row[0].strip('*')
            documented.add(prop)
            for name, marker in zip(groups, row[1:]):
                section = next(iter(getattr(aisc, name).sections.values()))
                self.assertEqual(marker == '&check;', prop in section.properties,
                                 (name, prop))
        available = {prop for profile in aisc.profiles.values()
                     for prop in next(iter(profile.sections.values())).properties}
        self.assertEqual(documented, available)
        self.assertEqual(aisc.L_shapes.L4X4X1_4.t, 0.25)
        self.assertEqual(aisc.HSS_shapes.HSS12X12X1_2.h, 10.6)
        self.assertEqual(aisc.HSS_shapes.HSS12X12X1_2.B, 12.0)


if __name__ == '__main__':
    unittest.main()
