#!/usr/bin/env python
# -*- coding: latin1 -*-

"""
Configuration file
"""

import os

def base_directory():
    """Returns the base directory"""
    return os.path.dirname(os.path.realpath(__file__)) + os.path.sep

def icon_directory():
    """Returns the location of the icons"""
    return os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "./images" + os.path.sep

if __name__ == "__main__":
    print __doc__
