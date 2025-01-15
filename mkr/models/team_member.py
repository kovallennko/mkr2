class TeamMember:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

class Developer(TeamMember):
    def __init__(self, name, experience, skills):
        super().__init__(name, experience)
        self.skills = skills

class Tester(TeamMember):
    def __init__(self, name, experience, test_types):
        super().__init__(name, experience)
        self.test_types = test_types

class ProjectManager(TeamMember):
    def __init__(self, name, experience, projects_completed):
        super().__init__(name, experience)
        self.projects_completed = projects_completed
