"""

    Plone views overrides.

    For more information see

    * http://collective-docs.readthedocs.org/en/latest/views/browserviews.html

"""

# Zope imports
from zope.interface import Interface
from five import grok

# Local imports
from interfaces import IAddonSpecific

grok.layer(IAddonSpecific)


class VisualTitle(grok.View):
    """
    Extracts visual title from the content.
    """

    grok.context(Interface)

    def render(self):
        """

        """

        # Make sure we don't poke parent content properites thru acquisition chain
        context = self.context.aq_base

        # Check for visual title Archetypes override
        if hasattr(context, "Schema"):
            schema = context.Schema()
            if "visualTitle" in schema:
                field = schema["visualTitle"]
                visualTitle = field.get(self.context)

                # Check that visual title has string payload value
                if visualTitle:
                    return visualTitle

        # Check for normal title
        if hasattr(context, "Title"):
            return context.Title()

        return "Page title"
