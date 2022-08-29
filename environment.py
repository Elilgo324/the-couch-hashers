from typing import Dict, List


class Contributor:
    def __init__(self, name: str, skillz: Dict[str, int]):
        self.name = name
        self.skillz = skillz

    def __repr__(self):
        return f'Contributor(name={self.name}, skills={self.skillz})'

    def __hash__(self):
        return hash(self.name)

    def improve_skill(self, skill_name: str):
        self.skillz[skill_name] += 1


class Project:
    def __init__(self, project_name: str, project_length: int, project_score: int, project_deadline: int,
                 rolls: Dict[str, int]):
        self.name = project_name
        self.length = project_length
        self.score = project_score
        self.deadline = project_deadline
        self.required_rolls = rolls
        self.latest = self.deadline + self.score - 1
        self.purple_score = self.score / self.length

    def __repr__(self):
        return f'Project(name={self.name}, length={self.length}, score={self.score}, deadline={self.deadline},' \
              f'rolls={self.required_rolls})'

    def __hash__(self):
        return hash(self.name)

    def score_on_day(self, day_start: int):
        return max(0, self.score - max(0, day_start + self.length - self.deadline))

    def find_most_fit_contributor(self, contributors: List[Contributor], required_roll: str):
        return max(contributors,
                   key=lambda c: max(c.skillz[required_roll] - self.required_rolls[required_roll], -.5))

    def fit_contributors(self, contributors: List[Contributor], required_roll: str):
        filtered_contributors = [contributor for contributor in contributors if
                                 required_roll in contributor.skillz and
                                 contributor.skillz[required_roll] - self.required_rolls[required_roll] >= 0]
        filtered_contributors.sort(
            key=lambda c: max(c.skillz[required_roll] - self.required_rolls[required_roll], -.5))
        return filtered_contributors

