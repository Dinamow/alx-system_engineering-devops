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
    tasks[0] = len(treq)
    for x in treq:
        if x['completed']:
            tasks[1] += 1
            tasks.append(x['title'])
    print(f'Employee {name} is done with tasks({tasks[1]}/{tasks[0]}):')
    for x in range(2, len(tasks)):
        print(f"\t {tasks[x]}")
