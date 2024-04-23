#!/usr/bin/python3
""" Unittests for the class Rectagle """


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Tests for class Rectangle """

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_2_0(self):
        """ Check id unittest """
        rec_1 = Rectangle(97, 9)
        self.assertEqual(rec_1.id, 1)
        rec_2 = Rectangle(9, 8)
        self.assertEqual(rec_2.id, 2)
        rec_3 = Rectangle(8, 9, 17, 3, 89)
        self.assertEqual(rec_3.id, 89)
        rec_4 = Rectangle(90, 18, 78, 76, -111)
        self.assertEqual(rec_4.id, -111)

    def test_2_1(self):
        """ Checks for type and inheritance """
        rec_1 = Rectangle(10, 98)
        self.assertTrue(type(rec_1), Rectangle)
        self.assertTrue(isinstance(rec_1, Base))
        self.assertFalse(isinstance(Rectangle, Base))
        self.assertTrue(issubclass(Rectangle, Base))

    def test_2_2(self):
        rec_1 = Rectangle(89, 78)
        self.assertEqual(rec_1.height, 78)
        self.assertEqual(rec_1.width, 89)
        self.assertEqual(rec_1.x, 0)
        self.assertEqual(rec_1.y, 0)
        rec_1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rec_1.height, 2)
        self.assertEqual(rec_1.width, 1)
        self.assertEqual(rec_1.x, 3)
        self.assertEqual(rec_1.y, 4)


if __name__ == "__main__":
    unittest.main()
