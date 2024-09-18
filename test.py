import unittest
import main
from io import StringIO
from test_base import captured_io,captured_output

class TestMyTest(unittest.TestCase):
    def test_even_numbers(self):
        output=main.even_numbers([2,4,20,45])
        self.assertEqual(output,[2,4,20])
        self.assertNotEqual(output,[2,4,20,45])

    def test_odd_numbers(self):
         output=main.odd_numbers([3,4,5,6,7]) 
