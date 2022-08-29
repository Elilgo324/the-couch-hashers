from typing import Dict, List


class Contributor:
    def __init__(self, name: str, skillz: Dict):
        self.name = name
        self.skillz = skillz

    def improve_skill(self, skill_name: str):
        self.skillz[skill_name] += 1


class Project:
    def __init__(self, project_name: str, project_length: int, project_deadline: int, project_score: int, required_rolls: Dict):
        self.name = project_name
        self.length = project_length
        self.score = project_score
        self.deadline = project_deadline
        self.required_rolls = required_rolls

    def get_greedy_contributors_assignment(self) -> List[Contributor]:
        pass
