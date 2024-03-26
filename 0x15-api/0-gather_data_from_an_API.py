#!/usr/bin/python3
"""Fetches task completion information for a specified user ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    uid = sys.argv[1]
    usr = requests.get(f"{url}users/{uid}").json()
    tsk = requests.get(f"{url}todos", params={"userId": uid}).json()

    done = [task.get("title") for task in tsk if task.get("completed") is True]
    print("User {} has completed tasks({}/{}):".format(
        usr.get("name"), len(done), len(tsk)))
    for task_title in done:
        print("\t {}".format(task_title))
