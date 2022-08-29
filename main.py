# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List


class Contributor:
    def __init__(self, name: str, skillz_names: List[str], skillz_levels: List[int]):
        self.name = name
        self.skillz = skillz_names
        self.skillz_levels = skillz_levels

    def __repr__(self):
        return f'Contributor(name={self.name}, skills={self.skillz})'


class Project:
    def __init__(self, project_name: str, project_length: int, project_score: int, project_deadline: int,
                 roll_names: List[str], roll_levels: List[int]):
        self.name = project_name
        self.length = project_length
        self.score = project_score
        self.deadline = project_deadline
        self.rolls = roll_names
        self.roll_levels = roll_levels

    def __repr__(self):
        return f'Project(name={self.name}, length={self.length}, score={self.score}, deadline={self.deadline},' \
              f'rolls={self.rolls})'


def parse():
    num_contributors, num_projects = (int(x) for x in input().split(' '))
    contributors = []
    for contributor in range(num_contributors):
        contributor_intial = input().split(' ')
        name = contributor_intial[0]
        num_skillz = int(contributor_intial[1])
        skillz_names, skillz_levels = [], []
        for skill in range(num_skillz):
            skill = input().split(' ')
            skillz_names.append(skill[0])
            skillz_levels.append(int(skill[1]))
        contributors.append(Contributor(name, skillz_names, skillz_levels))

    projects = []
    for project in range(num_projects):
        project_intial = input().split(' ')
        project_name = project_intial[0]
        project_length, project_score, project_deadline, project_rolls = (int(project_intial[x]) for x in range(1, 5))
        roll_names, roll_levels = [], []
        for roll in range(project_rolls):
            roll = input().split(' ')
            roll_names.append(roll[0])
            roll_levels.append(int(roll[1]))
        projects.append(Project(project_name, project_length, project_score, project_deadline, roll_names, roll_levels))

    return contributors, projects


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    contributors, projects = parse()
    print(contributors)
    print(projects)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
