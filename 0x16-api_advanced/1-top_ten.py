#!/usr/bin/python3
""" Contains the top_ten function """


import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {
            'User-Agent': 'Python/requests:APIproject:v1.0.0 (by /u/Selomon1)'}
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print(None)
        return

    data = res.json()
    posts = data.get("data", {}).get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "")
        print(title)
