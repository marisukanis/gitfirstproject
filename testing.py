import unittest
from test_func import area_of_a_square
import sys
""" 
unittest package (comes with python) or 
pytest (have to install - 'pip install pytest')

Run in terminal:
- python -m unittest filename.py
- python -m unittest filename.py - f (optional, if you want 
to stop executing test after the first error
- the usual: python testing.py

OK - shows that there are no errors
"""

class TestSomething(unittest.TestCase):
    def test_is_equals(self):
        #assertEqual means check if a == b
        self.assertEqual(10, 10)

    @unittest.skip('Skipping example')
    def test_is_equal_fails(self):
        self.assertEqual(True, False)

    def test_not_equal(self):
        self.assertNotEqual('Yellow', 'Blue')

    def test_is_in(self):
        self.assertIn(3, [7, 4, 5, 6, 8, 2, 3])

    def test_is_upper(self):
        txt = 'name'.upper()
        self.assertEqual('NAME', txt)

    def test_area_of_square(self):
        len = 20
        area = area_of_a_square(len)
        self.assertEqual(area, len*len)

    @unittest.skipIf(sys.platform.startswith('win'), 'skipping test for windows')
    def test_if_windows_os(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()