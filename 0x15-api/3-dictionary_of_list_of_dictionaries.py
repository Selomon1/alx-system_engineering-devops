#!/usr/bin/python3
"""
Script that retrieves and export data in the Json format
"""
import json
import requests

if __name__ == '__main__':
    b_url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{b_url}/users").json()
    todos = requests.get(f"{b_url}/todos").json()

    todo_all_employees = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_todos = [
            {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            for todo in todos if todo.get("userId") == user_id
        ]
        todo_all_employees[str(user_id)] = user_todos

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(todo_all_employees, json_file)
