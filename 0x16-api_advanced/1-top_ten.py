#!/usr/bin/python3
'''gets top 10 reddit posts'''
import requests


def top_ten(subreddit):
    '''does the thing'''
    url = 'https://www.reddit.com/r/{}/hot.json?show="all"&limit=10'.format(
        subreddit)
    headers = headers = {'User-Agent': 'Python/1.0(Holberton Project)'}
    request = requests.get(url, headers=headers, allow_redirects=False)
    try:
        for post in request.json()['data']['children']:
            print(post['data']['title'])
    except KeyError:
        print('None')
