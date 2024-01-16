#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Api_project'}

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()

        r_data = res.json()
        subscribers = r_data.get('data', {}).get('subscribers', 0)
        return subscribers

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
