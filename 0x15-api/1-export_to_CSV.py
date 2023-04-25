#!/usr/bin/python3
"""
Using what you did in task 0, extend
your python script to export data in the
CSV format
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    import csv

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
        file_name = '{}.csv'.format(userId)

        with open(file_name, 'w', newline='') as file:
            fieldnames = ['user_id', 'user_name', 'status', 'title']
            writer = csv.DictWriter(file, fieldnames=fieldnames,
                                    quotechar='"',
                                    quoting=csv.QUOTE_ALL)
            for todo in todo_data:
                csv_data = {}
                csv_data['user_id'] = todo.get('userId')
                csv_data['user_name'] = user_name
                csv_data['status'] = todo.get('completed')
                csv_data['title'] = todo.get('title')

                writer.writerow(csv_data)
