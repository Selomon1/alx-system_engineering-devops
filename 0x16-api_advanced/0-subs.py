#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Ubuntu:0x16.api_advanced:v1.0.0 (by /u/Selomon)"}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 404:
        return 0

    r_data = res.json().get('data')
    num_subscribe = r_data.get('subscribers')

    return num_subscribe
