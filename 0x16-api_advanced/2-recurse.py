#!/usr/bin/python3
'''creates list of hot post titles'''
import requests
import time


def recurse(subreddit, hot_list=[], after="NULL"):
    '''does the thing'''
    url = 'https://www.redit.com/r/{}/hot.json'.format(subreddit)
    headers = headers = {'User-Agent': 'Python/1.0(Holberton Project)'}
    request = requests.get(url, headers=headers, allow_redirects=False,
                           params=params)
    params = {'after': after}
    try:
        for post in request.json()['data']['children']:
            hot_list.append(post['data']['title'])
    except Exception:
        return None
    after = request.json()['data']['after']
    if after not in [None, 'None', 'NULL', 'null']:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
