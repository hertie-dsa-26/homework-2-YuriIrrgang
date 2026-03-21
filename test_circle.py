from circle import Circle
import unittest
import math

class TestCircle(unittest.TestCase):

    def test_circumference(self):
        circle = Circle(1)
        expected_value = 2 * math.pi
        result = circle.circumference()
        self.assertAlmostEqual(result, expected_value)

    def test_area(self):
        circle = Circle(1)
        expected_value = math.pi
        result = circle.area()
        self.assertAlmostEqual(result, expected_value)
    
if __name__ == '__main__':
    unittest.main()



