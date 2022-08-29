# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List


def parse():
    num_contributors, num_projects = input()
    contributors = []
    for contributor in range(num_contributors):
        name, num_skillz = input()
        skillz_names, skillz_levels = [], []
        for skill in range(num_skillz):
            skill = input()
            skillz_names.append(skill[0])
            skillz_levels.append(skill[1])
        contributors.append(Contributor(name, skillz_names, skillz_levels))

    projects = []
    for project in range(num_projects):
        project_name, project_length, project_score, project_deadline, project_rolls = input()
        roll_names, roll_levels = [], []
        for roll in range(project_rolls):
            roll = input()
            roll_names.append(roll[0])
            roll_levels.append(roll[1])
        projects.append(Project(project_name, project_length, project_score, project_deadline, roll_names, roll_levels))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
