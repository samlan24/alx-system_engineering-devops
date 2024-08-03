#!/usr/bin/env python3

"""
REST API for an employee
that returns ID and todo lists
"""


import requests
import sys


def get_employee_todo_progress(employee_id):
    # Fetch employee data
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found")
        return

    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch employee TODO list
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(done_tasks)

    # Display results
    print(
        f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
