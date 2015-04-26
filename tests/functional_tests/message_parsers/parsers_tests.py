import json
from nose.tools import *

from message_parsers.parsers import Parser


class TestParser(object):

    def test_with_mention(self):
        message = '@chris you around?'
        expected_output = json.dumps(
            {'mentions': ['chris']}
        )
        output = Parser(message).to_json()
        assert_equal(output, expected_output)

    def test_with_emoticon(self):
        message = 'Good morning! (megusta) (coffee)'
        expected_output = json.dumps(
            {'emoticons': ['megusta', 'coffee']}
        )
        output = Parser(message).to_json()
        assert_equal(output, expected_output)

    def test_with_link(self):
        message = 'Olympics are starting soon; http://www.nbcolympics.com'
        expected_output = json.dumps(
            {
                'links': [
                    {
                        'url': 'http://www.nbcolympics.com',
                        'title': 'NBC Olympics | Home of the 2016 Olympic Games in Rio'
                    }
                ]
            }
        )
        output = Parser(message).to_json()
        assert_equal(output, expected_output)

    def test_with_mention_emoticon_and_link(self):
        message = '@bob @john (success) such a cool feature; https://twitter.com/jdorfman/status/430511497475670016'
        expected_output = json.dumps(
            {
                'mentions': ['bob', 'john'],
                'emoticons': ['success'],
                'links': [
                    {
                        'url': 'https://twitter.com/jdorfman/status/430511497475670016',
                        'title': 'Justin Dorfman on Twitter: &quot;nice @littlebigdetail from @HipChat (shows hex colors when pasted in chat). http://t.co/7cI6Gjy5pq&quot;'
                    }
                ]
            }
        )
        output = Parser(message).to_json()
        assert_equal(output, expected_output)
