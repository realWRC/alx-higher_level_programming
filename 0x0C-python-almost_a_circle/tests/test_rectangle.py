#!/usr/bin/python3
"""Defines Unit tests for the Base subclass Rectangle"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Tests for the Rectangle Class """

    def test_parent_attribute(self):
        r1 = Rectangle(10, 10)
        r2 = Rectangle(10, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_attributes(self):
        r1 = Rectangle(10, 90, 1, 2, 25)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 90)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 25)

    def test_instance(self):
        r1 = Rectangle(10, 10)
        self.assertIsInstance(r1, Rectangle)
        self.assertTrue(issubclass(Rectangle, Base), True)

    def test_validation(self):
        r1 = Rectangle(5, 5)
        with self.assertRaises(ValueError):
            r1.width = -10
        with self.assertRaises(ValueError):
            r1.height = -10
        with self.assertRaises(ValueError):
            r1.x = -5
        with self.assertRaises(ValueError):
            r1.width = -5
        with self.assertRaises(TypeError):
            r1.width = "string"
        with self.assertRaises(TypeError):
            r1.height = "string"
        with self.assertRaises(TypeError):
            r1.x = "string"
        with self.assertRaises(TypeError):
            r1.width = "string"
        with self.assertRaises(TypeError):
            r2 = Rectangle("string", 10)
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, "string")

    def test_area(self):
        r1 = Rectangle(5, 5)
        self.assertEqual(r1.area(), 25)
        r2 = Rectangle(10, 5)
        self.assertEqual(r2.area(), 50)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)


if __name__ == "__main__":
    unittest.main()
