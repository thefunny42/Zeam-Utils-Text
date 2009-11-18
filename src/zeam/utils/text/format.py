
from docutils.core import publish_parts
from grokcore import component as grok
from zope import component
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zeam.utils.text.interfaces import ITextFormat


def availableFormat():
    """Return a vocabulary of the available formats.
    """
    results = []
    for name, format in component.getUtilitiesFor(ITextFormat):
        results.append(SimpleTerm(value=name, title=format.title))
    return SimpleVocabulary(results)


class TextFormat(grok.GlobalUtility):
    """Base class to define text format.
    """
    grok.baseclass()
    grok.implements(ITextFormat)
    grok.provides(ITextFormat)

    title = u'Default'

    def render(self, data):
        raise NotImplementedError


class RawFormat(TextFormat):
    """Raw format, just use the data as text.
    """
    grok.name('raw')

    title = u'Raw'

    def render(self, data):
        return u'<pre>' + data + u'</pre>'


class RestFormat(TextFormat):
    """Re-structured text format.
    """
    grok.name('rest')

    title = u'Re-structured text'

    def render(self, data):
        return publish_parts(
            data, parser_name='restructuredtext', writer_name='html')['body']
