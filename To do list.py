tasks = []

def show_menu():
    print("\n--- TO-DO LIST APPLICATION ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")
    for i, item in enumerate(tasks, start=1):
        status = "✓ Completed" if item["completed"] else "✗ Pending"
        print(f"{i}. {item['task']} - {status}")

def update_task():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("Enter task number to update: "))
            if 1 <= task_no <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[task_no - 1]["task"] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"Deleted: {removed['task']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def mark_completed():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("Enter task number to mark as completed: "))
            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        mark_completed()
    elif choice == "6":
        print("Exiting To-Do List Application. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
