todo_list = []

def show_menu():
    print("\nTo-Do List Options:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        task = input("Enter new task: ")
        todo_list.append(task)
        print("Task added!")
    elif choice == '2':
        if todo_list:
            print("\nYour Tasks:")
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")
        else:
            print("No tasks found.")
    elif choice == '3':
        try:
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(todo_list):
                removed = todo_list.pop(num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
