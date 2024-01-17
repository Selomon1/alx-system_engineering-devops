#!/usr/bin/python3
""" 100 count """
import requests


def count_words(subreddit, word_list, after='', word_data={}):
    """ Queries the reddit API, parses title and prints """
    if subreddit is None or not isinstance(subreddit, str) or len(word_list) == 0:
        return

    if not word_data:
        for word in word_list:
            if word.lower() not in word_data:
                word_data[word.lower()] = 0

    if after is None:
        sort_count = sorted(word_data.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sort_count:
            if count:
                print(f"{keyword}: {count}")
        return None

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
        hot = r.json().get('data', {}).get('children', [])
        aft = r.json().get('data', {}).get('after')

        for post in hot:
            title = post.get('data', {}).get('title', '').lower()
            lower = [word.lower() for word in title.split(' ')]

            for word in word_data.keys():
                word_data[word] += lower.count(word)
                
    except Exception as e:
        return None

    count_words(subreddit, word_list, aft, word_data)
