#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 01."""


# Import Python libs
import unittest


# Import user libs
import task_01


class Task01TestCase(unittest.TestCase):
    """Task 01 tests"""

    msg = 'Failed to catch exception (v1: {}, v2: {})'

    def test_string_out_of_range(self):
        """Tests that the function works when a string is out of range."""
        v1 = 'a string'
        v2 = 99
        returned = task_01.simple_lookup(v1, v2)
        self.assertEqual(returned, v1, self.msg.format(v1, v2))

    def test_dict_no_key(self):
        """Tests that the function works when a dict has no key."""
        v1 = {'a': 'dict'}
        v2 = 99
        returned = task_01.simple_lookup(v1, v2)
        self.assertEqual(returned, v1, self.msg.format(v1, v2))

    def test_other_raises(self):
        """Tests that other exceptions continue to be raised normally."""
        with self.assertRaises(TypeError):
            task_01.simple_lookup(['a', 'list'], {'a': 'dict'})


if __name__ == '__main__':
    unittest.main()
