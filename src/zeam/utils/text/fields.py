
from zope import schema, interface, component
from zope.schema.interfaces import InvalidValue

from zeam.utils.text.interfaces import IAdvancedText, IText, ITextFormat


class Text(object):
    """This represent text and is stored on a object.
    """
    interface.implements(IText)

    def __init__(self):
        self.__text = None
        self.__raw = None

    format = 'raw'

    @apply
    def raw():
        def get(self):
            return self.__raw
        def set(self, value):
            renderer = component.getUtility(ITextFormat, name=self.format)
            self.__text = renderer.render(value)
            self.__raw = value
        return property(get, set)

    @property
    def text(self):
        return self.__text


class AdvancedText(schema.Field):
    """This represent a zope.schema field for our Text.
    """
    interface.implements(IAdvancedText)

    def validate(self, obj):
        if not isinstance(obj, Text):
            raise InvalidValue('Not text')


