#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    
    pass

def get_age(birthyear):
    """ Raising manual exception """
    age = datetime.datetime.now().year - birthyear
    
    if age < 0:
        raise InvalidAgeError()
    else:
        return age
