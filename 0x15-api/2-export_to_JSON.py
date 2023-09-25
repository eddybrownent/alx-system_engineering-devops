#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


# Check if the script is being executed as the main
if __name__ == '__main__':
    # get employee ID from the command-line
    emp_id = sys.argv[1]

    # the base URL for the API
    baseUrl = "https://jsonplaceholder.typicode.com/users"

    # Constructs the URL for fetching employee information
    url = baseUrl + "/" + emp_id

    # Send an HTTP GET request to get employee infor
    response = requests.get(url)

    # get the employee's username from the JSON response
    username = response.json().get('username')

    # Constructs the URL for fetching the employee's todo list
    todoUrl = url + "/todos"

    # Sends HTTP GET request to get the todo list
    response = requests.get(todoUrl)

    # Extract the list of tasks from the JSON response
    tasks = response.json()

    # Create a dict to store the employee's todo list
    dictionary = {emp_id: []}
    for task in tasks:
        dictionary[emp_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
        # Creates and opens JSON file with employee ID as filename
    with open('{}.json'.format(emp_id), 'w') as filename:
        # Serialize the dict to JSON and write it to the file
        json.dump(dictionary, filename)
