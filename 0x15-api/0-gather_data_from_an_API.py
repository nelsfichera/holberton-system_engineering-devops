#!/usr/bin/python3
'''fetches progress of todo list'''
if __name__ == '__main__':
    from requests import get
    from sys import argv

    path = 'https://jsonplaceholder.typicode.com/users/{}'
    name = get(path.format(argv[1])).json()['name']

    to_do = get('https://jsonplaceholder.typicode.com/todos').json()
    complete = 0
    total = 0
    to_do_list = ''

    for task in to_do:
        if task['userId'] == int(av[1]):
            total = total + 1
            if task['completed'] is True:
                complete = complete + 1
                to_do_list += "\t " + task['title'] + "\n"

    print('Employee {} is done with tasks({}/{}):\n{}'.format(name, complete,
                                                              total,
                                                              to_do_list_),
          end='')
