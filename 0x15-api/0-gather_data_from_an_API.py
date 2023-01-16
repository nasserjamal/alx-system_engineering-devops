#!/usr/bin/python3
"""Gather data from an API """

if (__name__ == "__main__"):
    import requests
    import sys
    url = "https://jsonplaceholder.typicode.com/"
    resp_user = requests.get(f"{url}users?id={sys.argv[1]}")
    resp_todo = requests.get(f"{url}todos?userId={sys.argv[1]}")
    if resp_user.status_code != 200 or resp_todo.status_code != 200:
        exit()
    user_info = resp_user.json()
    todos_completed = [i for i in resp_todo.json() if i['completed']]
    todos_all = resp_todo.json()
    c = len(todos_completed)
    all = len(todos_all)
    print(f"Employee {user_info[0]['name']} is done with tasks({c}/{all}):")
    [print("\t"+todo['title']) for todo in todos_completed]
