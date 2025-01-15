class Task:
    def __init__(self, description):
        self.description = description
        self.status = 'New'
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def set_status(self, status):
        self.status = status
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

class Member:
    def __init__(self, name):
        self.name = name

    def update(self, task):
        print(f"{self.name} received update: Task '{task.description}' is now '{task.status}'.")
