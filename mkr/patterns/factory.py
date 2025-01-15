from models.team_member import Developer, Tester, ProjectManager

class TeamFactory:
    @staticmethod
    def create_member(role, name, experience, extra_info):
        if role == 'Developer':
            return Developer(name, experience, extra_info)
        elif role == 'Tester':
            return Tester(name, experience, extra_info)
        elif role == 'ProjectManager':
            return ProjectManager(name, experience, extra_info)
        else:
            raise ValueError(f"Unknown role: {role}")
