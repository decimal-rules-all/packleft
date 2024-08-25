import unittest

from packleft.model import DimensionedObject, Item, Box


class TestDimensionedObject(unittest.TestCase):
    """Test cases for DimensionedObject
    """

    def test_negative_dimension_should_throw_ValueError(self):
        with self.assertRaises(ValueError):
            DimensionedObject(-1, 2, 3)
        with self.assertRaises(ValueError):
            DimensionedObject(1, -2, 3)
        with self.assertRaises(ValueError):
            DimensionedObject(1, 2, -3)

    def test_volume_cacluation(self):
        dimensioned_object = DimensionedObject(1, 2, 3)
        self.assertEqual(dimensioned_object.volume, 6)


class TestItem(unittest.TestCase):
    """Test cases for Item
    """

    def test_negative_weight_should_throw_ValueError(self):
        with self.assertRaises(ValueError):
            Item(1, 2, 3, -1)


class TestBox(unittest.TestCase):
    """Test cases for Box
    """

    def test_negative_max_weight_should_throw_ValueError(self):
        with self.assertRaises(ValueError):
            Box(1, 2, 3, -1)