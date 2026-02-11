"""
Basic tests for the Octonion class.
"""

import unittest
from src.octonion import Octonion

class TestOctonion(unittest.TestCase):
    def test_init(self):
        o = Octonion([1,2,3,4,5,6,7,8])
        self.assertEqual(o.components, [1,2,3,4,5,6,7,8])

    def test_invalid_init(self):
        with self.assertRaises(ValueError):
            Octonion([1,2,3])

if __name__ == "__main__":
    unittest.main()
