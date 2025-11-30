import task_manager
import os
import ai_service
def main():
    while True:

        print(" Task Manager Application ")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Create Simple Tasks using AI")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")
        os.system('cls' if os.name == 'nt' else 'clear')
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
                task = input("Enter a task to create simple sub-tasks: ")
                simple_tasks = ai_service.create_simple_tasks(task)
                for sub_task in simple_tasks:
                    task_manager.add_task(sub_task)
            case '6':
                print("Exiting Task Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    task_manager = task_manager.TaskManager()
    main()