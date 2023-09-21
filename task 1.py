import json
from datetime import datetime

# Function to load tasks from a JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
            return []

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to display tasks
def display_tasks(tasks, category=None):
    if not tasks:
        print("No tasks found.")
          return

    tasks_to_display = tasks if category is None else [task for task in tasks if task.get('category') == category]
    
    if not tasks_to_display:
        print("No tasks in this category.")
          return

    print("Tasks:")
    sorted_tasks = sorted(tasks_to_display, key=lambda x: x['due_date'])
    for index, task in enumerate(sorted_tasks, start=1):
        status = "Done" if task['done'] else "Not Done"
          print(f"{index}. {task['title']} - {task['description']} - Due: {task['due_date']} - Status: {status} - Category: {task.get('category', 'Uncategorized')}")

# Function to add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
          return

    category = input("Enter task category (optional): ")

    tasks.append({"title": title, "description": description, "due_date": due_date, "done": False, "category": category})
    save_tasks(tasks)
         print("Task added successfully!")

# Function to edit a task
def edit_task(tasks):
    display_tasks(tasks)
    choice = int(input("Enter the number of the task to edit: "))

    if 1 <= choice <= len(tasks):
        task = tasks[choice - 1]
        print(f"Editing Task '{task['title']}':")
        task['title'] = input("New title (press Enter to keep current): ") or task['title']
        task['description'] = input("New description (press Enter to keep current): ") or task['description']
        due_date = input(f"New due date (YYYY-MM-DD, press Enter to keep current: {task['due_date']}): ")
        if due_date:
            try:
                task['due_date'] = datetime.strptime(due_date, "%Y-%m-%d").strftime("%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")
                return
        task['category'] = input(f"New category (press Enter to keep current: {task.get('category', 'None')}): ") or task.get('category')
        save_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Invalid choice.")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("\n1. Display tasks")
        print("\n2. Display tasks by category")
        print("\n3. Add a task")
        print("\n4. Edit a task")
        print("\n5. Mark a task as done")
        print("\n6. Remove a task")
        print("\n7. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            category = input("Enter category to filter (press Enter to show all): ")
            display_tasks(tasks, category)
        elif choice == '3':
            add_task(tasks)
        elif choice == '4':
            edit_task(tasks)
        elif choice == '5':
            display_tasks(tasks)
            mark_task_done(tasks)
        elif choice == '6':
            remove_task(tasks)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

