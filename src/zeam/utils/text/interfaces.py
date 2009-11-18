
from zope import interface
from zope.schema import interfaces


class IText(interface.Interface):
    """Some text.
    """

    format = interface.Attribute(u"Name of the format")
    raw = interface.Attribute(u"Raw data")
    text = interface.Attribute(u"Rendered text")


class ITextFormat(interface.Interface):
    """A format to render text.
    """

    title = interface.Attribute(u"Name of the format")

    def render(data):
        """Render the given data using the format.
        """


class IAdvancedText(interfaces.IField):
    """A zope.schema field able to store Text.
    """
