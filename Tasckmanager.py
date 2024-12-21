class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        return f"Task: {self.title}, Deadline: {self.deadline}, Completed: {self.is_completed}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def show_tasks(self):
        for task in self.tasks:
            print(task)


# Приклад використання:
task1 = Task("Завершити домашку", "Завершити математичну домашню роботу", "2024-12-21")
task2 = Task("Купити продукти", "Купити молоко та хліб", "2024-12-22")

manager = TaskManager()
manager.add_task(task1)
manager.add_task(task2)

manager.show_tasks()
task1.mark_completed()
manager.show_tasks()
