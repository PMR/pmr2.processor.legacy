import re
from pmr2.processor.legacy import apply_xslt, StringIO
from pmr2.processor.legacy.utils import makefileTerms

def tmpdoc2html(input):
    """\
    Given input CellML file object or string, apply xslt to extract
    the documentation and render it into html.

    input - should be a string.
    """

    if hasattr(input, 'read') and hasattr(input, 'seek'):
        # assume read is file-like, otherwise treat it as string
        input.seek(0)
        input = input.read()

    input = re.sub('<para>\r?\nThe model has been described here in CellML.*sec_download_this_model"/>\)\. *\r?\n</para>', '', input)
    input = makefileTerms(input)

    xslt_file = 'cellml_tmpdoc-to-html.xslt'
    input = StringIO(input)
    try:
        result = apply_xslt(input, xslt_file)
    except:
        # XXX figure out if we want to trap this here or earlier
        raise

    return result
