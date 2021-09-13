#!/usr/bin/python3
'''fetches todo list progress and exports to json'''
if __name __ = '__main__':
    from json import dump
    from requests import get

    path = 'https://jsonplaceholder.typicode.com/users'
    name = get(path).json()

    todo = get('https://jsonplaceholder.typicode.com/todos').json()

    task_dict = {}
    name_list = []

    for user in users:
        task_dict[user['id']] = []
        name_list.append(user['username'])

    for task in todo:
        temp_dict = {}
        temp_dict['username'] = namelist[task['userId'] - 1]
        temp_dict['task'] = task['title']
        temp_dict['completed'] = task['completed']
        task_dict['userId'].append(temp_dict)

    with open('todo_all_employees.json', 'w') as file:
        dump(task_dict, file)
