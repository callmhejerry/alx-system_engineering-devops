# !/usr/bin/python3

"""
Write a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit.If an invalid subreddit is given,
the function should return 0.
"""


import requests


def number_of_subscribers(subreddit):
    """
    returns the number of reddit subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-agent': "Advacned Api"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"].get("subscribers", 0)
        return subscribers
    return 0
