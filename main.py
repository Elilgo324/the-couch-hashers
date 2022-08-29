from environment import Contributor, Project
from genetics import Gene

projects = []
contributors = []
max_days = 0


def parse():
    global projects
    global contributors

    num_contributors, num_projects = input()
    contributors = []
    for contributor in range(num_contributors):
        name, num_skillz = input()
        skillz = {}
        for skill in range(num_skillz):
            skill = input()
            skillz[skill[0]] = skill[1]
        contributors.append(Contributor(name, skillz))

    projects = []
    for project in range(num_projects):
        project_name, project_length, project_score, project_deadline, project_rolls = input()
        required_rolls = {}
        for roll in range(project_rolls):
            roll = input()
            required_rolls[roll[0]] = roll[1]
        projects.append(Project(project_name, project_length, project_score, project_deadline, required_rolls))


if __name__ == '__main__':
    parse()

    global max_days
    max_days = max([project.deadline + project.score for project in projects])

    gene = Gene(contributors, projects)
    gene.greedy_init(projects, contributors)
