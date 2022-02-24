
# Functions to complete:



# Extention (Function): 

## Get a list of tasks by status
# def get_tasks_by_status(list, status):
    # pass

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)





