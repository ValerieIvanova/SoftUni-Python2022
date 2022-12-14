from task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in [task.name for task in self.tasks]:
            return f"Could not find task with the name {task_name}"

        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        removed_tasks = 0
        for task in filter(lambda x: x.completed, self.tasks):
            self.tasks.remove(task)
            removed_tasks += 1
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        result = [f"Section {self.name}:"]
        [result.append(t.details()) for t in self.tasks]

        return '\n'.join(result)