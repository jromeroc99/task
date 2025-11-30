import task_manager
def main():
    while True:
        print(" Task Manager Application ")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")

        choice = input("Choose an option (1-4): ")

        match choice:
            case '1':
                description = input("Enter task description: ")     
                task_manager.add_task(description)
            case '2':
                task_manager.list_tasks()
            case '3':
                task_id = int(input("Enter task ID to complete: "))
                task_manager.complete_task(task_id)
            case '4':
                task_id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(task_id)
            case '5':
                print("Exiting Task Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    task_manager = task_manager.TaskManager()
    main()