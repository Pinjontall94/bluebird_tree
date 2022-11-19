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
2. Get an api key from `twitter
   <https://developer.twitter.com/en/portal/petition/essential/basic-info>`_,
   copy the bearer token, and run:
   ``export 'BEARER_TOKEN'='<your_bearer_token>'``
3. Configure the scripts as needed (explained below)
4. Run the scripts in the bluebird_tree folder from the project root like so:
   ``poetry run python bluebird_tree/<name-of-script>.py > some_name.json``

(Note: Ofc this only gives you the json, but that's the most important thing at
this point. We can always clean the data later, considering both scripts tag 
each relevant datum (pinned tweet text, bio text) with the same user ids)


Configuration (i.e. "Twitter might die before I can write a nice UI for this")
------------------------------------------------------------------------------

So considering time is of the essence, the followers_lookup.py file is
configured by:
* Editing the ``followers_or_following`` variable to either "followers" or
"following"

Likewise the pinned_tweets_lookup.py script reads
"bluebird_tree/pinned_tweet_ids.txt" (a file containing only one id per line;
an example file is already there if you just cloned this repository).

How do I find the tweet ids? I'm working on it, but in the meantime you can
help me find a way to get the ids out of the json from followers_lookup.py
(it actually already grabs the ids of your follows/followers pinned tweets by
default! I just need to monkey with the json to get it to work.)
