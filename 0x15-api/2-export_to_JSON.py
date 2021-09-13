#!/usr/bin/python3
'''fetches todo list progress and exports to json'''
if __name __ = '__main__':
    from sys import argv
    from json import dump
    from requests import get

    path = 'https://jsonplaceholder.typicode.com/users/{}'
    name = get(path.format(argv[1])).json()['username']

    todo = get('https://jsonplaceholder.typicode.com/todos').json()

    task_dict = {}
    task_dict[argv[1]] = []

    for task in todo:
        if task['userId'] == int(argv[1]):
            temp_dict = {}
            temp_dict['task'] = task['title']
            temp_dict['completed'] = task['completed']
            temp_dict['username'] = name
            task_dict[argv[1]].append(temp_dict)

    with open('{}.json'.format(argv[1]), 'w') as file:
        dump(task_dict, file)
