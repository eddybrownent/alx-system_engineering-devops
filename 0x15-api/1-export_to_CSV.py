#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees
"""

import requests
import sys

# Check if the script is being executed as the main
if __name__ == '__main__':
    # Get the employee ID from the CL
    em_id = sys.argv[1]

    # Define the base URL for the API
    baseUrl = "https://jsonplaceholder.typicode.com/users"

    # Construct the URL for fetching employee information
    url = baseUrl + "/" + em_id

    # Sending HTTP GET request to get employee information
    response = requests.get(url)

    # Extracts the employee's username from the JSON response
    username = response.json().get('username')

    # Construct the URL for fetching the employee's todo list
    todoUrl = url + "/todos"

    # Sending HTTP GET request to get the todo list
    response = requests.get(todoUrl)

    # Extract the list of tasks from the JSON response
    tasks = response.json()

    # Create and open a CSV file with the employee ID as the filename
    with open('{}.csv'.format(em_id), 'w') as file:
        # Iterate through the tasks and write them to the CSV file
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(em_id, username, task.get('completed'),
                               task.get('title')))
