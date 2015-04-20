#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03."""


# Import Python libs
import datetime
import unittest


# Import user libs
import task_03


class Task03TestCase(unittest.TestCase):
    """Task 03 tests"""

    def test_flush_is_successful(self):
        """Tests if the flush command successfully clears messages."""
        logger = task_03.CustomLogger('test_flush_successful.log')
        logger.log('one')
        logger.log('two')
        self.assertEqual(len(logger.msgs), 2)
        logger.flush()
        self.assertEqual(len(logger.msgs), 0)

    def test_flush_handles_bad_open(self):
        """Flush logs but encounters a file path it cannot open."""
        with self.assertRaises(IOError):
            logger = task_03.CustomLogger('/my/crazy/pathname/whatever.log')
            logger.log('one')
            logger.log('two')
            self.assertEqual(len(logger.msgs), 3, 'Logger missing messages.')
            logger.flush()


if __name__ == '__main__':
    unittest.main()
