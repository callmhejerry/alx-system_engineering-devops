#!/usr/bin/python3
"""
Using what you did in task 0, extend
your python script to export data in the
json format
"""

if __name__ == '__main__':
    import requests
    import json

    user_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    todos = requests.get(url=todos_url)
    users = requests.get(user_url)
    if todos.status_code == 200 and users.status_code == 200:
        user_data = users.json()
        todo_data = todos.json()
        file_name = 'todo_all_employees.json'

        json_data = {}

        for user in user_data:
            id = user.get('id')
            json_data[id] = []

        for todo in todo_data:
            user_id = todo.get('userId')
            user = list(filter(lambda u: u.get('id') == user_id,
                               user_data))
            user_name = user[0].get('username')

            todo_data = {
                'username': user_name,
                'task': todo.get('title'),
                'completed': todo.get('completed')
            }
            json_data[user_id].append(todo_data)

        with open(file_name, 'w') as json_file:
            json.dump(json_data, json_file)
