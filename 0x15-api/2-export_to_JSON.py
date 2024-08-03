#!/usr/bin/python3
""" Export api to json"""
import json
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    res = requests.get(url_user)
    """ANYTHING"""
    user_name = res.json().get('username')
    task = url_user + '/todos'
    res = requests.get(task)
    tasks = res.json()

    user_data = {
        "user": user,
        "username": user_name,
        "tasks": []
    }

    for task in tasks:
        task_data = {
            "completed": task.get('completed'),
            "title": task.get('title')
        }
        user_data["tasks"].append(task_data)

    with open('{}.json'.format(user), 'w') as jsonfile:
        json.dump(user_data, jsonfile, indent=4)
