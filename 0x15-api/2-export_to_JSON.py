#!/usr/bin/python3
"""
Python script to retrieve employee TODO list progress and export data in JSON format.
"""

import sys
import requests
import json


def get_employee_todo_list(employee_id):
    """
    Retrieves the TODO list for the given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict: The TODO list in JSON format.
    """
    url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': employee_id}
    response = requests.get(url, params=params)
    todo_list = response.json()
    return todo_list


def export_todo_list_json(employee_id):
    """
    Exports the employee TODO list to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
    """
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)).json()
    employee_name = employee.get('name')
    todo_list = get_employee_todo_list(employee_id)

    data = {
        "USER_ID": [
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": employee_name
            }
            for task in todo_list
        ]
    }

    filename = '{}.json'.format(employee_id)

    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

    print("Data exported to: {}".format(filename))


def display_todo_list_progress(employee_id):
    """
    Displays the employee TODO list progress.

    Args:
        employee_id (int): The ID of the employee.
    """
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)).json()
    employee_name = employee.get('name')
    todo_list = get_employee_todo_list(employee_id)

    completed_tasks = []
    for task in todo_list:
        if task.get('completed'):
            completed_tasks.append(task)

    total_tasks = len(todo_list)
    total_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, total_completed_tasks, total_tasks))

    for task in completed_tasks:
        print("\t{}".format(task.get('title')))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    display_todo_list_progress(employee_id)
    export_todo_list_json(employee_id)
