import os

class Task:
    def __init__(self, description, deadline=None):
        self.description = description
        self.deadline = deadline

    def __str__(self):
        return f"{self.description}" + (f" (Due: {self.deadline})" if self.deadline else "")

class ToDoApp:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        tasks = []
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    parts = line.strip().split("||")
                    description = parts[0]
                    deadline = parts[1] if len(parts) > 1 else None
                    tasks.append(Task(description, deadline))
        return tasks

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                line = task.description
                if task.deadline:
                    line += f"||{task.deadline}"
                file.write(line + "\n")

    def add_task(self):
        description = input("Enter task: ")
        deadline = input("Enter deadline (or press Enter to skip): ")
        task = Task(description, deadline if deadline else None)
        self.tasks.append(task)
        self.save_tasks()
        print("Task added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks.")
            return
        print("\nYour Tasks:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def remove_task(self):
        self.view_tasks()
        try:
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(self.tasks):
                removed = self.tasks.pop(num - 1)
                self.save_tasks()
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a valid number.")

    def run(self):
        while True:
            print("\nTo-Do Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Remove Task")
            print("4. Exit")
            choice = input("Choose option (1-4): ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.remove_task()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

# Run the app
app = ToDoApp()
app.run()
