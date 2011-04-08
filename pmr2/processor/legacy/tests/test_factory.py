from os.path import join, dirname
from unittest import TestCase, TestSuite, makeSuite
from zope.interface import implements, directlyProvides
from zope.component import provideAdapter

from pmr2.app.annotation.interfaces import IExposureDocViewGenSourceAdapter
from pmr2.app.exposure.interfaces import IExposureFile

from pmr2.processor.legacy.factory import CellMLTmpDocViewGen

default_title = u'<Default Title>'
default_description = u'<Default Description>'

def get_path(filename):
    return join(dirname(__file__), 'input', filename)


class MockContent:
    def __init__(self, filename):
        self.filename = filename

    # since the generator assumes atct types, we mock those methods.
    def Title(self):
        return default_title

    def Description(self):
        return default_description


class MockSource:
    implements(IExposureDocViewGenSourceAdapter)

    def __init__(self, context):
        self.context = context

    def file(self):
        f = open(get_path(self.context.filename))
        result = f.read()
        f.close()
        return result


class TestFactory(TestCase):

    def setUp(self):
        provideAdapter(MockSource, (MockContent,), 
            IExposureDocViewGenSourceAdapter)

    def testCellMLTmpDocViewGen_010_std_no_title(self):
        content = MockContent('Bucket.cellml')
        generator = CellMLTmpDocViewGen(content)
        title = generator.generateTitle()
        description = generator.generateDescription()
        self.assertEqual(title, default_title)
        self.assertEqual(description, default_description)

    def testCellMLTmpDocViewGen_011_file_no_title(self):
        content = MockContent('Bucket.cellml')
        # make content be an ExposureFile
        directlyProvides(content, IExposureFile)
        generator = CellMLTmpDocViewGen(content)
        title = generator.generateTitle()
        description = generator.generateDescription()
        self.assertEqual(title, default_title)
        # this is untouched and unused but generated.
        self.assertEqual(description, default_description)

    def testCellMLTmpDocViewGen_020_std_cit_title(self):
        content = MockContent('basic.cellml')
        generator = CellMLTmpDocViewGen(content)
        title = generator.generateTitle()
        description = generator.generateDescription()
        self.assertEqual(title, 'Family1, Family2, Family3, 2004')
        self.assertEqual(description, 'Basic Test Title')

    def testCellMLTmpDocViewGen_021_file_cit_title(self):
        content = MockContent('basic.cellml')
        # make content be an ExposureFile
        directlyProvides(content, IExposureFile)
        generator = CellMLTmpDocViewGen(content)
        title = generator.generateTitle()
        description = generator.generateDescription()
        self.assertEqual(title, 'Basic Test Title')
        self.assertEqual(description, 'Basic Test Title')

    def testCellMLTmpDocViewGen_030_std_mod_title(self):
        content = MockContent('terms.cellml')
        generator = CellMLTmpDocViewGen(content)
        title = generator.generateTitle()
        description = generator.generateDescription()
        self.assertEqual(title, 'Family1, Family2, Family3, 2004')
        # still uses the citation title for this is shown on the main
        # listing
        self.assertEqual(description, 'Basic Test Title')

    def testCellMLTmpDocViewGen_031_file_mod_title(self):
        content = MockContent('terms.cellml')
        # make content be an ExposureFile
        directlyProvides(content, IExposureFile)
        generator = CellMLTmpDocViewGen(content)
        title = generator.generateTitle()
        description = generator.generateDescription()
        # still uses the mode title for this is shown under navigation
        # menu and category (catalog) listings, where citations may be
        # duplicated and need the file title to resolve the differences.
        self.assertEqual(title, 'Model Titled')
        # this is untouched and unused but generated as usual.
        self.assertEqual(description, 'Basic Test Title')


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(TestFactory))
    return suite

