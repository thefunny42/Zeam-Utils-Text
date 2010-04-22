
from zeam.form.base import NO_VALUE
from zeam.form.base.widgets import FieldWidget, DisplayFieldWidget, \
    WidgetExtractor
from zeam.form.ztk.fields import SchemaField, registerSchemaField
from zeam.utils.text.interfaces import IAdvancedText
from zeam.utils.text.fields import Text
from zeam.utils.text.format import availableFormat

from zope.interface import Interface

from grokcore import component as grok


class AdvancedTextSchemaField(SchemaField):
    """An advanced text field.
    """

    def availableFormats(self):
        return availableFormat()


registerSchemaField(AdvancedTextSchemaField, IAdvancedText)


class AdvancedTextFieldWidget(FieldWidget):
    """Input widget for text field.
    """
    grok.adapts(AdvancedTextSchemaField, Interface, Interface)

    def prepareContentValue(self, value):
        formattedValue = u''
        formattedFormat = 'raw'
        if value is not NO_VALUE:
            formattedValue = unicode(value.raw)
            formattedFormat = value.format
        return {self.identifier: formattedValue,
                self.formatIdentifier: formattedFormat}

    def isFormat(self, format):
        return self.inputValue('format') == format and 'checked' or None

    def update(self):
        self.formatIdentifier = self.identifier + '.format'
        self.formats = self.component.availableFormats()
        super(AdvancedTextFieldWidget, self).update()


class AdvancedTextWidgetExtractor(WidgetExtractor):
    """Widget extractor for text field.
    """
    grok.adapts(AdvancedTextSchemaField, Interface, Interface)

    def extract(self):
        text = self.request.form.get(self.identifier, u'')
        if not len(text):
            value = NO_VALUE
        else:
            formatIdentifier = self.identifier + '.format'
            format = self.request.form.get(formatIdentifier, 'raw')
            value = Text(text=text, format=format)
        return (value, None)


class DisplayAdvancedTextFieldWidget(DisplayFieldWidget):
    """Input widget for text field.
    """
    grok.adapts(AdvancedTextSchemaField, Interface, Interface)

    def valueToUnicode(self, value):
        return value.text
