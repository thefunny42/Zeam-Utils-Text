
from zeam.form.base import NO_VALUE
from zeam.form.base.widgets import FieldWidget, WidgetExtractor
from zeam.form.ztk.fields import SchemaField, registerSchemaField
from zeam.utils.text.interfaces import IAdvancedText
from zeam.utils.text.format import availableFormat

from zope.interface import Interface

from grokcore import component as grok


class AdvancedTextSchemaField(SchemaField):
    """An advanced text field.
    """

    def availableFormat(self):
        return availableFormat()


registerSchemaField(AdvancedTextSchemaField, IAdvancedText)


class AdvancedTextFieldWidget(FieldWidget):
    grok.adapts(AdvancedTextSchemaField, Interface, Interface)

    def prepareValue(self, value):
        formatted_value = u''
        formatted_format = 'raw'
        if value is not NO_VALUE:
            formatted_value = unicode(value.raw)
            formatted_format = value.format
        return {self.identifier: formatted_value,
                self.identifier + '.format': formatted_format}


class AdvancedTextWidgetExtractor(WidgetExtractor):
    grok.adapts(AdvancedTextSchemaField, Interface, Interface)


