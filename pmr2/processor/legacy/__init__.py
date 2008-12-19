import os.path
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

xsltroot = os.path.join(os.path.dirname(__file__), 'xslt')

from lxml import etree 

__all__ = ['apply_xslt',]

def xslt_transform(input, xslt):
    """\
    XSLT transform.

    input - File-like object to be transformed.
    xslt - File-like object containing the XSLT.

    Returns an xslt transform result object.
    """

    xslt_doc = etree.parse(xslt)
    transform = etree.XSLT(xslt_doc)
    input_doc = etree.parse(input)
    result = transform(input_doc)
    return result

def apply_xslt(input, xsltfile, xsltpath=xsltroot):
    """\
    Takes in an xsltfile name, and an input.

    Returns StringIO containing result.
    """

    xslt_fp = os.path.join(xsltpath, xsltfile)
    xslt = open(xslt_fp)
    xslt_result = xslt_transform(input, xslt)
    result = StringIO()
    xslt_result.write(result)
    return result
