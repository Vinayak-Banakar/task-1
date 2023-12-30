class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        return self.name

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def print_tasks(self):
        for task in self.tasks:
            print(f"{'[x]' if task.completed else '[_]'} {task.name}")


todo = ToDoList()

task1 = Task("Task 1")
task2 = Task("Task 2")
task3 = Task("Task 3")

todo.add_task(task1)
todo.add_task(task2)
todo.add_task(task3)

task2.complete()

todo.print_tasks()