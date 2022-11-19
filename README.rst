Bluebird Tree
=============

Installation
------------

This software is very much in pre-alpha, but it should work if you adhere
to the following workflow:

1. Download python, if not already installed on your system
   * If you're not sure, open a terminal and run ``python --version``
   * If you don't see something like "Python 3.x.x" check
   `here <https://www.python.org/downloads/>`_
2. Download `poetry <https://python-poetry.org/docs/>`_
3. Git clone this repository and open a terminal there


How To Run The Scripts
----------------------
1. Run ``poetry install`` to install dependencies
2. Get an api key from twitter, copy the bearer token, and run:
   ``export 'BEARER_TOKEN'='<your_bearer_token>'``
3. Run the scripts in the bluebird_tree folder from the project root like so:
   ``poetry run python bluebird_tree/<name-of-script>.py > some_name.json``

(Note: Ofc this only gives you the json, but that's the most important thing at
this point. We can always clean the data later, considering both scripts tag 
each relevant datum (pinned tweet text, bio text) with the same user ids)
