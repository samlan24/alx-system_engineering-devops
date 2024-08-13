#!/usr/bin/python3

"""
This script demonstrates how to retrieve data
from an API using the requests library.
"""

import requests


def number_of_subscribers(subreddit):
    """returns number of subsbribers"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()
    if response.status_code == 200:
        return data['data']['subscribers']
    else:
        return 0
