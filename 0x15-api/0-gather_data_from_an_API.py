#!/usr/bin/python3
'''
Python script that returns information using REST API
'''
import requests
import sys


def get_user_todo_list():
    employee_id = int(sys.argv[1])
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}?_embed=todos"
    response = requests.get(url)
    data = response.json()
    user = data
    todo_list = data["todos"]

    completed_todo = []
    for todo in todo_list:
        if todo.get('completed') is True:
            completed_todo.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}): ".format(user.get('name') + ": OK", len(completed_todo), "To Do Count: OK"))
    for todo in completed_todo:
        print("\t{}".format(todo))


if __name__ == '__main__':
    get_user_todo_list()
