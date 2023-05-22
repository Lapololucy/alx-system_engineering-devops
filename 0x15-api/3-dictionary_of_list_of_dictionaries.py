#!/usr/bin/python3
"""
Python script to retrieve employee TODO list progress for all employees and export data in JSON format.
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


def export_todo_list_json():
    """
    Exports the TODO list for all employees to a JSON file.
    """
    employees = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todo_all_employees = {}

    for employee in employees:
        employee_id = employee.get('id')
        employee_name = employee.get('name')
        todo_list = get_employee_todo_list(employee_id)

        employee_tasks = [
            {
                "username": employee_name,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            for task in todo_list
        ]

        todo_all_employees[employee_id] = employee_tasks

    filename = 'todo_all_employees.json'

    with open(filename, 'w') as jsonfile:
        json.dump(todo_all_employees, jsonfile, indent=4)

    print("Data exported to: {}".format(filename))


if __name__ == "__main__":
    export_todo_list_json()
