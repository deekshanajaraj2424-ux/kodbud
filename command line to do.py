# Command Line To-Do List Application

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add a task
    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    # View tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

    # Delete a task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available to delete.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

            task_number = int(input("Enter the task number to delete: "))

            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print("Task deleted:", deleted_task)
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "4":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")