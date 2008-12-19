from pmr2.processor.legacy import apply_xslt, StringIO

def tmpdoc2html(input):
    """\
    Given input CellML file object or string, apply xslt to extract
    the documentation and render it into html.
    """

    if isinstance(input, basestring):
        input = StringIO(input)
    elif not hasattr(input, 'read'):  # assume read is filelike
        raise TypeError('input must be filelikee')
    xslt_file = 'cellml_tmpdoc-to-html.xslt'
    try:
        result = apply_xslt(input, xslt_file)
    except:
        # XXX figure out if we want to trap this here or earlier
        raise

    # FIXME
    # Additional steps taken by PMR (such as replacement of variables
    # to point to correct URI) should be implemented here.
    return result
