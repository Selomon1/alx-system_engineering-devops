#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Api_project/requests:v1.0.0 (by /u/Selomon1)'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return "Subscribers for {}: {}".format(subreddit, 0)

    try:
        r_data = res.json()
        subscribe = r_data.get('data', {}).get('subscribers', 0)
        return "Subscribers for {}: {}".format(subreddit, subscribe)
    except ValueError:
        return "Subscribers for {}: {}".format(subreddit, 0)
