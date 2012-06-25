"""

    Zope 2 style module init

"""

# W0613:  7,15:initialize: Unused argument 'context'
# pylint: disable=W0613

from zope.i18nmessageid import MessageFactory

_ = MessageFactory("visualtitle")


def initialize(context):
    """ Zope 2 init code goes here.

    Usually there is nothing to go here,
    so move foward.
    """

