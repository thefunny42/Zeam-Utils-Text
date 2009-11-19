
from zope import schema, interface, component
from zope.schema.interfaces import InvalidValue

from zeam.utils.text.interfaces import IAdvancedText, IText, ITextFormat


class Text(object):
    """This represent text and is stored on a object.
    """
    interface.implements(IText)

    def __init__(self, text=None, format='raw'):
        self.__text = u''
        self.__raw = u''
        self.format = format
        if text is not None:
            self.raw = text

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


