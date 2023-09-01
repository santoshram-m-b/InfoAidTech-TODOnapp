#info aid internship
#TASK 2 TO-DO APP

import pickle
class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = "Incomplete"

    def mark_as_done(self):
        self.status = "Complete"

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nStatus: {self.status}\n"
class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
    def view_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"Task {index + 1}:\n{task}")
    def save_tasks(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.tasks, file)
    def load_tasks(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            print("File not found. No tasks loaded.")
def main():
    todo_list = ToDoList()
    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
            print("Task added successfully.")

        elif choice == "2":
            try:
                index = int(input("Enter the task number to delete: ")) - 1
                todo_list.delete_task(index)
                print("Task deleted successfully.")
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            filename = input("Enter the filename to save tasks: ")
            todo_list.save_tasks(filename)
            print("Tasks saved to file.")
        elif choice == "5":
            filename = input("Enter the filename to load tasks from: ")
            todo_list.load_tasks(filename)
            print("Tasks loaded from file.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()

