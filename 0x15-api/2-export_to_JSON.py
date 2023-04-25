#!/usr/bin/python3
"""
Using what you did in task 0, extend
your python script to export data in the
json format
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    import json

    userId = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(userId)
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        userId)
    todos = requests.get(url=todos_url)
    users = requests.get(user_url)
    if todos.status_code == 200 and users.status_code == 200:
        user_data = users.json()
        todo_data = todos.json()
        user_name = user_data.get('username')
        file_name = '{}.json'.format(userId)

        todo_list = []
        for todo in todo_data:
            data = {}
            data['task'] = todo.get('title')
            data['completed'] = todo.get('completed')
            data['username'] = user_name

            todo_list.append(data)

        json_data = {
            userId: todo_list
        }

        with open(file_name, 'w') as json_file:
            json.dump(json_data, json_file)
