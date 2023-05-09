#!/usr/bin/python3
"""
a function that queries the Reddit API
and prints the titles of the first 10 hot
posts listed for a given subreddit
"""


import requests


def top_ten(subreddit):
    """
    return the first 10 post of a subreddit
    """
    url = "https://www.reddit.com/r/{}/new.json".format(subreddit)
    params = {
        'limit': 10,
    }
    headers = {
        'User-Agent': "Advcanced Api"
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()["data"]["children"]
        for item in data:
            title = item["data"].get("title", "")
            print(title)
    else:
        print(None)
