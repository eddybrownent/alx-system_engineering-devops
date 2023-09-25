#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees
"""

import json
import requests
import sys


# Checks if the script is being executed as the main
if __name__ == '__main__':
    # defines base URL for API to fetch user data
    url = "https://jsonplaceholder.typicode.com/users"

    # sends  HTTP GET request to get user infor
    response = requests.get(url)

    # extracts the list of users from the JSON response
    users = response.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        # Construct the URL for fetching the user's todo list
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'

        # Send an HTTP GET request to get todo list for the user
        response = requests.get(url)

        # Extract the list of tasks from the JSON response
        tasks = response.json()

        # Create a list in the dict to store the user's tasks
        dictionary[user_id] = []

        # Iterate through tasks and add them to dict
        for task in tasks:
            dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
            # Create and open a JSON file to store employee data
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
