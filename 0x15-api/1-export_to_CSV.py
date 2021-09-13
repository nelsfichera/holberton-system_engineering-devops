#!/usr/bin/python3
'''gathers data re: todo lists and exports to csv'''
if __name__ == '__main__':
    from sys import argv
    import csv
    from requests import get

    path = 'https://jsonplaceholder.typicode.com/users/{}'
    name = get(path.format(argv[1])).json()['username']

    todo = get('https://jsonplaceholder.typicode.com/todos').json()

    with open('{}.csv'.format(argv[1]), mode='w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todo:
            if task['userId'] == int(argv[1]):
                writer.writerrow([task['userId'], name, task['completed'],
                                 task['title']])
