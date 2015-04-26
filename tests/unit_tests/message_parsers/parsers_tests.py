import json
from nose.tools import *
from mock import *

from message_parsers.parsers import Parser


class TestParser(object):

    @patch.multiple('message_parsers.parsers',
                    re=DEFAULT)
    def test_mentions(self, re):
        message = '@chris you around?'
        Parser(message).mentions
        re.findall(Parser.user_regex_pattern, message)

    @patch.multiple('message_parsers.parsers',
                    re=DEFAULT)
    def test_emoticons(self, re):
        message = '(coffee)'
        Parser(message).emoticons
        re.findall(Parser.emoticons_regex_pattern, message)

    @patch.multiple('message_parsers.parsers',
                    re=DEFAULT)
    def test_links(self, re):
        message = 'https://www.python.org'
        Parser(message).links
        re.findall(Parser.uri_regex_pattern, message)

    @patch.multiple('message_parsers.parsers',
                    urlopen=DEFAULT,
                    re=DEFAULT)
    def test_get_page_title(self, urlopen, re):
        message = '@chris you around?'
        Parser(message)._get_page_title('https://www.python.org')
        urlopen.assert_called_with('https://www.python.org')
        re.findall(Parser.title_regex_pattern, urlopen())

    @patch.multiple('message_parsers.parsers.Parser',
                    _get_page_title=DEFAULT)
    def test_get_page_title_or_none(self, _get_page_title):
        message = '@chris you around?'
        Parser(message)._get_page_title_or_none('https://www.python.org')
        _get_page_title.assert_called_with('https://www.python.org')
