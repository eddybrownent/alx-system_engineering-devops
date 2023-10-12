#!/usr/bin/python3
"""
Recursively queries the Reddit API
returns a list titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    user_agent = {'User-agent': 'MyRedditBot/1.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}

    response = requests.get(url, params=parameters,
                            headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        after_data = data.get("after")
        if after_data is not None:
            hot_list = recurse(subreddit, hot_list, after=after_data)
        children = data.get("children")
        for child in children:
            hot_list.append(child.get("data").get("title"))
        return hot_list
    else:
        return None
