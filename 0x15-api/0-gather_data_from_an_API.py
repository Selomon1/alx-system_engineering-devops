#!/usr/bin/python3
"""
Gathers data from an API about an employee's TODO list progress
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    user_info_url = (
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(employee_id)
    )
    user_info = requests.get(user_info_url).json()

    todo_url = (
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(employee_id)
    )
    todo_list = requests.get(todo_url).json()

    completed_tasks = [task for task in todo_list if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user_info.get("name"), len(completed_tasks), len(todo_list)
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
