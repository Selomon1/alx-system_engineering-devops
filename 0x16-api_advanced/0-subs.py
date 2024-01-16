#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyCustomUserAgent'}

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code >= 300:
        return 0
    else:
        data = res.json()
        data_dic = data.get('data')
        subscribers = data_dic.get('subscribers')
        return subscribers
