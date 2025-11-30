class Task:
    FILENAME = "tasks.json"
    def __init__(self,id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self): #Sobreescribimos funciones string
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.id}: {self.description}"
    
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        print(f"Task added: {task}")


    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                print(f"Task completed: {task}")
                self.save_tasks()
                return 

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                self.save_tasks()
                return


    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def load_tasks(self):
        import json
        try:
            with open(Task.FILENAME, 'r') as f:
                tasks_data = json.load(f)
                for task_data in tasks_data:
                    task = Task(task_data['id'], task_data['description'], task_data['completed'])
                    self.tasks.append(task)
                    self.next_id = max(self.next_id, task.id + 1)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        import json
        with open(Task.FILENAME, 'w') as f:
            tasks_data = [{'id': task.id, 'description': task.description, 'completed': task.completed} for task in self.tasks]
            json.dump(tasks_data, f, indent=4)