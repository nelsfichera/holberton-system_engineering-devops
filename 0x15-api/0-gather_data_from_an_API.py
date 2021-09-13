#!/usr/bin/python3
'''fetches progress of todo list'''
if __name__ == '__main__':
    from requests import get
    from sys import argv

    identity = argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(identity)
    url_tasks = "https://jsonplaceholder.typicode.com/todos"
    name = get(url_user).json()["name"]
    todo = get(url_tasks).json()

    complete = 0
    task_total = 0
    task_list = []

    for task in todo:
        if task['userId'] == int(identity):
            task_total += 1
            if task['completed'] is True:
                complete += 1
                task_list.append(task['title'])
    print("Employee {} is done with tasks({}/{}):"
          .format(name, complete, task_total))
    for title in task_list:
            print("\t {}".format(title))
