from cStringIO import StringIO

import zope.interface

from pmr2.processor.cmeta import Cmeta

from pmr2.app.interfaces import IDocViewGen
from pmr2.app.factory import named_factory, PortalTransformDocViewGenBase


class CellMLTmpDocViewGen(PortalTransformDocViewGenBase):
    zope.interface.implements(IDocViewGen)
    transform = 'pmr2_processor_legacy_tmpdoc2html'
    title = u'CellML-tmpdoc View Generator'
    description = u'This converts CellML files with legacy tmp-doc nodes ' \
                   'into html to be included in the pages.'

    def __init__(self, *a, **kw):
        super(CellMLTmpDocViewGen, self).__init__(*a, **kw)
        self.metadata = Cmeta(StringIO(self.input))
        self.cmetaids = self.metadata.get_cmetaid()
        self.citation = self.metadata.get_citation(self.cmetaids[0])

    def generateTitle(self):
        return self.citation[0]['title']

    def generateDescription(self):
        return self.citation[0]['title']

CellMLTmpDocViewGenFactory = named_factory(CellMLTmpDocViewGen)
