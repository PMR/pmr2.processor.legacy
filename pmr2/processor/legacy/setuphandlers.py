"""
Plone PortalTransforms stuff

This module enables Plone to turn this module into a proper transform
using setup handlers.
"""

from StringIO import StringIO
from Products.CMFCore.utils import getToolByName
from types import InstanceType

from pmr2.processor.legacy.PortalTransforms import TmpdocToHtml
from pmr2.processor.legacy.PortalTransforms.mimetype import \
    application_cellml_xml

def registerMimeType(self, out, mimetype):
    if type(mimetype) != InstanceType:
        mimetype = mimetype()
    mimetypes_registry = getToolByName(self, 'mimetypes_registry')
    mimetypes_registry.register(mimetype)
    print >> out, 'Registered mimetype', mimetype

# not going to unregister mimetypes

def install(context):
    """
    Step to setup the transforms
    """
    # Only run step if a flag file is present (e.g. not an extension profile)
    print 'BEFORE INSTALL'
    if context.readDataFile('transform-install.txt') \
            is None:
        return

    out = StringIO()
    site = context.getSite()
    print 'CALLING INSTALL'

    print >> out, 'Registering CellML mimetype and legacy PMR transforms'
    registerMimeType(site, out, application_cellml_xml)

    engine = getToolByName(site, 'portal_transforms')
    engine.registerTransform(TmpdocToHtml.register())
    print >> out, 'CellML tmpdoc to HTML transform registered.'

    return out.getvalue()


def uninstall(context):
    """
    Step to remove the transforms
    """
    # Only run step if a flag file is present (e.g. not an extension profile)
    print 'CALLING UNINSTALL'
    if context.readDataFile('transform-uninstall.txt') \
            is None:
        return

    out = StringIO()
    site = context.getSite()

    print 'CALLING UNINSTALL'
    transforms = (
        'pmr2_processor_legacy_tmpdoc2html',
    )

    engine = getToolByName(site, 'portal_transforms')
    for name in transforms:
        try:
            engine.unregisterTransform(name)
            print >> out, "Removed transform", name
        except AttributeError:
            print >> out, "Could not remove transform", name, "(not found)"

    return out.getvalue()
