#!/usr/bin/python3
'''fetches todo list progress and exports to json'''
if __name__ == '__main__':
    from sys import argv
    import json
    from requests import get

    identity = argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(identity)
    url_tasks = "https://jsonplaceholder.typicode.com/todos"
    name = get(url_user).json()["username"]
    todo = get(url_tasks).json()

    task_list = []
    for task in todo:
        task_dict = {}
        if task['userId'] == int(identity):
            task_dict["task"] = task['title']
            task_dict["completed"] = task['completed']
            task_dict["username"] = name
            task_list.append(task_dict)

    data = {}
    data[identity] = task_list

    with open("{}.json".format(identity), "w") as file:
        json.dump(data, file)
