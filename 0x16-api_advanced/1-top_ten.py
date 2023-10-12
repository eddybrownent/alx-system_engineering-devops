#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    Args:
    subreddit: The name of the subreddit to query.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'MyRedditBot/1.0'}
    params = {'limit': 10}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    try:
        response = get(url, headers=user_agent, params=params)
        results = response.json()

        my_data = results.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception as e:
        print("None")
