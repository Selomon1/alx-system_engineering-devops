#!/usr/bin/python3
""" Contains the top_ten function """


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts """

    response = requests.get(
        f'https://www.reddit.com/r/{subreddit}/hot.json',
        headers={
            'User-Agent': 'Python/requests:APIproject:v1.0.0 (by /u/Selomon1)'
        },
        params={'limit': 10}
    ).json()

    posts = response.get("data", {}).get("children", [])

    if not subreddit or not isinstance(subreddit, str) or not posts or \
       (len(posts) > 0 and posts[0].get('kind') != 't3'):
        print(None)
    else:
        for post in posts:
            title = post.get("data", {}).get("title", None)
            print(title)
