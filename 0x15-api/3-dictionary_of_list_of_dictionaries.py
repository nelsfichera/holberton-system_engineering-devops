#!/usr/bin/python3
'''fetches todo list progress and exports to json'''
if __name__ == '__main__':
    import json
    from requests import get
    from sys import argv

    url_user = "https://jsonplaceholder.typicode.com/users"
    url_tasks = "https://jsonplaceholder.typicode.com/todos"
    users = get(url_user).json()
    todos = get(url_tasks).json()

    data = {}

    for user in users:
        task_list = []
        for task in todos:
            task_dict = {}
            if task['userId'] == user['id']:
                task_dict["task"] = task['title']
                task_dict["completed"] = task['completed']
                task_dict["username"] = user['username']
                task_list.append(task_dict)
        data[user['id']] = task_list

    with open("todo_all_employees.json", "w") as file:
        json.dump(data, file)
