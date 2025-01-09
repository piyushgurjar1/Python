tasks = []

def add_task():
    task_name = input("Enter the task name: ")    
    tasks.append(task_name)
    print(f"Task '{task_name}' has been added!")

def update_task():
    task_name = input("Enter the task name to update: ")
    if task_name in tasks:
        new_name = input(f"Enter the new name for '{task_name}': ")
        tasks[tasks.index(task_name)] = new_name
        print(f"Task '{task_name}' has been updated to '{new_name}'!")
    else:
        print("Task not found.")

def remove_task():
    task_name = input("Enter the task name to remove: ")
    if task_name in tasks:
        tasks.remove(task_name)
        print(f"'{task_name}' has been removed!")
    else: 
        print("Task not found.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

print('''To-Do List Menu:
    1. Add a task
    2. Update a task
    3. Remove a task
    4. View all tasks''')

while True:  
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        update_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        view_tasks()
    else:
        print("Invalid option.")
        break
