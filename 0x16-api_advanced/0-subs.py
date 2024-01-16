#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Api_project'}

    res = requests.get(url, headers=headers)

    if subreddit is None or not isinstance(subreddit, str):
        return 0
    else:
        data = res.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
