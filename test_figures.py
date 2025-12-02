import unittest
import math

from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter


class TestCircleFunctions(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(2), math.pi * 4)
        self.assertAlmostEqual(circle_area(3.5), math.pi * 3.5 * 3.5)

    def test_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(0), 0)
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circle_perimeter(2), 4 * math.pi)
        self.assertAlmostEqual(circle_perimeter(3.5), 2 * math.pi * 3.5)

    def test_negative_values(self):
        self.assertAlmostEqual(circle_area(-2), math.pi * 4)
        self.assertAlmostEqual(circle_perimeter(-2), -4 * math.pi)


class TestSquareFunctions(unittest.TestCase):

    def test_area(self):
        self.assertEqual(square_area(0), 0)
        self.assertEqual(square_area(1), 1)
        self.assertEqual(square_area(2), 4)
        self.assertEqual(square_area(3.5), 3.5 * 3.5)

    def test_perimeter(self):
        self.assertEqual(square_perimeter(0), 0)
        self.assertEqual(square_perimeter(1), 4)
        self.assertEqual(square_perimeter(2), 8)
        self.assertEqual(square_perimeter(3.5), 4 * 3.5)

    def test_negative_values(self):
        self.assertEqual(square_area(-2), 4)
        self.assertEqual(square_perimeter(-2), -8)


if __name__ == "__main__":
    unittest.main()
