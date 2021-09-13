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

    with open("{}.csv".format(identity), "a") as csv:
        for task in todo:
            if task['userId'] == int(identity):
                csv.write('"{}","{}","{}","{}"\n'
                          .format(identity, name, str(task['completed']),
                                  task['title']))
