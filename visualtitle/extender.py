"""

    Add visual title field to Archetypes content.


"""

# Zope imports
from five import grok

# Plone imports
try:
    from Products.LinguaPlone import atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi

from Products.Archetypes.interfaces import IBaseObject

# 3rd party
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender, ISchemaModifier
from archetypes.schemaextender.field import ExtensionField

from .interfaces import IAddonSpecific
from visualtitle import _


class ExtensionStringField(ExtensionField, atapi.StringField):
    """ Enhance bool field  to be used with schema extender"""

FIELDS = [
        ExtensionStringField("visualTitle",
            widget=atapi.StringWidget(
                label=_(u"Visual Title"),
                description=_(u"Different title for in-page text (as opposite to navigation title). Leave empty to use the main title everywhere."),
            ),
            default="",
            # On which edit tab this field appears
            languageIndependent=False
        )
]


class VisualTitleExtender(grok.Adapter):
    """
    Define schema fiddler which injects a new field to every item.
    """

    grok.context(IBaseObject)
    # Tell that we fiddle()
    grok.provides(ISchemaModifier)

    # Tell that we getOrder() + we are bound to a layer
    grok.implements(IBrowserLayerAwareExtender)
    grok.name("visualtitle")

    layer = IAddonSpecific

    def getFields(self):
        return self.fields

    def fiddle(self, schema):
        """
        Override main title description
        """

        # Add visualTitle field
        for field in FIELDS:
            schema.addField(field)

        schema.moveField("visualTitle", after="title")

        schema["title"].description = _(u"The navigational heading of the content")


