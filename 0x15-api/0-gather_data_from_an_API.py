#!/usr/bin/python3
"""
a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    userId = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(userId)
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        userId)
    todos = requests.get(url=todos_url)
    users = requests.get(user_url)
    if todos.status_code == 200 and users.status_code == 200:
        todo_data = todos.json()
        user_data = users.json()
        user_name = user_data.get('name')
        completed_todo = 0
        number_of_todo = len(todo_data)

        for todo in todo_data:
            if todo.get('completed'):
                completed_todo = completed_todo + 1

        print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                              completed_todo,
                                                              number_of_todo))

        for todo in todo_data:
            title = todo.get('title')
            print('\t {}'.format(title))
