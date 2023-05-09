#!/usr/bin/python3

"""
A recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a
sorted count of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""


import requests


def count_words(subreddit, word_list, count=0, after="", result={}):
    """
    prints a sorted count of given keywords
    """
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    after = after
    count = count
    result = result

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
    if after is None:
        sorted_list = sorted(result.items(),
                             key=lambda item: (-item[1], item[0]))
        for key, value in sorted_list:
            print("{}: {:d}".format(key, value))
    else:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            print("success")
            data = response.json().get("data")
            after = data.get("after")
            articles = data.get("children")
            count = count + len(articles)

            for article in articles:
                title = article["data"]["title"].lower()
                for keyword in word_list:
                    if keyword.lower() in result.keys():
                        result[keyword.lower()] += title.count(keyword.lower())
                    else:
                        if title.count(keyword) > 0:
                            result[keyword] = title.count(keyword.lower())
            count_words(subreddit, word_list, count=count,
                        after=after, result=result)
        else:
            print("")
