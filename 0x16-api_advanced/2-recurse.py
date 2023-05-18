#!/usr/bin/python3

"""
a recursive function that queries the Reddit API
and returns a list containing the titles of all hot
articles for a given subreddit. If no results are found for
the given subreddit, the function should return None.
"""


import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    return list containing titles of all articles
    """
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    after = after
    count = count

    if count == 0:
        params = {
            "limit": 50
        }
    else:
        params = {
            "after": after,
            "count": count,
            "limit": 50,
        }
    headers = {
        "User-Agent": "advanced api"
    }
    titles = hot_list
    if after is None:
        return titles
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()["data"]
        children = data.get("children", [])
        count = count + len(children)
        after = data.get("after")
        for child in children:
            title = child["data"].get("title", "")
            titles.append(title)
        return recurse(subreddit, titles, after=after, count=count)
    else:
        return None
