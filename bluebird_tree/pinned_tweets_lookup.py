import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")


pinned_tweet_id_list = ["1278747501642657792", "1255542774432063488"]


def batch_request(lst):
    """Loop over a list of tweet_ids to generate params dict."""
    # iterate over tuples of 100 tweet ids
    for tweet_ids_100batch in zip(*(iter(lst),) * 100):

        # splice a nice comma-separated string of your tweet ids
        ids = "ids=" + ",".join(tweet_ids_100batch)
        tweet_fields = "tweet.fields=text,id"

        url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
        response = requests.request("GET", url, auth=bearer_oauth)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code,
                    response.text
                )
            )
    return response.json()

def single_request(lst):
    "Iterate over a single list of <100 pinned tweets."
    # splice a nice comma-separated string of your tweet ids
    ids = "ids=" + ",".join(lst)
    tweet_fields = "tweet.fields=text,id"

    url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code,
                response.text
            )
        )
    return response.json()


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def main():
    if len(pinned_tweet_id_list) > 100:
        json_response = batch_request(pinned_tweet_id_list)
    else:
        print("Len of pinned_tweet_id_list = {}".format(
            len(pinned_tweet_id_list))
        )
        json_response = single_request(pinned_tweet_id_list)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
