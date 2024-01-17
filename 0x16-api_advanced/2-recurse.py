#!/usr/bin/python3
""" Recursive module """
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """ Recursive function """
    url = f'https://www.reddit.com/r/{subreddit}/hpt.json'
    headers = {
        'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/Selomon1)'
    }

    while True:
        params = {'limit': 100, 'after': after}
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if r.status_code == 404:
            return None

        data = r.json().get('data', {})
        children = data.get('children', [])

        for child in children:
            title = child.get('data', {}).get('title', '')
            hot_list.append(title)

        after = data.get('after')
        count += data.get('dist', 0)

        if after is None:
            return recurse(subreddit, hot_list, after, count)
        else:
            return hot_list
