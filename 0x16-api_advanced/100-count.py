#!/usr/bin/python3
""" 100 count """
import requests


def count_words(subreddit, word_list, after=None, count=0, wd_count=None):
    """ Queries the reddit API, parses title and prints """
    if subreddit is None or not isinstance(subreddit, str) or len(word_list) == 0:
        return

    if wd_count is None:
        wd_count = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/Selomon1)'
    }
    params = {'limit': 100, 'after': after}

    try:
        r = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    data = r.json().get('data', {})
    children = data.get('children', [])

    for child in children:
        title = child.get('data', {}).get('title', '').lower()
        for keyword in word_list:
            keyword = keyword.lower()
            if keyword in title:
                wd_count[keyword] = wd_count.get(keyword, 0) + 1

    after = data.get('after')
    if after is not None:
        return count_words(subreddit, word_list, after, wd_count)
    else:
        sort_count = sorted(wd_count.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sort_count:
            print(f"{keyword}: {count}")
