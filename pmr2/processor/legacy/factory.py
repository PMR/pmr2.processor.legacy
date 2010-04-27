from cStringIO import StringIO

import zope.interface

from pmr2.processor.cmeta import Cmeta

from pmr2.app.content.interfaces import IExposureFile
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
        self.modeltitle = self.metadata.get_dc_title('')
        self.citation = None
        if self.cmetaids:
            self.citation = self.metadata.get_citation(self.cmetaids[0])

    # The find${Type}Title methods have fallback onto the other types.

    def findModelTitle(self):
        if self.modeltitle:
            return self.modeltitle[0]
        elif self.citation and self.citation[0]['title']:
            return self.citation[0]['title']

    def findCitationTitle(self):
        if self.citation and self.citation[0]['title']:
            return self.citation[0]['title']
        elif self.modeltitle:
            return self.modeltitle[0]

    def findCitationAuthors(self):
        if not self.citation:
            return None

        issued = self.citation[0]['issued']
        authors = ', '.join([c['family'] for c in self.citation[0]['creator']])
        if simple_valid_date(issued):
            # Got everything.
            return u'%s, %s' % (authors, issued[:4])
        else:
            # We could pull from workspace, but users can fix this on
            # their own.  Proper citation metadata spec, etc.
            return u'%s, ' % (authors,)

    def generateTitle(self):
        # the fallbacks assume context is an atct type.
        if IExposureFile.providedBy(self.context):
            # since this is an exposure file, we will need to derive the
            # model/citation file as this should be the actual file that
            # contain the documentation.
            return self.findModelTitle() or self.context.Title()

        # otherwise, we just use the list of authors if citation is
        # found, for there are expectations for the listing to be the
        # same as how PMR1 did it.
        return self.findCitationAuthors() or self.context.Title()

    def generateDescription(self):
        # the fallbacks assume context is an atct type.
        # Since ExposureFiles don't usually show this field, the special
        # rule here applies to Exposures.  In the name of following the
        # footsteps of PMR1, the description will be the title of the
        # citation.
        return self.findCitationTitle() or self.context.Description()

CellMLTmpDocViewGenFactory = named_factory(CellMLTmpDocViewGen)
