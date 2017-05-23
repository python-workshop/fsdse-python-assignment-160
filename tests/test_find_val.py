from unittest import TestCase


class TestFind_val(TestCase):
    def test_find_val(self):
        try:
            from build import find_val
        except ImportError:
            self.assertFalse("no function found")

        matrix = [[20, 40, 63, 80],
                  [30, 50, 80, 90],
                  [40, 60, 110, 110],
                  [50, 65, 105, 150]]

        self.assertRaises(TypeError, find_val, None, None)
        self.assertEqual(find_val(matrix, 1000), None)
        self.assertEqual(find_val(matrix, 60), (2, 1))
