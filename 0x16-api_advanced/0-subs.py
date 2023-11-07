#!/usr/bin/python3


def number_of_subscribers(subreddit):
    """
    this function returns the number of subscribers
    """
    import requests

    data = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                        headers={'User-Agent': 'Mozilla/5.0'},
                        allow_redirects=False)

    if data.status_code != 200:
        return 0

    return int(data.json()['data']['subscribers'])
