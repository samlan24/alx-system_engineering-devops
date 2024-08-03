#!/usr/bin/python3
'''
Gather employee data from API and export to CSV
'''

import re
import requests
import sys
import csv

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            user_id = int(sys.argv[1])
            user_req = requests.get(
                '{}/users/{}'.format(REST_API, user_id)).json()
            task_req = requests.get('{}/todos'.format(REST_API)).json()
            username = user_req.get('username')
            tasks = list(
                filter(
                    lambda x: x.get('userId') == user_id,
                    task_req))

            # Prepare the data for CSV
            csv_data = []
            for task in tasks:
                csv_data.append([user_id, username, task.get(
                    'completed'), task.get('title')])

            # Define the CSV file name
            csv_filename = '{}.csv'.format(user_id)

            # Write to CSV
            with open(csv_filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(csv_data)

            print('Data has been exported to {}'.format(csv_filename))
