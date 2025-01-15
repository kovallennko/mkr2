from patterns.factory import TeamFactory
from patterns.mediator import Project
from patterns.observer import Task
from models.team_member import Developer, Tester

# Створення проєкту
project = Project()

# Додавання членів команди через фабрику
dev = TeamFactory.create_member('Developer', 'Alice', 5, ['Python', 'Java'])
tester = TeamFactory.create_member('Tester', 'Bob', 3, ['Unit Testing', 'Integration Testing'])
pm = TeamFactory.create_member('ProjectManager', 'Charlie', 10, 8)

project.add_member(dev)
project.add_member(tester)
project.add_member(pm)

# Створення та призначення завдань
task1 = Task('Develop new feature')
task2 = Task('Test new feature')

project.assign_task('Develop new feature', Developer)
project.assign_task('Test new feature', Tester)

# Додавання спостерігачів
task1.add_observer(dev)
task2.add_observer(tester)

# Зміна статусу завдань
task1.set_status('In Progress')
task2.set_status('Completed')
