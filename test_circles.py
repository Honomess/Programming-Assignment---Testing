# test_circles.py

import unittest
from circles import area

class TestCircleArea(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(area(1), 3.14159, places=5)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(2.1), 13.85442, places=5)

if __name__ == '__main__':
    unittest.main()