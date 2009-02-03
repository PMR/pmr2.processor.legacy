import unittest
import os
from os.path import dirname, join
from cStringIO import StringIO

from pmr2.processor.legacy import *
from pmr2.processor.legacy import transforms

testroot = dirname(__file__)
input_dir = join(testroot, 'input')
output_dir = join(testroot, 'output')

class RootTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_basic(self):
        f = StringIO('<egg><bacon>Hamburger</bacon></egg>')
        result = apply_xslt(f, 'test.xslt').getvalue()
        self.assertEqual(result, '<bread>Hamburger</bread>')

    def test_tmpdoc2html_basic(self):
        f = open(join(input_dir, 'basic.cellml'))
        result = transforms.tmpdoc2html(f).getvalue()
        i = open('/dev/shm/fail', 'w')
        i.write(result)
        i.close()
        # just a simple test is good enough for now.
        self.assert_('<h4>Model Structure</h4>' in result)

    def test_tmpdoc2html_with_terms(self):
        f = open(join(input_dir, 'terms.cellml'))
        result = transforms.tmpdoc2html(f).getvalue()
        # just a simple test is good enough for now.
        self.assert_('${HTML_EXMPL_ALBRECHT_MODEL1}' not in result)
        self.assert_('/albrecht_colegrove_hongpaisan_pivovarova_andrews_friel_2001_version01">' in result)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RootTestCase))
    return suite

if __name__ == '__main__':
    unittest.main()

