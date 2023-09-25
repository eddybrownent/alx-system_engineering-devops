#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import request
import sys

if __name__ == '__main__':
    em_id = sys.argv[1]

    """ Defining the base URL for the API """
    baseUrl = "https://jsonplaceholder.typicode.com/users"

    """ Constructing the URL to fetch employee info """
    url = baseUrl + "/" + em_id

    """Send an HTTP GET request to get employee info """
    response = requests.get(url)

    """ Extract the employee name from the JSON response """
    em_name = response.json().get('name')

    """ the URL for fetching the employee's todo list """
    todoUrl = url + "/todos"

    """ Send an HTTP GET request to get the todo list """
    response = requests.get(todoUrl)

    """ Extract the list of tasks from the JSON response """
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(em_name, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
