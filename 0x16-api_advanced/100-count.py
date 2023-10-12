#!/usr/bin/python3
"""
Reddit API Word Count

This script counts occurrences of specific words in titles of hot
posts from a given subreddit using Reddit API

Usage:
    Specify the subreddit and a list of words to count.
    The script fetches the hot posts from subreddit and count word
    occurrences
    The results will be displayed in the format "word: count".
"""
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """count word occurrences in subreddit hot post titles"""

    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url, params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'MyRedditBot/1.0'})

    if request.status_code == 200:
        data = request.json()

        for heading in (data['data']['children']):
            for word in heading['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count[j] > count[i] or
                            (word_list[i] > word_list[j] and
                             count[j] == count[i])):
                        aux = count[i]
                        count[i] = count[j]
                        count[j] = aux
                        aux = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = aux

            for i in range(len(word_list)):
                if (count[i] > 0) and i not in save:
                    print("{}: {}".format(word_list[i].lower(), count[i]))
        else:
            count_words(subreddit, word_list, after, count)
