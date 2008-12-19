import unittest
import os
from os.path import dirname, join
from cStringIO import StringIO

from pmr2.processor.legacy import *
from pmr2.processor.legacy import tmpdoc

testroot = dirname(__file__)

class RootTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_basic(self):
        f = StringIO('<egg><bacon>Hamburger</bacon></egg>')
        result = apply_xslt(f, 'test.xslt').getvalue()
        self.assertEqual(result, '<bread>Hamburger</bread>')

    def test_tmpdoc(self):
        f = open(join(testroot, 'input.cellml'))
        result = tmpdoc.tmpdoc2html(f).getvalue()
        # just a simple test is good enough for now.
        self.assert_('<h4>Model Structure</h4>' in result)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RootTestCase))
    return suite

if __name__ == '__main__':
    unittest.main()

