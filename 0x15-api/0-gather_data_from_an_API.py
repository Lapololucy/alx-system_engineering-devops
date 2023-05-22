#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
by using a REST API.
"""

import requests
import sys


def get_user_todo_list(employee_id):
    """
    Retrieves the TODO list progress of the employee with the given ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        str: The formatted output representing the employee's TODO list progress.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}?_embed=todos"
    response = requests.get(url)
    data = response.json()
    user = data
    todo_list = data["todos"]

    completed_todo = []
    for todo in todo_list:
        if todo.get('completed', False):
            completed_todo.append(todo.get('title'))

    output = f"Employee {user.get('name')} is done with tasks({len(completed_todo)}/{len(todo_list)}):\n"
    for todo in completed_todo:
        output += f"\t{todo}\n"

    return output


if __name__ == '__main__':
    employee_id = int(sys.argv[1]) if len(sys.argv) > 1 else None

    if employee_id is None:
        print("Please provide an employee ID as a command-line argument.")
        sys.exit(1)

    todo_list_progress = get_user_todo_list(employee_id)
    print(todo_list_progress)
