#!/usr/bin/python3
"""
Gathers data from an API about employee's todo list and export to CSV.
"""
import requests
import sys
import csv

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

    with open(filename, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            csv_writer.writerow([
                str(employee_id),
                user_info.get("username"),
                str(task.get("completed")),
                task.get("title")
            ])
