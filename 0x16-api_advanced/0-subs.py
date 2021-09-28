#!/usr/bin/python3
'''gets subscribers of subreddit '''
import requests


def number_of_subscribers(subreddit):
    '''does the thing'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/1.0(Holberton Project)'}
    request = requests.get(url, headers=headers, allow_redirects=False)
    try:
        return request.json()['data']['subscribers']
    except Exception:
        return 0
