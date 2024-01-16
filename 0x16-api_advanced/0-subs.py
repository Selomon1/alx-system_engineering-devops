#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers """
    if subreddit is None or not isinstance(reddit, str):
        return 0

    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Api_project/requests:v1.0.0 (by /u/Selomon1)'}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        r_data = res.json()
        if r_data.get("error") == "invalid_category":
            return 0
    subscribe = r_data.get('subscribers', 0)
    return subscribe
