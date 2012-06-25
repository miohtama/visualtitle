"""

    Add visual title field to Archetypes content.


"""

# Python imports
import logging

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
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.field import ExtensionField

logger = logging.getLogger("visualtitle")


class ExtensionStringField(ExtensionField, atapi.StringField):
    """ Enhance bool field  to be used with schema extender"""


class VisualTitleExtender(grok.Adapter):
    """
    Define schema fiddler which injects a new field to every item.
    """

    grok.context(IBaseObject)
    grok.implements(IOrderableSchemaExtender)
    grok.name("visualtitle")

    fields = [
            ExtensionStringField("visualTitle",
                widget=atapi.StringWidget(
                    label="Visual Title",
                    description="Different title for in-page text (as opposite to navigation title). Leave empty to use the main title everywhere."
                ),
                default="",
                # On which edit tab this field appears
                languageIndependent=False
            )
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        """ Manipulate the order in which fields appear.

        @param schematas: Dictonary of schemata name -> field lists

        @return: Dictionary of reordered field lists per schemata.
        """

        # Replace the field order for the "default" schemata
        default = schematas["default"]

        default.remove("visualTitle")

        # Insert as 2nd field
        default.insert(2, "visualTitle")

        return schematas

    def getFields(self):
        return self.fields

