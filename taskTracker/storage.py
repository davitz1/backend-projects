import os 
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return {}
    with open(TASKS_FILE, "r") as f:
        return json.load(f) #returns a dict from the json file

def save_tasks(tasks): #take a dict as input
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def generate_id(tasks):
    if not tasks:
        return "1"
    return str(int(max(tasks, key = int)) + 1)
