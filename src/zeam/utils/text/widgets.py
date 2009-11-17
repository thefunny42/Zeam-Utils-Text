
from zeam.form.base.widgets import FieldWidget, WidgetExtractor
from zeam.form.ztk.fields import SchemaField, registerSchemaField
from zeam.utils.text.interfaces import IAdvancedText

from zope.interface import Interface

from grokcore import component as grok


class AdvancedTextSchemaField(SchemaField):
    """An advanced text field.
    """
    pass


registerSchemaField(AdvancedTextSchemaField, IAdvancedText)


class AdvancedTextFieldWidget(FieldWidget):
    grok.adapts(AdvancedTextSchemaField, Interface, Interface)



class AdvancedTextWidgetExtractor(WidgetExtractor):
    grok.adapts(AdvancedSchemaField, Interface, Interface)


