#!/usr/bin/python3
'''fetches progress of todo list'''
if __name__ == '__main__':
    from requests import get
    from sys import argv
    import csv

    identity = argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(identity)
    url_tasks = "https://jsonplaceholder.typicode.com/todos"
    name = get(url_user).json()["username"]
    todo = get(url_tasks).json()

    with open("{}.csv".format(identity), mode="w") as file:
        for task in todo:
            if task['userId'] == int(identity):
                r = csv.writer(file, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_ALL)
                r.writerow([str(identity), name, task['completed'], task['title']])
