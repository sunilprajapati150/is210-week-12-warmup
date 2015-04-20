#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 02."""


# Import Python libs
import datetime
import unittest


# Import user libs
import task_02


class Task02TestCase(unittest.TestCase):
    """Task 02 tests"""

    def test_valid_age(self):
        """Tests that the valid age is returned."""
        age = 40
        year = datetime.datetime.now().year - age
        returned = task_02.get_age(year)
        self.assertEqual(returned, age)

    def test_invalid_age(self):
        """Tests that an invalid age forces an exception."""
        age = -40
        year = datetime.datetime.now().year - age

        with self.assertRaises(task_02.InvalidAgeError):
            returned = task_02.get_age(year)


if __name__ == '__main__':
    unittest.main()
