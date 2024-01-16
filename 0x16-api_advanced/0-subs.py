#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """


import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/58.0.3029.110 Safari/537.3'}

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code >= 300:
        return (0)
    else:
        data = res.json().
        data_dic = data.get('data')
        subscribers = data_dic.get('subscribers')
        return (subscribers)
