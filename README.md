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

Set Up Development Environment
------------------------------
1. Setup Virtualenv

Install development requirements. It is highly recommended that you use a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/), and activate the virtualenv before installing the requirements.

1. Clone Project

    ``` bash
    $ git clone https://github.com/joeljames/chat-message-parser.git
    ```

2. Install Dependency

    ``` bash
    $ pip install -r requirements.txt
    ```

Test & Coverage
---------------
1. Install Dependency

    ``` bash
    $ pip install -r requirements.txt
    ```

2. Run Unit Test:

    ``` bash
    $ make unit_test
    ```

3. Run Functional Test:

    ``` bash
    $ make functional_test
    ```

4. Run Unit and Functional Test Using Tox (Test the package in python 2.7 and 3.4):

    ``` bash
    $ tox
    ```
