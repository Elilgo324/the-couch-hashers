# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List, Dict
from environment import Contributor, Project


def parse():
    num_contributors, num_projects = (int(x) for x in input().split(' '))
    contributors = []
    for contributor in range(num_contributors):
        contributor_intial = input().split(' ')
        name = contributor_intial[0]
        num_skillz = int(contributor_intial[1])
        skillz = {}
        for skill in range(num_skillz):
            skill = input().split(' ')
            skillz[skill[0]] = int(skill[1])
        contributors.append(Contributor(name, skillz))

    projects = []
    for project in range(num_projects):
        project_intial = input().split(' ')
        project_name = project_intial[0]
        project_length, project_score, project_deadline, project_rolls = (int(project_intial[x]) for x in range(1, 5))
        rolls = {}
        for roll in range(project_rolls):
            roll = input().split(' ')
            rolls[roll[0]] = int(roll[1])
        projects.append(Project(project_name, project_length, project_score, project_deadline, rolls))

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
