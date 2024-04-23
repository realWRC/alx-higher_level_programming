#!/usr/bin/python3
""" Unittests for class Base. """


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test class for class Base. """

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_01(self):
        """ Create instances of class and check id. """
        base_1 = Base()
        self.assertEqual(base_1.id, 1)
        base_2 = Base()
        self.assertEqual(base_2.id, 2)
        base_3 = Base(-9)
        self.assertEqual(base_3.id, -9)
        base_4 = Base(0)
        self.assertEqual(base_4.id, 0)
        base_5 = Base(9109)
        self.assertEqual(base_5.id, 9109)

    def test_02(self):
        """ Checks instance type """
        base_1 = Base()
        self.assertEqual(type(base_1), Base)
        self.assertTrue(isinstance(base_1, Base))


if __name__ == '__main__':
    unittest.main()
