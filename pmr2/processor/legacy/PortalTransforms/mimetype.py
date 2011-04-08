from Products.MimetypesRegistry.MimeTypeItem import MimeTypeItem

class application_cellml_xml(MimeTypeItem):

    __name__   = "CellML Media Type"
    mimetypes  = ('application/cellml+xml',)
    extensions = ('cellml',)
    binary     = 0
