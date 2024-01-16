#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given
"""


import requests


def number_of_subscribers(subreddit):
    """
    Returns number of subscribers for a given subreddit.
    Args:
        subreddit (str): the subreddit to query
    Returns:
        int: number of subscribers, else 0 if invalid
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/58.0.3029.110 Safari/537.3'}

    res = requests.get(url, headers=headers, allow_redirects=False)
    res.raise_for_status()

    try:
        if res.status_code >= 300:
            return (0)
        else:
            data = res.json().get('data', {})
            subscribers = data.get('subscribers', 0)
            return (subscribers)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return (0)
