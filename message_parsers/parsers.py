import re
import json
from collections import defaultdict
import six
from message_parsers.utils import force_str
if six.PY2:
    from urllib2 import urlopen
else:
    from urllib.request import urlopen


__all__ = [
    'Parser',
]


class Parser(object):

    user_regex_pattern = r'@([\w]+)\W'
    emoticons_regex_pattern = r'\((\w{1,15})\)'
    uri_regex_pattern = r'https?://[/.\w]+'
    title_regex_pattern = r'<title>(.*?)</title>'

    def __init__(self, value):
        self.value = force_str(value)
        if not isinstance(self.value, six.string_types):
            raise TypeError(
                '%s must set `value` of type %s.'
                % (self.__class__.__name__, six.string_types)
            )

    @property
    def mentions(self):
        """
        Returns a list of mentions.
        """
        return re.findall(self.user_regex_pattern, self.value)

    @property
    def emoticons(self):
        """
        Returns a list of emoticons.
        """
        return re.findall(self.emoticons_regex_pattern, self.value)

    @property
    def links(self):
        """
        Returns a list of links.
        """
        match = re.findall(self.uri_regex_pattern, self.value)
        return [{'url': url, 'title': self._get_page_title_or_none(url)} for url in match]

    def to_json(self):
        """
        Returns a dict of mentions, Emoticons, and Links in the message.
        """
        d = defaultdict(list)
        if self.mentions:
            d['mentions'] = self.mentions
        if self.emoticons:
            d['emoticons'] = self.emoticons
        if self.links:
            d['links'] = self.links
        return json.dumps(d)

    def _get_page_title(self, url):
        response = urlopen(url)
        response_data = force_str(response.read())
        match = re.findall(self.title_regex_pattern, response_data)
        if match:
            return match[0]
        return None

    def _get_page_title_or_none(self, url):
        try:
            return self._get_page_title(url)
        except:
            return None
