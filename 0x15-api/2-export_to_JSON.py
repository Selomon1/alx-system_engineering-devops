#!/usr/bin/python3
"""
Script that retrives and exports data in JSON format
"""
import json
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} ,employee_id".format(sys.argv[0]))
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

    user_tasks = {}

    for task in todo_list:
        user_id = user_info["id"]
        username = user_info["username"]
        t_completed = task["completed"]
        t_title = task["title"]

        if user_id not in user_tasks:
            user_tasks[user_id] = []

        user_tasks[user_id].append({
            "task": t_title,
            "completed": t_completed,
            "username": username
        })

    filename = f"{employee_id}.json"

    with open(filename, 'w') as file:
        json.dump(user_tasks, file)
