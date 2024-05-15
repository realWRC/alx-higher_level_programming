#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Testing class for mobule Base"""
    def test_instance(self):
        b1 = Base()
        self.assertIsInstance(b1, Base)

    def test_cls_variable(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)


if __name__ == "__main__":
    unittest.main()
