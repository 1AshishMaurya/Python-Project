# Simple To-Do List App

tasks = []  # List to store tasks

while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f'Task "{task}" added!')

    elif choice == "2":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(f'Task "{task}" removed!')
        else:
            print("Task not found!")

    elif choice == "3":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again!")

        