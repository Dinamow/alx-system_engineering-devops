#!/usr/bin/python3
"""returns information about his/her TODO list progress. """

if __name__ == "__main__":
    import requests
    import sys

    EMPID = int(sys.argv[1])
    USER = f"https://jsonplaceholder.typicode.com/users/{EMPID}"
    TODO = f"https://jsonplaceholder.typicode.com/users/{EMPID}/todos"
    tasks = [0, 0]

    ureq = requests.get(USER).json()
    treq = requests.get(TODO).json()
    name = ureq['name']
    for x in treq:
        tasks[0] += 1
        if x['completed']:
            tasks[1] += 1
    print(f'Employee {name} is done with tasks({tasks[1]}/{tasks[0]}):')
    for x in treq:
        if x['completed']:
            print(f"\t {x['title']}")
