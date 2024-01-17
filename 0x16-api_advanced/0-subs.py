#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'request'}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return 0

    r_data = res.json()
    subscribe = r_data.get('data', {}).get('subscribers', 0)
    
    return subscribe
