tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    while True:
        task = input("Enter task (or type 'q' to stop): ")

        if task.lower() == 'q':
            break

        tasks.append({"task": task, "done": False})
        print("Task added!")

def view_tasks():

    if not tasks:
        print("No tasks available.")
        return

    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i}. {t['task']} [{status}]")
def mark_complete():
    view_tasks()
    index = int(input("Enter task index to mark complete: "))

    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print("Task marked as complete!")
    else:
        print("Invalid index!")
def delete_task():
    view_tasks()
    index = int(input("Enter task index to delete: "))
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted!")
    else:
        print("Invalid index!")
while True:
    show_menu()
    choice = input("Enter your option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")