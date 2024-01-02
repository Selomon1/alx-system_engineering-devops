#!/usr/bin/python3
"""
Gathers data from an API about employee's todo list and export to CSV.
"""
import csv
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

    filename = "{}.csv".format(employee_id)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todo_list:
            user_id = user_info["id"]
            username = user_info["username"]
            completed = task["completed"]
            title = task["title"]

            writer.writerow([user_id, username, str(completed), title])
