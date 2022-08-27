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

