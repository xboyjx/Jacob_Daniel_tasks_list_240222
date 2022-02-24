

# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    completed_tasks =[]
    for task in list:
        if task["completed"] == False:
            completed_tasks.append(task)

    return completed_tasks 
            

## Get a list of completed tasks
def get_completed_tasks(list):
    uncompleted_tasks =[]
    for task in list:
        if task["completed"] == True:
            uncompleted_tasks.append(task)
        
    return uncompleted_tasks
## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    tasks_with_time = []
    for task in list:
        if task["time_taken"] >= time:
            tasks_with_time.append(task)

    return tasks_with_time

## Find a task with a given description
def get_task_with_description(list, description):
    found = False
    for task in list:
        if task["description"] == description:
            return task
    if found == False:
        return "error"

# Extention (Function): 






def print_task(task):
    print(f'Description: { task["description"] }')
    print(f'Status: { "Completed" if task["completed"] else "Incomplete"}')
    print(f'Time Taken: {task["time_taken"]} mins')

def print_list(list):
    for task in list:
        print_task(task)

def print_menu():
    print("Options:")
    print("1: Display All Tasks")
    print("2: Get Uncompleted Tasks")
    print("3: Get Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")