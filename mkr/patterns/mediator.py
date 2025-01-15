class Project:
    def __init__(self):
        self.members = []
        self.tasks = []

    def add_member(self, member):
        self.members.append(member)
        print(f"Added {member.name} to the project.")

    def assign_task(self, task, role):
        available_member = next((m for m in self.members if isinstance(m, role)), None)
        if available_member:
            self.tasks.append(task)
            print(f"Assigned task '{task}' to {available_member.name}.")
        else:
            print(f"No available {role.__name__} for the task '{task}'.")

    def notify_all(self, message):
        for member in self.members:
            print(f"Notification to {member.name}: {message}")
