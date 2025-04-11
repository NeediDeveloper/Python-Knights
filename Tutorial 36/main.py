FILE_NAME = "todo.txt"

def load_file():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
            tasks = [task.strip() for task in tasks]
        return tasks
    except FileNotFoundError:
        return []
        
def update_file(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")        

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    update_file(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if tasks:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks found.")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                delete_task = tasks.pop(task_num - 1)
                update_file(tasks)
                print("Task deleted successfully!")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    tasks = load_file()
    while True:
        print("Menu:")
        print("1. Add task")
        print("2. View all tasks")
        print("3. Delete a task by number")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            delete_task(tasks)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
   
main()