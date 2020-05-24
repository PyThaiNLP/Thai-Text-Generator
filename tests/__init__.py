# -*- coding: utf-8 -*-
"""
Unit test.
"""
import sys
import unittest

sys.path.append("../thaitextgenerator")

loader = unittest.TestLoader()
testSuite = loader.discover("tests")
testRunner = unittest.TextTestRunner(verbosity=2)
testRunner.run(testSuite)
