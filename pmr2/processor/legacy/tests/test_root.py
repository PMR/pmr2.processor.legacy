import unittest
import os
from os.path import dirname, join
from cStringIO import StringIO

from pmr2.processor.legacy import *

class RootTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_basic(self):
        f = StringIO('<egg><bacon>Hamburger</bacon></egg>')
        result = apply_xslt(f, 'test.xslt').getvalue()
        self.assertEqual(result, '<bread>Hamburger</bread>')


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RootTestCase))
    return suite

if __name__ == '__main__':
    unittest.main()

