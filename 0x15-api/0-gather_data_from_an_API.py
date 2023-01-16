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
            resp_user = requests.get(f'{API}/users?id={sys.argv[1]}')
            resp_todo = requests.get(f'{API}/todos?userId={sys.argv[1]}')
            if resp_user.status_code != 200 or resp_todo.status_code != 200:
                exit()
            user_info = resp_user.json()
            todos_completed = [i for i in resp_todo.json() if i.get('completed')]
            todos_all = resp_todo.json()
            c = len(todos_completed)
            all = len(todos_all)
            print(f'Employee {user_info[0].get("name")} is done with tasks({c}/{all}):')
            [print(f'\t {todo.get("title")}') for todo in todos_completed]
