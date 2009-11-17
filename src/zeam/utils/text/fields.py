
from zope import schema, interface
from zope.schema.interfaces import InvalidValue

from zeam.utils.text.interfaces import IAdvancedText


class Text(object):
    """This represent text and is stored on a object.
    """

    format = 'raw'
    data = ''


class AdvancedText(schema.Field):
    """This represent a zope.schema field for our Text.
    """
    interface.implements(IAdvancedText)

    def validate(self, obj):
        if not isinstance(obj, Text):
            raise InvalidValue


