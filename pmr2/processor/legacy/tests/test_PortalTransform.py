"""\
Test case to be sure that these works as PortalTransforms within Plone.
"""

from os.path import abspath, dirname, join
from Products.PortalTransforms.tests.test_transforms import make_tests, \
    TransformTest, load

PREFIX = abspath(dirname(__file__))

def input_file_path(file):
    return join(PREFIX, 'input', file)

def output_file_path(file):
    return join(PREFIX, 'output', file)

TRANSFORMS_TESTINFO = (
    ('pmr2.processor.legacy.PortalTransforms.TmpdocToHtml', 
    'basic.cellml', 'basic.html', None, 0,),
)


def make_tests(test_descr=TRANSFORMS_TESTINFO):
    """generate tests classes from test info

    return the list of generated test classes
    """
    tests = []
    for _transform, tr_input, tr_output, _normalize, _subobjects in test_descr:
        # load transform if necessary
        if type(_transform) is type(''):
            try:
                _transform = load(_transform).register()
            except MissingBinary:
                # we are not interessted in tests with missing binaries
                continue
            except:
                import traceback
                traceback.print_exc()
                continue

        class TransformTestSubclass(TransformTest):
            input = input_file_path(tr_input)
            output = output_file_path(tr_output)
            transform = _transform
            normalize = None
            subobjects = _subobjects

        tests.append(TransformTestSubclass)

    return tests

def test_suite():
    from unittest import TestSuite, makeSuite
    return TestSuite([makeSuite(test) for test in make_tests()])

