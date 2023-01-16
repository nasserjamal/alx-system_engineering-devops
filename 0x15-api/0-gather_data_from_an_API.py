#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
Implemented using recursion
"""
import re
import requests
import sys


API = "https://jsonplaceholder.typicode.com"
"""REST API url"""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            resp_user = requests.get('{}/users/{}'.format(API, id)).json()
            resp_todo = requests.get('{}/todos'.format(API)).json()
            user_info = resp_user
            todos_completed = [i for i in resp_todo if i.get('completed')]
            todos_all = resp_todo
            todos = list(filter(lambda x: x.get('userId') == id, resp_todo))
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            c = len(todos_completed)
            all = len(todos_all)
            print(f"Employee {user_info[0].get('name')} is done with tasks({c}/{all}):")
            [print(f"\t {todo.get('title')}") for todo in todos_completed]
