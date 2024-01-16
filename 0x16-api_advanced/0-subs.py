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

    try:
        with requests.get(url, headers=headers, allow_redirects=False) as res:
            res.raise_for_status()

            data = res.json().get('data', {})
            subscribers = data.get('subscribers', 0)
            return subscribers

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print("{:d}".format(subscribers))
