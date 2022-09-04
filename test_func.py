import unittest

def area_of_a_square(length):
     return length ** 2

"""
Test Fixture: setUp and tearDown

setUp = called immediately before your test method
tearDown - called after your test method is executed
"""

class TestFixture(unittest.TestCase):
    def setUp(self) -> None:
        print('This is a setup method')
        self.list1 = [2,3,4,5,6,7]

    def test_value_in_list(self):
        print('test value')
        self.assertIn(4, self.list1)

    def tearDown(self) -> None:
        print('Tear down')
        del self.list1

    def test_true_is_true(self):
        self.assertTrue(True)

    def test_exception(self):
        with self.assertRaises(ZeroDivisionError):
            10/0

    def test_exception_name_error(self):
        with self.assertRaises(NameError):
            print(xyzz)
