from cStringIO import StringIO

import zope.interface

from pmr2.processor.cmeta import Cmeta

from pmr2.app.content.interfaces import IExposure
from pmr2.app.annotation.interfaces import IDocViewGen
from pmr2.app.factory import named_factory
from pmr2.app.annotation.viewgen import PortalTransformDocViewGenBase
from pmr2.app.util import simple_valid_date


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
        self.modelinfo = self.metadata.get_dc_vcard_info('')
        self.citation = None
        if self.cmetaids:
            self.citation = self.metadata.get_citation(self.cmetaids[0])

    def findModelTitle(self):
        if self.modelinfo and self.modelinfo[0]['title']:
            return self.modelinfo[0]['title']
        elif self.citation and self.citation[0]['title']:
            return self.citation[0]['title']
        else:
            return self.context.Title()

    def generateTitle(self):
        if not IExposure.providedBy(self.context):
            # normally we just return the citation title
            return self.findModelTitle()

        # This overrides default like so because of PMR1.
        if not self.citation:
            # unchanged
            # XXX assuming ATCT
            return self.context.Title()

        # however for the root object, we want the list of authors.
        issued = self.citation[0]['issued']
        authors = ', '.join([c['family'] for c in self.citation[0]['creator']])
        if simple_valid_date(issued):
            # Got everything.
            return u'%s, %s' % (authors, issued[:4])
        else:
            # We could pull from workspace, but users can fix this on
            # their own.  Proper citation metadata spec, etc.
            return u'%s, ' % (authors,)

    def generateDescription(self):
        title = self.findModelTitle() or self.context.Description()
        return title

CellMLTmpDocViewGenFactory = named_factory(CellMLTmpDocViewGen)
