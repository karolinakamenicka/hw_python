import unittest

import calc

class TestCase(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(calc.sum(1, 1), 2)