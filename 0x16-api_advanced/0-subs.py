#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
from requests import get


def number_of_subscribers(subreddit):
    """
    This finction queries the Reddit API and returns the number of subscribers
    (total subscribers) for a given subreddit
    Args:
        subreddit: The name of the subreddit to query
    Returns:
        number of subscribers for given subreddit, or 0 if an error occurs
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'MyRedditBot/1.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = get(url, headers=user_agent)
        results = response.json()
        try:
            return results.get('data').get('subscribers')
        except Exception:
            return 0

    except Exception:
        return 0
