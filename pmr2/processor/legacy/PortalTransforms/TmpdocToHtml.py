from Products.PortalTransforms.interfaces import itransform

from pmr2.processor.legacy.transforms import tmpdoc2html

class TmpdocToHtml:
    """\
    TmpdocToHtml - Processes tmpdoc in CellML into HTML.
    """
    #wraps around tmpdoc2html for PortalTransforms.

    __implements__ = itransform

    __name__ = "pmr2_processor_legacy_tmpdoc2html"
    output = "text/html"

    def __init__(self, name=None, inputs=('text/xml', 'application/cellml+xml', 'application/xml',)):
        self.config = { 'inputs' : inputs, }
        self.config_metadata = {
            'inputs' : ('list', 'Inputs', 'Input(s) MIME type. Change with care.'),
            }
        if name:
            self.__name__ = name

    def name(self):
        return self.__name__

    def __getattr__(self, attr):
        if attr == 'inputs':
            return self.config['inputs']
        if attr == 'output':
            return self.config['output']
        raise AttributeError(attr)

    def convert(self, orig, data, **kwargs):
        # we return html string, not the StringIO object
        data.setData('%s' % tmpdoc2html(orig).getvalue())
        return data

def register():
    return TmpdocToHtml()

