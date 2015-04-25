Installation
------------

You can to use [pip](https://pypi.python.org/pypi/pip) to install last source:
``` bash
$ pip install git+git://github.com/joeljames/chat-message-parser.git
```

Usage
-----

``` python
from message_parsers.parsers import Parser

>>> Parser("@chris you around?").to_json() #Parse mentions
'{"mentions": ["chris"]}'

>>> Parser("@chris you around?").to_json() #Parse mentions
'{"emoticons": ["megusta", "coffee"]}'

>>> Parser("Olympics are starting soon; http://www.nbcolympics.com").to_json() #Parse link and get the page title
'{"links": [{"title": "Welcome to Python.org", "url": "http://python.org"}]}'

```

Test
-----
1. Install Dependency

    ``` bash
    $ pip install -r requirements.txt
    ```

2. Run Test:

    ``` bash
    $ make test
    ```
