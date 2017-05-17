from unittest import TestCase

class TestBuild(TestCase):
    #check the array is not null
    #check the araay on search gives indice number
    #check if the array gives none if there are no values in given value
    def test_check_the_array_is_not_null(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Failure")

        res = build(None,None)
        self.assertEqual(False,res)

    def test_check_the_araay_on_search_gives_indice_number(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Failure")

        res = build([[12,3,0,5]], 5)
        self.assertEqual((0,3), res)

    def test_if_the_array_gives_none_if_there_are_no_values_in_given_value(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Failure")

        res = build([[12, 3, 0, 5]], 2)
        self.assertEqual(None, res)