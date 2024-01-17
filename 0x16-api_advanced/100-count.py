#!/usr/bin/python3
""" 100 count """
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """ Queries the reddit API, parses title and prints """
    if after is None:
        after = ""
    if not (subreddit and isinstance(subreddit, str) and word_list):
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/Selomon1'
    }
    params = {'limit': 100, 'after': after}

    try:
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()
        data = r.json().get('data', {})
        children = data.get('children', [])

        for child in children:
            title = child.get('data', {}).get('title', '').lower()
            for word in word_list:
                keyword = word.lower()
                if keyword in title:
                    counts[keyword] = counts.get(keyword, 0) + 1

        after = data.get('after')
        if after is not None:
            return count_words(subreddit, word_list, after, counts)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for keyword, count in sorted_counts:
        print(f"{keyword}: {count}")
